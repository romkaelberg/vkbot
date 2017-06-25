TOKEN_VK = ""
TOKEN_APIXUWEATHER= ""
import vk, os, math, json,time,re,requests
from geopy.geocoders import GoogleV3

def enter_command():
    command = input("enter command: ")
    return command
# command = enter_command()

session = vk.Session(access_token=TOKEN_VK)
API_VK = vk.API(session)

def messages_data():
    return API_VK.messages.getDialogs()

def number_of_messages():
    return _messages_data[0]

def get_weather(city):
    geolocator = GoogleV3()
    location = geolocator.geocode(city)
    if location != None:
        response = requests.get('https://api.apixu.com/v1/current.json?key=' +TOKEN_APIXUWEATHER+'&q=' + str(location.latitude) + ',' + str(location.longitude))
        result = json.loads(response.content.decode())
        # print(result['location']['name'])
        temp = result['current']['temp_c']
        return temp
    
def command_handler(message):
    message_split_array = message.split(' ')
    command = message_split_array[0]
    if bool(re.match(r'^!п.?г.?д.?', command, re.I)) == True and len(message_split_array) == 2:
        city = message_split_array[1]
        _get_weather = get_weather(city)
        return city,_get_weather
    else:
        return False

def send_message(user_id,message):
    API_VK.messages.send(user_id=user_id,message=message)

while True:
    _messages_data = messages_data()
    _number_of_messages = number_of_messages()

    if _number_of_messages == 1:
        message = _messages_data[1]['body']
        print(message)
        message_id = _messages_data[1]['mid']
        user_id = _messages_data[1]['uid']
        _command_handler = command_handler(message)

        if _command_handler != False:
            city = _command_handler[0]  # т.к command_handler() возвращает массив
            temp = _command_handler[1]  # т.к command_handler() возвращает массив

            if temp != None:
                message = "Сейчас в городе " + city + " " + str(temp) + " градусов тепла:)"
                send_message(user_id, message)
            else:
                message = "Такого города нету!"
                send_message(user_id, message)

    if _number_of_messages > 1:
        for i in range(_number_of_messages+1):

            if i > 0: #т.к _messages_data[0] - счетчик сообщений, а после него сами сообщения
                message = _messages_data[i]['body']
                message_id = _messages_data[i]['mid']
                user_id = _messages_data[i]['uid']
                # print(message_id)
                # print(message)

                # if _checker_of_command == True:
                _command_handler = command_handler(message)

                if _command_handler != False:
                    city = _command_handler[0] #т.к command_handler() возвращает массив
                    temp = _command_handler[1] #т.к command_handler() возвращает массив

                    if temp != None:
                        message = "Сейчас в городе " + city + " " + str(temp) + " градусов тепла:)"
                        send_message(user_id,message)
                    else:
                        message = "Такого города нету!"
                        send_message(user_id, message)
        time.sleep(1)
