## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- sure
- alright
- okay done
- Thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- No
- no

## intent:greet
- hey
- howdy
- hey there
- hello
- hi there
- good morning
- good evening
- good afternoon
- dear sir
- hi
- hi sir
- hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- show me [American](cuisine) restaurants
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [American](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please find [Mexican](cuisine) restaurant in [Hyderabad](location)
- I’m hungry. Looking out for some good restaurants
- I feel like eating something
- Where can I get something to eat
- what's a good dining place
- Can you suggest some good restaurants in [Rishikesh](location)
- please find [South Indian](cuisine) restaurant in [Mumbai](location)
- please find [south indian](cuisine) restaurant in [mumbai](location)
- [dineshsumanupgradchatbot@gmail.com](email)
- please find [Mexican](cuisine) restaurant in [unknownlocation](location)
- Im hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- Im hungry. Looking out for some good restaurants
- [pune](location)
- [Baroda](location)
- [Nagpur](location)
- [Ujjain](location)
- please find [North Indian](cuisine) restaurant in [Bhopal](location) for price [300](pricerangemin) to [700](pricerangemax)
- want something [Chinese]{"entity": "cuisine", "value": "chinese"} to eat in [kolkata](location) for price >[700](pricerangemin)
- get me something [South Indian](cuisine) to eat in [Hubli](location) for price less than [300](pricerangemax)
- can I get something [chinese](cuisine) to eat in [Chennai](location) for price greater than [700](pricerangemin)
- Hungry,want to something [American](cuisine) to eat in [Delhi](location) for price more than [700](pricerangemin)
- please find [chinese](cuisine) restaurant  to eat in [Chennai](location)

## synonym: Ahmedabad
- Amdavad
- Amdabad
- amdavad
- amdabad
- ahmedabad

## synonym: Cochin
- Kochi

## synonym: Gurugram
- Gurgaon
- gurgaon
- gurugram

## synonym: Guwahati
- Gauhati
- gauhati
- guwahati

## synonym: Kolkata
- Calcutta
- calcutta
- kolkata
- kolkatta

## synonym: Mysore
- Mysuru
- mysuru
- mysore

## synonym: Nellore
- Simhapuri
- simhapuri
- nellore

## synonym: Pondicherry
- Puducherry
- pondicherry
- pondichery
- Pondichery

## synonym: Prayagraj
- Allahabad
- Illahabad

## synonym: Pune
- Poona
- pune

## synonym: Rajahmundry
- Rajahmahendravaram
- Rajamundry

## synonym: Thrissur
- Trichur

## synonym: Tiruchirapalli
- Trichy

## synonym: Vadodara
- Baroda

## synonym: Varanasi
- Banaras
- Benaras

## synonym: Vijayawada
- Bejawada

## synonym: Visakhapatnam
- Vizag
- Visakhapattanam

## synonym: less
- lower
- <

## synonym: more
- greater
- >

## synonym:4
- four

## synonym:Bangalore
- Bengaluru

## synonym:Delhi
- New Delhi
- Nai dilli
- New Dilli
- Dehli

## synonym:Mumbai
- Bombay
- Bambai

## synonym:Thiruvananthapuram
- Trivandrum

## synonym:chennai
- Madras

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:thanks
- Thx
- Thnks
- Ty

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hello[^\s]*
- hey[^\s]*
- hi[^\s]*
- hola[^\s]*

## regex:pincode
- [0-9]{6}
