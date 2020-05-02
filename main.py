from fbchat.models import *
from fbchat import Client

import thread_getter
from sys import platform, argv
from os import system


def login():
    username = input('enter username: ')
    password = input('enter password: ')
    return Client(username, password)


# going to be clearing the cmd on updates, so need a quick way on both os
if platform == "win32":
    clear = lambda: system('cls')
else:
    clear = lambda: system('clear')

# login details as args, can do better later
# prompt if argv[1] is empty
# use flags for more modes etc
if len(argv) > 1:
    client = Client(argv[1], argv[2])
else:
    client = login()

# this will return a thread by doing the search type specified in x
thread = thread_getter.recent_conversations(client=client)
client.logout()


def send_message(thread, thread_type):
    message = input('Message: ')
    client.send(message=Message(text=message), thread_id=thread.uid, thread_type=thread_type)

# Gets the last 10 messages sent to the thread
# messages = client.fetchThreadMessages(thread_id="<thread id>", limit=10)
# Since the message come in reversed order, reverse them
# messages.reverse()
