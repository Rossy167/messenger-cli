try:
    from fbchat.models import *
    from fbchat import Client
    import thread_getter
    from sys import platform, argv
    from os import system
except ImportError:
    print('')
    print('Cannot import the modules required for messenger-cli')
    print('Did you run the setup script?')
    print('If so... did you activate the venv before running')
    print('You can run from start.sh or start.ps1 or you can activate the venv at __projectdir__/messenger-cli/messenger_environment')
    print('')
    quit()


def login():
    username = input('enter username: ')
    password = input('enter password: ')
    return Client(username, password)


def print_thread(name, thread):
    messages = client.fetchThreadMessages(thread_id=thread.uid, limit=20)
    messages.reverse()
    clear()
    print(name + ': ')
    for message in messages:
        author = client.fetchUserInfo(message.author)[message.author]
        if message.text != '':
            print(author.name + ': ' + message.text)
        else:
            print(author.name + ' sent an image/attachment')


def send_message(thread, user_message, thread_type):
    client.send(Message(text=user_message), thread_id=thread.uid, thread_type=thread_type)


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
clear()
thread = thread_getter.recent_conversations(client=client)
name = thread[1]
thread = thread[0]

while True:
    print_thread(name, thread)
    print('Enter Message:')
    print('(or type !Q to quit)')
    message = input()
    if message == '!Q':
        client.logout()
        quit()
    else:
        send_message(thread, message, thread.type)



# thread_type=thread_type

# Gets the last 10 messages sent to the thread
# messages = client.fetchThreadMessages(thread_id="<thread id>", limit=10)
# Since the message come in reversed order, reverse them
# messages.reverse()
