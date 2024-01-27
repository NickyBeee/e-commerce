from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import datetime
from django.contrib.auth.decorators import login_required

from .models import User, listing, bid, comment, watchlist, winner


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        if not username:
            return render(request,"auction/register.html",{
                "message":"Please enter your username.",
                "msg_type":"danger"
            })
        if not email:
            return render(request,"auction/register.html",{
                "message":"Please enter your email.",
                "msg_type":"danger"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

@login_required(login_url='/login')
def activelisting(request):
    products = listing.objects.all()
    empty = False
    if len(products) == 0:
        empty = True
    return render(request,"auctions/activelisting.html",{
            "products":products,
            "empty":empty})


@login_required(login_url='/login')
def closedlisting(request):
    winners = winner.objects.all()
    empty = False
    if len(winners) == 0 :
        empty = True
    return render(request,"auctions/closedlisting.html",{
        "products" : winners,
        "empty" : empty
    })

@login_required(login_url='/login')
def createlisting(request):
    if request.method == "POST":

        item = listing()

        item.seller = request.user.username
        item.title = request.POST.get('title')
        item.listingid = request.POST.get('listingid')
        item.description = request.POST.get('description')
        item.category = request.POST.get('category')
        item.start = request.POST.get('start')

        if request.POST.get('image_link'):
            item.image_link = request.POST.get('image_link')
        else:
            item.image_link = "https://pbs.twimg.com/media/GEaNr3rWAAARAIq?format=jpg&name=medium"

        item.save()

        products = listing.objects.all()
        empty = False
        if len(products) == 0:
            empty = True
        return render(request, "activelisting.html",{
            "products": products,
            "empty": empty
        })
    else:
        return render(request, "auctions/createlisting.html")



def listing_active(request):
    return render(request,'listing_active.html')

def watchlist(request):
    return render(request,'watchlist.html')

def categories(request):
    return render(request,'categories.html')

def category(request,category):
    return render(request,'category.html',{'category':category})


def listing_detail(request,listing_id):
    listing = get_object_or_404(listing, listingid = listing_id)

    return render(request,'listing_detail.html',{'listing':listing})
