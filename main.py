from fbchat.models import *
from fbchat import Client
from switchcase import switch
import time

# do this as ARGS
client = Client('<email>', '<password>')


def message_from_list_dump():
    threads = client.fetchThreadList()
    print('Who do you want to message:')
    for i in range(0, len(threads)):
        print(str(i) + ': ' + threads[i].name)
    choice = input('Enter a number: ')
    return threads[int(choice)]


def send_message(thread):
    message = input('Message:' )
    client.send(message=Message(text=message), thread_id=thread.uid, thread_type=ThreadType.USER)


def user_menu():
    time.sleep(2)
    options = ['Recent Conversations', 'Search User by name', 'Search Group by name',
               'Find User by UID', 'Find Group by UID']
    for i in range(0, len(options)):
        print(str(i) + ': ' + options[i])
    choice = input('Enter a number: ')
    return user_menu_switch(int(choice))


def user_menu_switch(x):
    for case in switch(x):
        if case(0):
            thread = message_from_list_dump()
            break
        if case(1):
            print("x was 1")
            break
        else:
            print("x was unmatched")
    return thread


def message_menu(thread):
    time.sleep(1)
    options = ['Send message', 'etc']
    print('What do you want to do with ' + thread.name)
    for i in range(0, len(options)):
        print(str(i) + ': ' + options[i])
    choice = input('Enter a number: ')
    message_menu_switch(int(choice), thread)


def message_menu_switch(x, thread):
    for case in switch(x):
        if case(0):
            send_message(thread)


thread = user_menu()
message_menu(thread)
client.logout()

# Gets the last 10 messages sent to the thread
# messages = client.fetchThreadMessages(thread_id="<thread id>", limit=10)
# Since the message come in reversed order, reverse them
#mmessages.reverse()
