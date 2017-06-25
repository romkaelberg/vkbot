TOKEN_VK = ""
TOKEN_APIXUWEATHER= ""
import vk, os, math, json,time,re,requests
from geopy.geocoders import GoogleV3

session = vk.Session(access_token=TOKEN_VK)
API_VK = vk.API(session)

def messages_data(): #получаем массив сообщений
    return API_VK.messages.getDialogs()

def number_of_messages(): #вынимаем количество сообщений
    return _messages_data[0]

def get_weather(city): #погода
    geolocator = GoogleV3()
    location = geolocator.geocode(city)
    if location != None:
        response = requests.get('https://api.apixu.com/v1/current.json?key=' +TOKEN_APIXUWEATHER+'&q=' + str(location.latitude) + ',' + str(location.longitude))
        result = json.loads(response.content.decode())
        # print(result['location']['name'])
        temp = result['current']['temp_c']
        return temp
    
def command_handler(message): #обработчик комманд
    message_split_array = message.split(' ')
    command = message_split_array[0]
    if bool(re.match(r'^!п.?г.?д.?', command, re.I)) == True and len(message_split_array) == 2:
        city = message_split_array[1]
        _get_weather = get_weather(city)
        return city,_get_weather
    else:
        return False

def send_message(user_id,message): #отправка сообщения
    API_VK.messages.send(user_id=user_id,message=message)

while True: #беспрерывное получение сообщений
    _messages_data = messages_data() #переменная с сообщениями
    _number_of_messages = number_of_messages() #переменная с количеством сообщений

    if _number_of_messages == 1: #проверка на одиночное сообщение
        message = _messages_data[1]['body']
        print(message)
        message_id = _messages_data[1]['mid']
        user_id = _messages_data[1]['uid']
        _command_handler = command_handler(message) #переменная с городом, погодой или False

        if _command_handler != False: #если команда корректная
            city = _command_handler[0]  # т.к command_handler() возвращает массив
            temp = _command_handler[1]  # т.к command_handler() возвращает массив

            if temp != None: #проверка на правильность города
                message = "Сейчас в городе " + city + " " + str(temp) + " градусов тепла:)"
                send_message(user_id, message)
            else:
                message = "Такого города нету!"
                send_message(user_id, message)

    if _number_of_messages > 1: #если сообщений > 1
        for i in range(_number_of_messages+1):

            if i > 0: #т.к _messages_data[0] - счетчик сообщений, а после него сами сообщения
                message = _messages_data[i]['body'] #переменная с текущим сообщением
                message_id = _messages_data[i]['mid']#переменная с текущим id сообщения
                user_id = _messages_data[i]['uid']#переменная с текущим id юзера
                _command_handler = command_handler(message) #переменная с городом, погодой или False

                if _command_handler != False:
                    city = _command_handler[0] #т.к command_handler() возвращает массив
                    temp = _command_handler[1] #т.к command_handler() возвращает массив

                    if temp != None: #проверка на правильность города
                        message = "Сейчас в городе " + city + " " + str(temp) + " градусов тепла:)"
                        send_message(user_id,message)
                    else:
                        message = "Такого города нету!"
                        send_message(user_id, message)
        time.sleep(1)
