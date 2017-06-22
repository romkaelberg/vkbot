#ROMKA
import vk, os, math, json,time
from messages_list import print_messages
from check import check
from answerer import ans_messages
from geopy.geocoders import GoogleV3
import requests
import json
#app_id = 6071061
command = input("enter command: ")
def setup():
    f = open('access_token_file.conf', 'w')
    access_token_input = input("Enter your access_token: ->")
    f.write(access_token_input)
    f = open('access_token_file.conf', 'r')
    print("access_token was recorded")
if command == "setup":
    setup()
try:
    f = open('access_token_file.conf', 'r')
except ValueError:
    setup()
f = open('access_token_file.conf', 'r')
access_token = f.read()
session = vk.Session(access_token=access_token)
vkapi = vk.API(session)
# print(access_token)
messages = vkapi.messages.getDialogs()
number_of_messages = messages[0]
if command == "debug":
    print("|MESSAGES|")
    for i in range(4):
        print(messages[i])
if command == "get_msg":
    print_messages(messages, number_of_messages, vkapi)
if command == "ans":
    while True:
        messages = vkapi.messages.getDialogs()
        number_of_messages = messages[0]
        ans_messages(messages,number_of_messages,vkapi)
