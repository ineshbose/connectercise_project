import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectercise_project.settings')

import django
django.setup()
from connectercise.models import Sport, SportRequest

def populate():
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

    sports = {'Hiking': {'requests': hike_requests, 'views': 128, 'likes': 64},
            'Cycling': {'requests': cycling_requests, 'views': 64, 'likes': 32},
            'Others': {'requests': other_requests, 'views': 32, 'likes': 16} }

    for sport, sport_data in sports.items():
        s = add_sport(sport, sport_data['views'], sport_data['likes'])
        for r in sport_data['requests']:
            add_request(s, r['title'], r['desc'], r['views'])
    
    for s in Sport.objects.all():
        for r in SportRequest.objects.filter(sport=s):
            print(f'- {s}: {r}')

def add_request(sport, title, desc, views=0):
    r = SportRequest.objects.get_or_create(sport=sport, title=title)[0]
    r.desc = desc
    r.views = views
    r.save()
    return r

def add_sport(name, views=0, likes=0):
    s = Sport.objects.get_or_create(name=name, views=views, likes=likes)[0]
    s.save()
    return s

if __name__ == '__main__':
    print('Starting Connectercise population script...')
    populate()
