from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Donation, CommitteeMember
from .forms import DonationForm, ContactForm, UserRegisterForm

def home(request):
    recent_posts = Post.objects.order_by('-created_at')[:6]
    committee = CommitteeMember.objects.all()
    return render(request, 'main/home.html', {'posts': recent_posts, 'committee': committee})

def gallery(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'main/gallery.html', {'posts': posts})

def donation_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your generous donation!')
            return redirect('donations')
    else:
        form = DonationForm()
    
    donors = Donation.objects.filter(is_approved=True).order_by('-date')
    return render(request, 'main/donations.html', {'form': form, 'donors': donors})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

from .models import Post, Donation, CommitteeMember, UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile_image = form.cleaned_data.get('profile_image')
            UserProfile.objects.create(user=user, profile_image=profile_image)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

@login_required
def dashboard(request):
    profile_image_url = None
    try:
        if request.user.userprofile and request.user.userprofile.profile_image:
            profile_image_url = request.user.userprofile.profile_image.url
    except Exception:
        pass
    
    return render(request, 'main/dashboard.html', {'profile_image_url': profile_image_url})
