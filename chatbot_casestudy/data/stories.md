## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "delhi"}
    - utter_ask_price_range
* restaurant_search
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "adfakfaek"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "adfakfaek"}
    - action_check_location
    - slot{"location": "adfakfaek"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Hyderabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Hyderabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Hyderabad"}
    - utter_ask_price_range
* restaurant_search 
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_email
* restaurant_search{"email": "abcde@gmail.com"}
    - slot{"email": "abcde@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* goodbye
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Mumbai"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Mumbai"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": "20000"}
    - utter_ask_email
* goodbye
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mumbai"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": "20000"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"type": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "unknownlocation"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "unknownlocation"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_check_location
    - slot{"location": "unknownlocation"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "300", "pricerangemax": "700"}
    - slot{"pricerangemax": "700"}
    - slot{"pricerangemin": "300"}
    - action_search_restaurants
    - slot{"pricerangemin": "300"}
    - slot{"pricerangemax": "700"}
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": "20000"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Baroda"}
    - slot{"location": "Baroda"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "300", "pricerangemax": "700"}
    - slot{"pricerangemax": "700"}
    - slot{"pricerangemin": "300"}
    - action_search_restaurants
    - slot{"pricerangemin": "300"}
    - slot{"pricerangemax": "700"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": "20000"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "Ujjain"}
    - slot{"location": "Ujjain"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "0", "pricerangemax": "300"}
    - slot{"pricerangemax": "300"}
    - slot{"pricerangemin": "0"}
    - action_search_restaurants
    - slot{"pricerangemin": "0"}
    - slot{"pricerangemax": "300"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Bhopal", "pricerangemin": "300", "pricerangemax": "700"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Bhopal"}
    - slot{"pricerangemax": "700"}
    - slot{"pricerangemin": "300"}
    - action_search_restaurants
    - slot{"pricerangemin": "300"}
    - slot{"pricerangemax": "700"}
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkata", "pricerangemin": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": 20000.0}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* affirm
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Hubli", "pricerangemax": "300"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Hubli"}
    - slot{"pricerangemax": "300"}
    - action_search_restaurants
    - slot{"pricerangemin": 0.0}
    - slot{"pricerangemax": "300"}
    - action_send_email
    - slot{"email": null}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chennai", "pricerangemin": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": 20000.0}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* affirm
    - utter_goodbye

## interactive_story_2
* restaurant_search{"cuisine": "American", "location": "Delhi", "pricerangemin": "700"}
    - slot{"cuisine": "American"}
    - slot{"location": "Delhi"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": 20000.0}
    - utter_ask_email
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "dineshsumanupgradchatbot@gmail.com"}
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
    - action_send_email
    - slot{"email": "dineshsumanupgradchatbot@gmail.com"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - utter_ask_price_range
* restaurant_search{"pricerangemin": "700", "pricerangemax": "20000"}
    - slot{"pricerangemax": "20000"}
    - slot{"pricerangemin": "700"}
    - action_search_restaurants
    - slot{"pricerangemin": "700"}
    - slot{"pricerangemax": "20000"}
    - utter_ask_email
* goodbye
    - utter_goodbye
