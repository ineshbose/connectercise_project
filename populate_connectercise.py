import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectercise_project.settings')

import django
django.setup()
from connectercise.models import Sport, SportRequest

def populate():
    hike_requests = [
        {'title': 'HIKING BUDDY NEEDED!!',
        'url': 'https://inesh.xyz/'},
        {'title': 'A Hike Across The Country',
        'url': 'https://inesh.xyz/'},
        {'title': 'The Highland Hike',
        'url': 'https://inesh.xyz/'},
    ]

    cycling_requests = [
        {'title': 'Looking to start a club!',
        'url': 'https://inesh.xyz/'},
        {'title': 'Glasgow - Dumfries Ride',
        'url': 'https://inesh.xyz/'},
        {'title': 'Edinburgh Cyclothon Buddies?',
        'url': 'https://inesh.xyz/'},
    ]

    other_requests = [
        {'title': 'Online Chess?',
        'url': 'https://inesh.xyz/'},
        {'title': 'C***fighting!!! ^_^ ',
        'url': 'https://inesh.xyz/'},
    ]

    sports = {'Hiking': {'requests': hike_requests, 'views': 128, 'likes': 64},
            'Cycling': {'requests': cycling_requests, 'views': 64, 'likes': 32},
            'Others': {'requests': other_requests, 'views': 32, 'likes': 16} }

    for sport, sport_data in sports.items():
        s = add_sport(sport, sport_data['views'], sport_data['likes'])
        for r in sport_data['requests']:
            add_request(s, r['title'], r['url'])
    
    for s in Sport.objects.all():
        for r in SportRequest.objects.filter(sport=s):
            print(f'- {s}: {r}')

def add_request(sport, title, url, views=0):
    r = SportRequest.objects.get_or_create(sport=sport, title=title)[0]
    r.url = url
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