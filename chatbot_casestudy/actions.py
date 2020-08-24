from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"641b84e1301a9db5ddb6cee18507f066"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        pricerangemin = tracker.get_slot('pricerangemin')
        pricerangemax = tracker.get_slot('pricerangemax')
        location_detail= zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'American':1,'Chinese':25,'Mexican':73,'Italian':55,'North Indian':50,'South Indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        response=""
        
        if d['results_found'] == 0:
            response= "No results found for Location and Cusine type requested"
        else:
            for restaurant in d['restaurants']:
                if  (float(restaurant['restaurant']['average_cost_for_two']) < float(pricerangemax)) &  (float(restaurant['restaurant']['average_cost_for_two']) > float(pricerangemin)):
                    response=response+restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+" with Average Price: "+str(restaurant['restaurant']['average_cost_for_two'])+"\n"
                else:
                    response = response

        if response == "":
            response= "No results found for Location and Cusine type requested in the price range between "+str(pricerangemin)+ " and " + str(pricerangemax)
                    
        dispatcher.utter_message("-----"+response)
        return [SlotSet('pricerangemin',pricerangemin),SlotSet('pricerangemax',pricerangemax)]
        

class ActionCheckLocation(Action):
    def name(self):
        return 'action_check_location'
        
    def run(self, dispatcher, tracker, domain):
        city_tier1_tier2=['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Aligarh','Amravati','Amritsar',
                      'Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','Bokaro',
                      'Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur',
                      'Gulbarga','Guntur','Gwalior','Gurgaon','Guwahati','Hamirpur','Hubli','Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar',
                      'Jamshedpur','Jhansi','Jodhpur','Kakinada','Kannur','Kanpur','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow',
                      'Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Patna',
                      'Pondicherry','Purulia','Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Shimla','Siliguri','Solapur',
                      'Srinagar','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tiruppur','Ujjain','Bijapur','Vadodara','Varanasi','Vasai','Virar',
                      'Vijayawada','Visakhapatnam','Vellore','Warangal']
        loc = tracker.get_slot('location')
        
        if loc.title() not in city_tier1_tier2:
            response= "Sorry,We do not operate in that area yet"
            dispatcher.utter_message("-----"+response)
            
        return [SlotSet('location',loc)]
        


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        import yagmail
        
        config={ "user_key":"b6e35f9b60aa69bca3fab190730d871b"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        email_v = tracker.get_slot('email')
        cuisine = tracker.get_slot('cuisine')
        pricerangemin = tracker.get_slot('pricerangemin')
        pricerangemax = tracker.get_slot('pricerangemax')
        location_detail= zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'American':1,'Chinese':25,'Mexican':73,'Italian':55,'North Indian':50,'South Indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
        d = json.loads(results)
        response=""
        if d['results_found'] == 0:
            response= "No results found for Location and Cusine type requested"
        else:
            for restaurant in d['restaurants']:
                if  (float(restaurant['restaurant']['average_cost_for_two']) < float(pricerangemax)) &  (float(restaurant['restaurant']['average_cost_for_two']) > float(pricerangemin)):
                    response=response+restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+" with Average Price: "+str(restaurant['restaurant']['average_cost_for_two'])+"\n"
                else:
                    response = response
                  
        if response == "":
            response= "No results found for Location and Cusine type requested in the price range between "+str(pricerangemin)+ " and " + str(pricerangemax)
        
        receiver = email_v
        body = "Hi Sir/Madam"+"\n"+"\n"+"Below are the requested restaurants"+"\n"+response+"\n"+"Thanks"

        yag = yagmail.SMTP("dineshsumanupgradchatbot@gmail.com")
        yag.send(
        to=receiver,
        subject="Top 10 Restaurants as per your request",
        contents=body, 
        #attachments=filename,
        )
        dispatcher.utter_message("-----"+"Email Sent,Bon Appetit!")
        return [SlotSet('email',receiver)]
