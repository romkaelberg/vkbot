import vk, os, math, json,time
from messages_list import print_messages
# <Авторизация>
#Для авторизации перейти по ссылке и скопировать поле acess_token. https://oauth.vk.com/authorize?client_id=ID_ВАШЕГО_ПРИЛОЖЕНИЯ&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&scope=8194
#app_id = 6071061
access_token = "e473baceb5969241b87d9d37ff7a32e6d8d29fe7237401512498931f3e158083b33d7107d3d0d8c0260bb"
session = vk.Session(access_token=access_token)
vkapi = vk.API(session)

#</Авторизация>
#<Получаем новые сообщения, через связь с LongPool сервером>
def messages_flow():
    server_connect = vkapi.messages.getLongPollServer()
    ts_value = server_connect['ts']
    for i in range(999):
        time.sleep(1)
        os.system('clear')
        print(vkapi.messages.getLongPollHistory(ts=ts_value))
#</Получаем новые сообщения, через связь с LongPool сервером>
    # <Проверка, работает нестабильно>
def check(el):
    if el:

        print("| CONNECTION ESTABILISHED!" + "\n")
    else:
        print("ERROR!")
# </ Проверка vkapi>
# </ Модули>
check(access_token)

# wall_posts = vkapi.wall.get() #получаем записи

# number_of_wall_posts = wall_posts[0] #получаем кол-во записей

# wall_posts_list(wall_posts,number_of_wall_posts)

messages = vkapi.messages.getDialogs()

number_of_messages = messages[0]

print_messages(messages, number_of_messages,vkapi)

# messages_flow()