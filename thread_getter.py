from fbchat.models import *
from fbchat import Client
from switchcase import switch


# will return a thread, given a client
# thread will have uid which can be used for read and write


def recent_conversations(client):
    threads = client.fetchThreadList()
    print('Who do you want to talk to: ')
    for i in range(0, len(threads) - 1):
        if threads[i].name:
            print(str(i) + ': ' + threads[i].name)
        else:
            users = threads[i].participants
            user_names = []
            for user in users:
                user_obj = client.fetchUserInfo(user)[user]
                user_names.append(user_obj.name)
            print(str(i) + ': ' + str(user_names))
    choice = input('Enter a number: ')
    if threads[int(choice)].name:
        name = threads[i].name
    else:
        users = threads[i].participants
        user_names = []
        for user in users:
            user_obj = client.fetchUserInfo(user)[user]
            user_names.append(user_obj.name)
        name = str(user_names)
    
    return [threads[int(choice)], name]


if __name__ == '__main__':
    print('imported fb_client')
