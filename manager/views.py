from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import *
def login(request):
    if request.method == "POST":
        print(request.POST.get('email'), request.POST.get('password'))
        user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            auth.login(request, user)
            # Redirect to the next page if available, otherwise go to home
            next_page = 'home'
            return redirect(next_page)
        else:
            return render(request, 'manager/login.html', {'error': 'Username or password is incorrect'})
    else:
        # Check if user is already logged in, if so, redirect to home
        if request.user.is_authenticated:
            return redirect('home')
        # Store the next page in session for cases when login happens through other actions
        request.session['next'] = request.GET.get('next', '')
        return render(request, 'manager/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')
    else:
        return render(request, 'manager/login.html')

@login_required(login_url='login')
def home(request):
    clients = Client.objects.all().order_by('name')
    return render(request, 'manager/home.html', {"clients":clients})


@login_required(login_url='login')
def create_client(request):
    if request.method == "POST":
        name = request.POST.get("name")  # Get client name
        images = request.FILES.getlist("images")  # Get multiple uploaded images
        category = request.POST.get('category')

        if name:
            try:
                with transaction.atomic():  # Start atomic transaction
                    client = Client.objects.create(name=name, category=category)  # Create client

                    # Create client images
                    for img in images:
                        ClientImage.objects.create(client=client, image=img)

                return redirect("home")  # Redirect only if everything succeeds

            except Exception as e:
                print(f"Error: {e}")  # Log the error
                # Optionally, display an error message on the page
                return render(request, "manager/create_client.html",
                              {"error": "Error creating client. Please try again."})

    return render(request, "manager/create_client.html")

@login_required(login_url='login')
def client_details(request, id):
    try:
        client = get_object_or_404(Client, pk=id)
        client_images  = ClientImage.objects.filter(client=client)
        return render(request, 'manager/client_details.html',{"client_images":client_images,"client":client})
    except Exception as e:
        return render(request, 'manager/client_details.html', {"error":str(e)})



def add_images(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == "POST":
        images = request.FILES.getlist("images")
        if images:
            for img in images:
                ClientImage.objects.create(client=client, image=img)
            messages.success(request, "Images added successfully.")
    return redirect("client-details", id=id)

# Delete Images View
@csrf_exempt
def delete_images(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == "POST":
        image_ids = request.POST.getlist("image_ids")
        if image_ids:
            ClientImage.objects.filter(id__in=image_ids, client=client).delete()
            messages.success(request, "Selected images deleted.")
    return redirect("client-details", id=id)

# Delete Client View
def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    with transaction.atomic():
        client.delete()
        messages.success(request, "Client deleted successfully.")
    return redirect("home")