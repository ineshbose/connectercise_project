import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectercise_project.settings')

import django
django.setup()
from main.models import UserProfile, SportingRequest
from django.utils import timezone

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

    for user in users:
        u = add_user(user['username'],user['password'],user['email'],user['sport'],user['location'],user['socialMedia'])

    for u in UserProfile.objects.all():
        print(f'-{u}')

    for req in requests:
        r = add_request(req['time'], req['location'], req['sessionID'], req['sport'])
    
    for r in SportingRequest.objects.all():
        print(f'-{r}')

def add_user(username,password,email,sport,location,socialMedia, pageURL='www.connectercise.com/'):
    u = UserProfile.objects.get_or_create(username=username,password=password,email=email,pageURL=pageURL, sport=sport,location=location,socialMedia=socialMedia) [0]
    u.save()
    return u

def add_request(time, location, sessionID, sport):
    r = SportingRequest.objects.get_or_create(time=time, location=location, sessionID=sessionID, sport=sport)[0]
    r.save()
    return r

if __name__ == '__main__':
    print('Starting Main population script...')
    populate()