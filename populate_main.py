import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectercise_project.settings')

import django
django.setup()
from main.models import UserProfile, SportingRequest
from django.contrib.auth.models import User
from django.utils import timezone
import string
import datetime
import os
import sys
import random

def populate():
    users = [{'username': 'alemon1', 
                        'password': 'password',
                        'email': 'alemon1@connectercise.com',
                        'sport':'tennis',
                        'location': 'glasgow',
                        'socialMedia':'user1@strava'},
                    {'username': 'aapple1', 
                        'password': 'password',
                        'email': 'aapple1@connectercise.com',
                        'sport':'swimming',
                        'location': 'glasgow',
                        'socialMedia':'user2@strava'},
                    {'username': 'apeach1', 
                        'password': 'password',
                        'email': 'apeach1@connectercise.com',
                        'sport':'running',
                        'location': 'glasgow',
                        'socialMedia':'user3@strava'},
                    {'username': 'acitrus1', 
                        'password': 'password',
                        'email': 'acitrus1@connectercise.com',
                        'sport':'running',
                        'location': 'glasgow',
                        'socialMedia':'user4@strava'},
                    {'username': 'aapple2', 
                        'password': 'password',
                        'email': 'aapple2@connectercise.com',
                        'sport':'swimming',
                        'location': 'edinburgh',
                        'socialMedia':'user5@strava'},
                    {'username': 'apeach2', 
                        'password': 'password',
                        'email': 'apeach2@connectercise.com',
                        'sport':'running',
                        'location': 'edinburgh',
                        'socialMedia':'user6@strava'},
                    {'username': 'acitrus2', 
                        'password': 'password',
                        'email': 'acitrus2@connectercise.com',
                        'sport':'running',
                        'location': 'edinburgh',
                        'socialMedia':'user7@strava'},
                        {'username': 'aapple3', 
                        'password': 'password',
                        'email': 'aapple3@connectercise.com',
                        'sport':'swimming',
                        'location': 'edinburgh',
                        'socialMedia':'user8@strava'},
                    {'username': 'apeach3', 
                        'password': 'password',
                        'email': 'apeach3@connectercise.com',
                        'sport':'running',
                        'location': 'edinburgh',
                        'socialMedia':'user9@strava'},
                    {'username': 'acitrus3', 
                        'password': 'password',
                        'email': 'acitrus3@connectercise.com',
                        'sport':'running',
                        'location': 'edinburgh',
                        'socialMedia':'user10@strava'},]

    requests = [{'time': timezone.now(),
                'location': 'glasgow',
                'sessionID': '1',
                'sport':'hiking'},
                {'time': timezone.now(),
                'location': 'edinburgh',
                'sessionID': '2',
                'sport':'swimming'},
                {'time': timezone.now(),
                'location': 'glasgow',
                'sessionID': '3',
                'sport':'hiking'},
                {'time': timezone.now(),
                'location': 'edinburgh',
                'sessionID': '4',
                'sport':'swimming'},
                {'time': timezone.now(),
                'location': 'glasgow',
                'sessionID': '5',
                'sport':'hiking'},
                {'time': timezone.now(),
                'location': 'edinburgh',
                'sessionID': '6',
                'sport':'swimming'},
                {'time': timezone.now(),
                'location': 'glasgow',
                'sessionID': '7',
                'sport':'hiking'},
                {'time': timezone.now(),
                'location': 'edinburgh',
                'sessionID': '8',
                'sport':'swimming'},
                ]

    for req in requests:
        r = add_request(req['time'], req['location'], req['sessionID'], req['sport'])
    
    for r in SportingRequest.objects.all():
        print(f'-{r}')

def add_request(time, location, sessionID, sport):
    r = SportingRequest.objects.get_or_create(time=time, location=location, sessionID=sessionID, sport=sport)[0]
    r.save()
    return r

def get_random_string(length, stringset=string.ascii_letters):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])

def get_random_name(case):
    if case == "first":
        fnames = ['Marc','Martin','Marvin','Peter','Angela','Clive','Megan','Fiona','Sky','Randy','Miranda','Gemma','Andrew']
        return random.choice(fnames)
    if case == "last":
        lnames = ['Smith','Doe','Murphy','Jacobs','Steinwien','Galoppa']
        return random.choice(lnames)

def get_random_sport():
    sports = ['Tennis', 'Cycling', 'Running', 'Hiking', 'Football', 'Boxing', 'Climbing', 'Skiing', 'Walking', 'Darts']
    return random.choice(sports)

def get_random_location():
    locations = ['Glasgow', 'Edinburgh', 'Aberdeen', 'Dumfries', 'St. Andrews', 'Dunbarr']
    return random.choice(locations)

def generate_users(n):    
    print("Generating %s user(s)..." % n)
    print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("#", "username", "firstname", "lastname", "title", "company", "work_email"))

    for user_index in range(n):
        # create user
        name = get_random_name("first")
        new_user = User.objects.create(
            first_name=name,
            username="{0}{1}".format(name,get_random_string(4)),
            last_name=get_random_name("last"),
        )
        new_user.save()

        # create profile for user
        p = UserProfile.objects.create(user=new_user)
        p.pageURL = "www.%s.com" % new_user.username
        p.email = "%s@random.com" % new_user.username
        p.sport = get_random_sport()
        p.socialMedia = "%s@strava.com" % new_user.username
        p.location = get_random_location()
        p.save()

        print("'{0}'\t'{1}'\t'{2}'\t'{3}'\t'{4}'\t'{5}'\t'{6}'\t'{7}'\t'{8}'".format(str(user_index+1),new_user.username, new_user.first_name, new_user.last_name,str(p.pageURL),p.email,p.sport,p.socialMedia,p.location))

        print("")

if __name__ == '__main__':
    print('Starting Main population script...')
    populate()
    generate_users(10)