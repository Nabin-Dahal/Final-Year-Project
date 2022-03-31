<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from orders.models import Order, OrderProduct
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Verification email
=======
from email.message import EmailMessage
from django.shortcuts import render, redirect,  get_object_or_404
from accounts.forms import RegistrationFrom, UserForm, UserProfileForm
from accounts.models import Account, UserProfile
from orders.models import Order, OrderProduct
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
<<<<<<< HEAD

from carts.views import _cart_id
from carts.models import Cart, CartItem
import requests


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
=======
from carts.models import CartItem, Cart
from carts.views import _cart_id
import requests



def register(request):
    if request.method =='POST':
        form  = RegistrationFrom(request.POST)
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
<<<<<<< HEAD
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # Create a user profile
            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'default/default-user.png'
            profile.save()

            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
=======
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username = username, password=password)
            user.phone_number = phone_number
            user.save()
            
            #user activation
            current_site = get_current_site(request)
            mail_subject = "Please Verify your account"
            message = render_to_string('accounts/account_verification_email.html',{
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
<<<<<<< HEAD
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address [rathan.kumar@gmail.com]. Please verify it.')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
=======
            send_email = EmailMessage(mail_subject,message, to=[to_email])
            send_email.send()
            
            
            # messages.success(request, 'Thank you for Registeration. Please verify your account with the link that we have sent you')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationFrom()
    context = {
        'form': form,    
    }
    return render(request,'accounts/register.html',context)

def login(request):
    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
<<<<<<< HEAD

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    # Getting the product variations by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    # Get the cart items from the user to access his product variations
=======
        
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id =_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart = cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    
                    product_variation =[]
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                        
                        
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
<<<<<<< HEAD

                    # product_variation = [1, 2, 3, 4, 6]
                    # ex_var_list = [4, 6, 3, 5]

=======
                        
                    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
<<<<<<< HEAD
                            item = CartItem.objects.get(id=item_id)
=======
                            item = CartItem.objects.get(id = item_id)
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
<<<<<<< HEAD
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout/
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
=======
                            cart_item = CartItem.objects.filter(cart=cart) 
                            for item in cart_item:
                                item.user = user
                                item.save()                
                
            except:
                pass
            auth.login(request, user)
            messages.success(request,'you are logged in.')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)    
            except:
                return redirect('dashboard')
        else: 
            messages.error(request, 'your email or password does not match ')
            return redirect('login')
        
        
    return render(request,'accounts/login.html')
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
<<<<<<< HEAD

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


@login_required(login_url = 'login')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()

    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/dashboard.html', context)
=======
        
    if user is not None and  default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated.")
        return redirect('login')
    else:
        messages.error(request,'Invalid activation link')
        return redirect('register')


@login_required(login_url= 'login')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    
    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,  
    }
    
    
    
    return render(request, 'accounts/dashboard.html',context)


@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html',context)

    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
<<<<<<< HEAD
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
=======
        if Account.objects.filter(email = email).exists():
            user = Account.objects.get(email__exact=email)
            
            #reset password verification
            current_site = get_current_site(request)
            mail_subject = "Reset your Password"
            message = render_to_string('accounts/reset_password_email.html',{
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
<<<<<<< HEAD
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
=======
            send_email = EmailMessage(mail_subject,message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
            
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')

<<<<<<< HEAD

=======
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
<<<<<<< HEAD

    if user is not None and default_token_generator.check_token(user, token):
=======
    
    if user is not None and  default_token_generator.check_token(user, token):
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
<<<<<<< HEAD
        messages.error(request, 'This link has been expired!')
        return redirect('login')


=======
        messages.error(request, 'this link is expired')
        return redirect('login')
    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
<<<<<<< HEAD

=======
        
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
<<<<<<< HEAD
            messages.success(request, 'Password reset successful')
            return redirect('login')
=======
            messages.success(request, 'Password changed successful')
            return redirect('login') 
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')
<<<<<<< HEAD


@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)


@login_required(login_url='login')
=======
    

@login_required(login_url='login')    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
<<<<<<< HEAD
    return render(request, 'accounts/edit_profile.html', context)
=======
    return render(request, 'accounts/edit_profile.html',context)
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
<<<<<<< HEAD

        user = Account.objects.get(username__exact=request.user.username)

=======
        user = Account.objects.get(username__exact=request.user.username)
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
<<<<<<< HEAD
                # auth.logout(request)
=======
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
                messages.success(request, 'Password updated successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Please enter valid current password')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match!')
<<<<<<< HEAD
            return redirect('change_password')
=======
            return redirect('change_password')    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
    return render(request, 'accounts/change_password.html')


@login_required(login_url='login')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
<<<<<<< HEAD
        subtotal += i.product_price * i.quantity

=======
        subtotal  += i.product_price * i.quantity
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
    context = {
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
<<<<<<< HEAD
    return render(request, 'accounts/order_detail.html', context)
=======
    return render(request, 'accounts/order_detail.html',context)

    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
