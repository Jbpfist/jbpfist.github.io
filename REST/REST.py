
import requests
import json
errormessage='Invalid input please enter a valid zip code or city name'
def zip( zipcode ):

    api_key = "91e2c0c842117d035d6694903512f133"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url +"appid=" + api_key + '&zip=' + zipcode + '&units=imperial'
    response = requests.get(final_url)
    data = json.loads(response.text)
    try:
        temp = data['main']['temp']
        feelslike = data['main']['feels_like']
        return 'The current temperature in '+str(zipcode)+' is '+str(temp)+'\n'+'and feels like '+str(feelslike)
    except:
        return errormessage


def city( cityname ):
    api_key = "91e2c0c842117d035d6694903512f133"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url +"appid=" + api_key + '&q=' + cityname + '&units=imperial'
    response = requests.get(final_url)
    data = json.loads(response.text)
    try:
        temp = data['main']['temp']
        feelslike = data['main']['feels_like']
        return 'The current temperature in '+str(cityname)+' is '+str(temp)+'\n'+'and feels like '+str(feelslike)
    except:
        return errormessage

def main():
    weather = input('Please tell us where you would like to know the weather using either a city name or your zip code')
    zipresponse = zip(weather)
    cityresponse = city(weather)
    if zipresponse==errormessage and cityresponse==errormessage:
        print(errormessage)
    elif zipresponse!=errormessage and cityresponse==errormessage:
        print(zipresponse)
    elif cityresponse!=errormessage and zipresponse==errormessage:
        print(cityresponse)
    elif cityresponse!=errormessage and zipresponse!=errormessage:
        print(zipresponse)

    keepgoing=input("Do you want to check another location? Y/N?")
    if keepgoing == "Y":
        main()
main()

