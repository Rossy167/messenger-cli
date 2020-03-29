from fbchat.models import *
from fbchat import Client
from switchcase import switch


# will return a thread, given a client
# thread will have uid which can be used for read and write


def recent_conversations(client):
    threads = client.fetchThreadList()
    print('Who do you want to talk to: ')
    for i in range(0, len(threads)):
        print(str(i) + ': ' + threads[i].name)
    choice = input('Enter a number: ')
    return [threads[int(choice)], threads[int(choice)].type]


def search_for_user(client, name):
    threads = client.searchForUsers(name)
    for i in range(0, len(threads)):
        try:
            print(str(i) + ': ' + threads[i].name)
        except:
            print('uwu i did a fucky')
    choice = input('Enter a number: ')
    return [threads[int(choice)], threads[int(choice)].type]


def search_for_group(client, group):
    threads = client.searchForGroups(group)
    for i in range(0, len(threads)):
        print(str(i) + ': ' + threads[i].name)
    choice = input('Enter a number: ')
    return [threads[int(choice)], threads[int(choice)].type]


def get_group_by_uid(client, uid):
    thread = []
    try:
        thread = client.fetchThreadInfo(uid)[uid]
    except:
        print('thread not found/not valid')
    return [thread, ThreadType.GROUP]


def get_user_by_uid(client, uid):
    thread = []
    try:
        thread = client.fetchUserInfo(uid)[uid]
    except:
        print('user not found/not valid')
    return [thread, ThreadType.USER]


if __name__ == '__main__':
    print('imported fb_client')
