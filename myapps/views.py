from django.shortcuts import render
from django.http import JsonResponse
from .models import Products
from django.templatetags.static import static
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from .models import Users


def product_list(request):

    products = Products.objects.all()

    data = []

    for product in products:

        data.append({
            "id": product.product_id,
            "name": product.product_name,
            "description": product.description,
            "price": float(product.price),
            "brand": product.brand,
            "image": product.image_url.url
            if product.image_url
            else "",
            "category": product.category.category_name if product.category else ""
        })

    return JsonResponse(data, safe=False)


def shop(request):
    return render(request, 'ecomm.html')
def register(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check passwords
        if password != confirm_password:

            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check existing email
        if Users.objects.filter(email=email).exists():

            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create user
        Users.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=make_password(password),
            role='Customer'
        )

        messages.success(
            request,
            "Registration successful. Please login."
        )

        return redirect('login')

    return render(request, 'register.html')
def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user = Users.objects.get(email=email)

        except Users.DoesNotExist:

            messages.error(request, "Invalid email or password.")
            return redirect('login')

        if check_password(password, user.password):

            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.name

            return redirect('shop')

        else:

            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')
def logout_view(request):

    request.session.flush()

    return redirect('shop')