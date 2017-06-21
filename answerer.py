import time
from geopy.geocoders import GoogleV3
import requests
import json

def ans_messages(messages,number_of_messages,api):
    geolocator = GoogleV3()

    if number_of_messages == 1:
        i = 1
        print("|-----------------------------------------------")
        userid = messages[1]['uid']
        message = messages[1]['body']
        print("| USERID: " + str(userid))
        print("| MESSAGE: " + message)
    if number_of_messages > 1:
        last_mes_id = 0
        for i in range(number_of_messages+1):
            if i > 0:
                userid = messages[i]['uid']
                message = messages[i]['body']
                # print("| USERID: " + str(userid))
                # print("| MESSAGE: " + message)
                try:
                    status = float(message)
                    # print(status)
                except ValueError:
                    status = str()
                if message == "привет" or message == "Привет":
                    welcome = "Привет, я - бот погоды, напиши мне свой город и страну и я пришлю тебе погоду в твоем городе"
                    api.messages.send(user_id=userid, message=welcome)
                if type(status) == str:
                    location = geolocator.geocode(message)
                    # print(location.latitude,location.longitude)
                    # print(location.address)
                    if location !=None:
                        response = requests.get('https://api.apixu.com/v1/current.json?key=6d9d5f6b5f534ea69a191950172106&q=' + str(location.latitude) + ',' + str(location.longitude))
                        result = json.loads(response.content.decode())
                        # print(result['location']['name'])
                        temp = result['current']['temp_c']
                        last_mes_id = messages[i]['mid']
                        api.messages.send(user_id=userid,message=temp)
                        if temp > 15:
                            last_mes_id = messages[i]['mid']
                            api.messages.send(user_id=userid,message=" градусов тепла")
                        else:
                            last_mes_id = messages[i]['mid']
                            api.messages.send(user_id=userid, message=" градусов холода, xD, смотри не простудись")
                        if messages[i]['mid'] != last_mes_id and last_mes_id != 0:
                            print(message)
                time.sleep(1)