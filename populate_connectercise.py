import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectercise_project.settings')

import django
django.setup()
from connectercise.models import Sport, SportRequest, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import random

def populate():
    dummy_users = [
        {'username': 'testusername1',
        'password': 'connectercise1',
        'email': 'testuser1@connectercise.com'},
        {'username': 'testusername2',
        'password': 'connectercise2',
        'email': 'testuser2@connectercise.com'},
        {'username': 'testusername3',
        'password': 'connectercise3',
        'email': 'testuser3@connectercise.com'},
        {'username': 'testusername4',
        'password': 'connectercise4',
        'email': 'testuser4@connectercise.com'},
    ]

    hike_requests = [
        {'title': 'HIKING BUDDY NEEDED!!',
        'desc': 'I am going on a hike. Join me',
        'views': 128},
        {'title': 'A Hike Across The Country',
        'desc': 'Lets travel the country :)',
        'views': 64},
        {'title': 'The Highland Hike',
        'desc': 'Going up north',
        'views': 32},
    ]

    cycling_requests = [
        {'title': 'Looking to start a club!',
        'desc': 'Based in Glasgow West End',
        'views': 64},
        {'title': 'Glasgow - Dumfries Ride',
        'desc': '200km ride, anyone?',
        'views': 32},
        {'title': 'Edinburgh Cyclothon Buddies?',
        'desc': 'Pres at my place lol',
        'views': 16},
    ]

    other_requests = [
        {'title': 'Online Chess?',
        'desc': 'fast af boi',
        'views': 32},
        {'title': 'C***fighting!!! ^_^ ',
        'desc': 'winner takes all',
        'views': 16},
    ]

    sports = {'Hiking': {'requests': hike_requests, 'picture': 'sports/hiking.jpg'},
            'Cycling': {'requests': cycling_requests, 'picture': 'sports/cycling.jpg'},
            'Others': {'requests': other_requests, 'picture': 'sports/default.jpg'} }

    user_list = []
    for u in dummy_users:
        up = add_user(u['username'],u['password'],u['email'])
        user_list.append(up)
        print(f'- Added user {up}')

    for sport, sport_data in sports.items():
        s = add_sport(sport, sport_data['picture'])
        for r in sport_data['requests']:
            add_request(s, r['title'], r['desc'], user_list[random.randint(0,3)], r['views'])

    for s in Sport.objects.all():
        for r in SportRequest.objects.filter(sport=s):
            print(f'- {s}: {r}')

def get_random_name(case):
    if case == "first":
        fnames = ['Marc','Martin','Marvin','Peter','Angela','Clive','Megan','Fiona','Sky','Randy','Miranda','Gemma','Andrew']
        return random.choice(fnames)
    if case == "last":
        lnames = ['Smith','Doe','Murphy','Jacobs','Steinwien','Galoppa']
        return random.choice(lnames)

def add_request(sport, title, desc, creator, views=0):
    r = SportRequest.objects.get_or_create(sport=sport, title=title, creator=creator, desc=desc, views=views)[0]
    return r

def add_sport(name, picture):
    s = Sport.objects.get_or_create(name=name, picture=picture)[0]
    s.save()
    return s

def add_user(username, password, email):
    user_to_add = User(username=username, email=email, password=make_password(password), first_name=get_random_name("first"), last_name=get_random_name("last"))
    user_to_add.save()
    up = UserProfile.objects.get_or_create(user=user_to_add)[0]
    up.save()
    return user_to_add

if __name__ == '__main__':
    print('Starting Connectercise population script...')
    populate()
