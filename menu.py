from switchcase import switch

import time
import thread_getter


# i want menu to be given a client and then return a thread, including type
# do this by navigating menu and calling a different module

# returns which search method will be using
def start_menu():
    time.sleep(2)
    print('Select from: ')
    options = ['Recent Conversations', 'Search User by name',
               'Search Group by name', 'Find User by UID', 'Find Group by UID']
    for i in range(0, len(options)):
        print(str(i) + ': ' + options[i])
    choice = input('Enter a number: ')
    return int(choice)


# given search method, returns user/group
def get_thread(x, client):
    for case in switch(x):
        if case(0):
            print('recent')
            return thread_getter.recent_conversations(client=client)
        if case(1):
            print('user name')
            user = input('Say user name: ')
            return thread_getter.search_for_user(client=client, name=user)
        if case(2):
            print('group name')
            group = input('Say group name: ')
            return thread_getter.search_for_group(client=client, group=group)
        if case(3):
            print('user uid')
            uid = input('Enter user UID: ')
            return thread_getter.get_user_by_uid(client=client, uid=uid)
        if case(4):
            print('group uid')
            uid = input('Enter group UID: ')
            return thread_getter.get_group_by_uid(client=client, uid=uid)