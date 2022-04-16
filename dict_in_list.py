

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


# creatign a function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,times_visited,cities_visited):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 2, ["Haryana", "Punjab"])


print(travel_log)



