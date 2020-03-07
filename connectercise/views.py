from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from connectercise.models import Sport, SportRequest
from connectercise.forms import SportForm, RequestForm, UserForm, UserProfileForm
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
    return render(request, 'connectercise/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Team Connectercise!'}
    return render(request, 'connectercise/about.html', context=context_dict)

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
def add_request(request, sport_name_slug):
    try:
        sport = Sport.objects.get(slug=sport_name_slug)
    except Sport.DoesNotExist:
        sport = None
    
    if sport is None:
        return redirect('/')
    
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            if sport:
                s_request = form.save(commit=False)
                s_request.sport = sport
                s_request.views = 0
                s_request.save()
                return redirect(reverse('connectercise:show_sport', kwargs={'sport_name_slug': sport_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'sport': sport}
    return render(request, 'connectercise/add_request.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'connectercise/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('connectercise:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'connectercise/login.html')

@login_required
def restricted(request):
    return render(request, 'connectercise/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('connectercise:index'))

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