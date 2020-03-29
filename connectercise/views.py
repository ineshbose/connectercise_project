from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from connectercise.models import Sport, SportRequest, UserProfile
from django.contrib.auth.models import User
from connectercise.forms import SportForm, RequestForm, UserForm, UserProfileForm, CommentForm, SportRequestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    sport_list = Sport.objects.order_by('-likes')[:5]
    request_list = SportRequest.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'lorem ipsum?'
    context_dict['sports'] = sport_list
    context_dict['requests'] = request_list
    visitor_cookie_handler(request)
    return render(request, 'connectercise/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Team Connectercise!'}
    sport_list = Sport.objects.order_by('-likes')[:5]
    context_dict['sports'] = sport_list
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'connectercise/about.html', context=context_dict)

def activity(request):
    sport_list = Sport.objects.order_by('-likes')[:5]
    request_list = SportRequest.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'lorem ipsum?'
    context_dict['sports'] = sport_list
    context_dict['requests'] = request_list
    visitor_cookie_handler(request)
    return render(request, 'connectercise/activity.html', context=context_dict)

def sports(request):
    sport_list = Sport.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'This tutorial has been put together by Team Connectercise!'}
    context_dict['sports'] = sport_list
    return render(request, 'connectercise/sports.html', context=context_dict)

def show_sport(request, sport_name_slug):
    context_dict = {}
    try:
        sport = Sport.objects.get(slug=sport_name_slug)
        requests = SportRequest.objects.filter(sport=sport)
        context_dict['requests'] = requests
        context_dict['sport'] = sport
    except Sport.DoesNotExist:
        context_dict['sport'] = None
        context_dict['requests'] = None
    return render(request, 'connectercise/sport.html', context=context_dict)

def show_request(request, sport_name_slug, request_name_slug):
    context_dict = {}
    try:
        s_request = get_object_or_404(SportRequest,slug=request_name_slug)
        context_dict['request'] = s_request
        comments = s_request.comments.filter(active=True)
        new_comment = None
        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current request to the comment
                new_comment.request = s_request
                # Save the comment to the database
                new_comment.save()
                context_dict['new_comment'] = new_comment
            else:
                comment_form = CommentForm()
                context_dict['comment_form'] = comment_form
            
            context_dict['comment_form'] = comment_form
        context_dict['comments'] = comments
    except SportRequest.DoesNotExist:
        context_dict['request'] = None
    return render(request, 'connectercise/request.html', context=context_dict)

@login_required
def add_sport(request):
    form = SportForm()
    if request.method == 'POST':
        form = SportForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'connectercise/add_sport.html', {'form': form})

@login_required
def add_sport_request(request, sport_name_slug):
    try:
        sport = Sport.objects.get(slug=sport_name_slug)
    except Sport.DoesNotExist:
        sport = None
    
    if sport is None:
        return redirect('/')
    
    form = SportRequestForm()

    if request.method == 'POST':
        form = SportRequestForm(request.POST)
        if form.is_valid():
            if sport:
                s_request = form.save(commit=False)
                s_request.sport = sport
                s_request.views = 0
                s_request.creator = request.user
                s_request.completed = False
                s_request.save()
                return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': sport_name_slug, 'request_name_slug': s_request.request_id}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'sport': sport}
    return render(request, 'connectercise/add_request.html', context=context_dict)

@login_required
def add_request(request):

    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            s_request = form.save(commit=False)
            s_request.views = 0
            s_request.creator = request.user
            s_request.completed = False
            s_request.save()
            return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': s_request.sport, 'request_name_slug': s_request.request_id}))
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'connectercise/add_request.html', context=context_dict)

@login_required
def restricted(request):
    context_dict = {}
    sport_list = Sport.objects.order_by('-likes')[:5]
    context_dict['sports'] = sport_list
    return render(request, 'connectercise/restricted.html', context=context_dict)

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits+1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits

def show_user(request, user_profile_slug):
    context_dict = {}
    try:
        user = User.objects.get(username=user_profile_slug)
        userp = UserProfile.objects.get(user=user)
        context_dict['userp'] = userp
        try:
            user_requests = SportRequest.objects.filter(creator=user)
            context_dict['requests'] = user_requests
        except SportRequest.DoesNotExist:
            context_dict['requests'] = None
    except User.DoesNotExist:
        context_dict['userp'] = None
    return render(request, 'connectercise/user.html', context=context_dict)

def accept_request(request):
    RequestForm.completed = True
    return HttpResponse('Request has been accepted')

@login_required
def user_settings(request, user_profile_slug):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            #s_request = form.save(commit=False)
            user = User.objects.get(username=user_profile_slug)
            user.first_name = form.first_name
            user.last_name = form.last_name
            userp = UserProfile.objects.get(user=user)
            userp.picture = form.picture
            #s_request.save()
            return redirect(reverse('connectercise:show_user', kwargs={'user_profile_slug': user_profile_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'connectercise/user_settings.html', context=context_dict)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'connectercise/view_profile.html', args)