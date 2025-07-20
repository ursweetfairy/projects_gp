import requests
from pprint import pprint

# Asystent podróży
# Api pogodowe - https://openweathermap.org/api
# Api z informacjami o krajach - https://restcountries.com/
# Api z informacjami o kursach walut - https://api.nbp.pl/#info


API_KEY = #Tu wpisz swój klucz API

def check_coordinates(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    #print(response.status_code)
    #pprint(response.json())
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, city, country

def get_weather_info(lat,lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    #print(response.status_code)
    #pprint(response.json())
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temperature, pressure, humidity

def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code

def get_country_full_name(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    country_name = response.json()[0]['name']['common']
    return country_name

print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")
origin_city = input("Podaj nazwę miasta z którego podróżujesz: ")
destitanion_city = input("Podaj nazwę miasta do którego podróżujesz: ")

origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city,API_KEY)
destitanion_lat, destitanion_lon, destitanion_city, destitanion_country = check_coordinates(destitanion_city,API_KEY)

ori_curr = get_currency_code(origin_country)
dest_curr = get_currency_code(destitanion_country)

weather, temperature, pressure, humidity = get_weather_info(destitanion_lat,destitanion_lon)


print(f"Miasto z którego podróżujesz: {origin_city}")
print(f"Leży w kraju {get_country_full_name(origin_country)}")
print(f"Obowiązująca waluta to {ori_curr}")
print(f"Miasto do którego podróżujesz: {destitanion_city}")
print(f"Miasto leży w kraju {get_country_full_name(destitanion_country.lower())}")
print(f"Obowiązująca waluta to {dest_curr}")
print(f"Jego współrzędne geograficzne to:\n{destitanion_lat} szerokości geograficznej \n{destitanion_lon} dlugości geograficznej")
print(f"Pogoda : {weather}")   
print(f"Temperatura {temperature} st.Celcjusza")
print(f"wilgotność: {humidity}%")
print(f"ciśnienie atmosferyczne {pressure}hPa")
