from fbchat.models import *
from fbchat import Client
from switchcase import switch

import menu
from sys import platform, argv
from os import system

# going to be clearing the cmd on updates, so need a quick way on both os
if platform == "win32":
    clear = lambda: system('cls')
else:
    clear = lambda: system('clear')

# login details as args, can do better later
# prompt if argv[1] is empty
# use flags for more modes etc
client = Client(argv[1], argv[2])

# this will return the type of search we are doing
x = menu.start_menu()

# this will return a thread by doing the search type specified in x
thread = menu.get_thread(x, client)

# welcome to the infinite loop which will be chatting in the thread found in get_thread
response = None
while True:
    if response != '-quit':
        response = input('Response: ')
        # probably something along the lines of clear the cmd and then print 10 recent messages
        # if user says -update then update without taking any action
        # also update on every action
        # where update is refresh messages output by clearing cmd and posting 10 recent messages
        print('the code')
    else:
        break

client.logout()


def send_message(thread, thread_type):
    message = input('Message: ')
    client.send(message=Message(text=message), thread_id=thread.uid, thread_type=thread_type)

# Gets the last 10 messages sent to the thread
# messages = client.fetchThreadMessages(thread_id="<thread id>", limit=10)
# Since the message come in reversed order, reverse them
# messages.reverse()
