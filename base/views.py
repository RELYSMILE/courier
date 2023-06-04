from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from random import randint
from .models import UserProfile, Header,Signupbanner,SouthAfricaupdate,ShipmentDetails,ShipperDetails,receiverDetails,BannerPictures
from django.utils.translation import activate, gettext_lazy as _
from django.conf import settings




#login logics
def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    # getting input from user
    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist!.")
        user = authenticate(request, username=username, password = password)

        if username =='richie@britishemirate.com':
            login(request, user)
            return redirect('generate_tracking')
        

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect password or username!.")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

# logout logics
def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['firstname']
        middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['Confirmpassword']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')  # Redirect to the registration page
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')  # Redirect to the registration page


        # Create the user
        user = User.objects.create_user(username=email, password=password)
        user.first_name = first_name
        user.email = email
        user.last_name = last_name
        user.save()

        # # Create user profile
        profile = UserProfile(user=user, middle_name=middle_name, phone=phone)
        profile.save()
        # Redirect to a success page or login page
        return redirect('login')
    # If the request method is GET, render the registration form
    return render(request, 'base/login_register.html')


#index logics
def home(request):
    users = User.objects.all()
    headers = Header.objects.latest('updated')
    signupbanners =Signupbanner.objects.latest('updated')
    southafrican =SouthAfricaupdate.objects.latest('updated')
    bannerimages =BannerPictures.objects.latest('updated')

    if request.method == 'POST':
        tracking_number = request.POST.get('delivery')
        try:
            shipment = ShipmentDetails.objects.get(tracking_number=tracking_number)
            shippers = ShipperDetails.objects.filter(shipmentDetails=shipment)
            receivers = receiverDetails.objects.filter(shipmentDetails=shipment)
            # Render the template with shipment, shippers, and receivers details
            return render(request, 'base/tracking_view_component.html', {'shipment': shipment, 'shippers': shippers, 'receivers': receivers})
        except ShipmentDetails.DoesNotExist:
            messages.error(request, 'Invalid Tracking Number')
            return redirect('home')
        

    context = {
        'users': users, 
        'headers': headers,
        'signupbanners': signupbanners,
        'southafrican': southafrican,
        'bannerimages': bannerimages,
        }
    return render(request, 'base/index.html', context)

def generate_tracking(request):
    tracking_num = randint(0,5)
    tracking_num1 = randint(6,11)
    a = str(randint(15,500))

    if tracking_num == 0:
        trackingNumber1 = 'BZ2-2324'+a
    elif tracking_num == 1:
         trackingNumber1 = 'XAZ-0071'+a
    elif tracking_num == 2:
         trackingNumber1 = 'HJK-5631'+a
    elif tracking_num == 3:
         trackingNumber1 = 'XIL-5091'+a
    elif tracking_num == 4:
         trackingNumber1 = 'WQT-6668'+a
    else:
         trackingNumber1 = 'OUR-3852'+a


    if tracking_num1 == 6:
        trackingNumber2 = 'B22C-'+a
    elif tracking_num1 == 7:
         trackingNumber2 = '9GT4-'+a
    elif tracking_num1 == 8:
         trackingNumber2 = 'MXV2-'+a
    elif tracking_num1 == 9:
         trackingNumber2 = '10VM-'+a
    elif tracking_num1 == 10:
         trackingNumber2 = 'GJ9X-'+a
    else:
         trackingNumber2 = 'RW45-'+a

    context = {
        'trackingNumber1': trackingNumber1,
        'trackingNumber2': trackingNumber2,
        }
    return render(request, 'base/generate_tracking.html', context)


# views.py


def set_language(request):
    if request.method == 'POST':
        language_code = request.POST.get('language')
        if language_code:
            activate(language_code)
            request.session[settings.LANGUAGE_SESSION_KEY] = language_code
    
    # Redirect back to the referring page or a default page
    return redirect(request.META.get('HTTP_REFERER') or '/')
