#<Парсер сообщений пользователя>
import time
def print_messages(messages,number_of_messages,api):
    print("| MESSAGES LIST ")
    print(number_of_messages)
    for i in range(number_of_messages):

        if i > 0:
            user = api.users.get(user_id=messages[i]['uid'])
            print("|-----------------------------------------------")
            print("| USER: " + user[0]['first_name'] +" "+ user[0]['last_name'])
            print("| USERID: " + str(user[0]['uid']))
            print("| MESSAGE: " + messages[i]['body'])
            time.sleep(1)