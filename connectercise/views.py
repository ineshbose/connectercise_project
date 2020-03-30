from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from connectercise.models import Sport, SportRequest, UserProfile
from django.db.models import F
from django.contrib.auth.models import User
from connectercise.forms import SportForm, RequestForm, UserForm, UserProfileForm, CommentForm, SportRequestForm, UserForm2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    sport_list = Sport.objects.all()[:5]
    request_list = SportRequest.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'lorem ipsum?'
    context_dict['sports'] = sport_list
    context_dict['requests'] = request_list
    return render(request, 'connectercise/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'connectercise/about.html', context=context_dict)

def activity(request):
    sport_list = Sport.objects.all()[:5]
    request_list = SportRequest.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['sports'] = sport_list
    context_dict['requests'] = request_list
    return render(request, 'connectercise/activity.html', context=context_dict)

def sports(request):
    sport_list = Sport.objects.all()[:5]
    context_dict = {}
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
        s_request = SportRequest.objects.get(slug=request_name_slug)
        SportRequest.objects.filter(slug=request_name_slug).update(views=s_request.views+1)
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
                new_comment.creator = request.user
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
                if 'picture' in request.FILES:
                    s_request.picture = request.FILES['picture']
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
            if 'picture' in request.FILES:
                    s_request.picture = request.FILES['picture']
            s_request.completed = False
            s_request.save()
            return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': s_request.sport, 'request_name_slug': s_request.request_id}))
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'connectercise/add_request.html', context=context_dict)

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

def search(request):
    query = request.GET.get('q')
    request_list = None
    if query != None:
        request_list = SportRequest.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query)) 
        return render(request, 'connectercise/search.html', {'query': query,'requests': request_list}) 
    
    return render(request, 'connectercise/search.html', {'query': query, 'requests': request_list}) 
    
@login_required
def accept_request(request, sport_name_slug, request_name_slug):
    s_request = SportRequest.objects.get(slug=request_name_slug)
    if s_request.creator != request.user:
        SportRequest.objects.filter(slug=request_name_slug).update(completed=True)
        return redirect(reverse('connectercise:show_user', kwargs={'user_profile_slug': s_request.creator.username}))
    else:
        return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': s_request.sport, 'request_name_slug': s_request.request_id}))

@login_required
def delete_request(request, sport_name_slug, request_name_slug):
    s_request = SportRequest.objects.get(slug=request_name_slug)
    if s_request.creator == request.user:
        SportRequest.objects.filter(slug=request_name_slug).delete()
        return redirect(reverse('connectercise:show_user', kwargs={'user_profile_slug': s_request.creator.username}))
    else:
        return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': s_request.sport, 'request_name_slug': s_request.request_id}))

@login_required
def user_settings(request, user_profile_slug):
    
    if user_profile_slug == request.user.username:
        user_profile = UserProfile.objects.get(user=request.user)

        if request.method == "POST":
            update_user_form = UserForm2(data=request.POST, instance=request.user)
            update_profile_form = UserProfileForm(data=request.POST, instance=user_profile)

            if update_user_form.is_valid() and update_profile_form.is_valid():
                user = update_user_form.save()
                profile = update_profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()
                return redirect(reverse('connectercise:show_user', kwargs={'user_profile_slug': user_profile_slug}))

            else:
                print(update_user_form.errors, update_profile_form.errors)
        else:
            update_user_form = UserForm2(instance=request.user)
            update_profile_form = UserProfileForm(instance=user_profile)

        return render(request,
                'connectercise/user_settings.html',
                {'update_user_form': update_user_form, 'update_profile_form': update_profile_form}
                )
    else:
        return render(request, 'connectercise/user_settings.html', {'user':None})

def privacy_policy(request):
    return render(request, 'connectercise/policy.html')

def terms_of_service(request):
    return render(request, 'connectercise/terms.html')
