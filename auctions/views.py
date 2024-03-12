from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import date

from .models import User,Listings,Category,Comment,Bid



###############################################
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


###############################################
    
def index(request):
    return render(request, "auctions/index.html", {
        'list' : Listings.objects.filter(isActive = True),
        'categories' : Category.objects.all()
    })
    
def catList(request):
    if request.method == 'POST':
        cat = Category.objects.get(pk = int(request.POST['category']))
        return render(request, 'auctions/catList.html', {
            'list' : Listings.objects.filter(isActive = True, category = cat),
            'cat' : cat
        })

def createListing(request):
    if request.method == 'GET':
        return render(request, 'auctions/create.html', {
            'categories' : Category.objects.all()
        })
    else:
        title = request.POST['title']
        desc = request.POST['description']
        price = request.POST['price']
        cuser = request.user

        today = date.today()
        time = today.strftime("%B %d, %Y")
        bid = Bid(bid = price, user = cuser, time = time)
        bid.save()
        
        url = request.POST['imgurl']
        cat = Category.objects.get(pk = int(request.POST['category']))
        
        item = Listings(
            title = title,
            description = desc,
            price = bid,
            imgurl = url,
            category = cat,
            owner = cuser,
            time = time
        )
        item.save()
        return HttpResponseRedirect(reverse('index'))
    
def item(request,id):
    listing = Listings.objects.get(pk = id)
    u = request.user
    inwatch = u in listing.watchlist.all()
    comments = Comment.objects.filter(listing = listing)
    return render(request, 'auctions/items.html', {
        'listing' : listing,
        'inwatch' : inwatch,
        'comments' : comments
    }) 

def removeFromWatchlist(request,id):
    listing = Listings.objects.get(pk = id)
    u = request.user
    listing.watchlist.remove(u)
    return HttpResponseRedirect(reverse('item', args=(id, )))

def addToWatchlist(request,id):
    listing = Listings.objects.get(pk = id)
    u = request.user
    listing.watchlist.add(u)
    return HttpResponseRedirect(reverse('item', args=(id, )))

def watchlist(request):
    u = request.user
    return render(request, 'auctions/watchlist.html', {
        'list' :  u.user_watchlist.all()
    })

def addComment(request, id):
    u = request.user
    listing = Listings.objects.get(pk = id)
    today = date.today()
    time = today.strftime("%B %d, %Y")
    newcomment = Comment(
        author = u,
        listing = listing,
        message = request.POST['message'],
        time = time
    )
    newcomment.save()
    return HttpResponseRedirect(reverse('item', args=(id, )))


def userListings(request):
    u = request.user
    list = u.user_listing.all()
    return render(request, 'auctions/userListings.html',{
        'list' : list
    })

def addBid(request,id):
    u = request.user
    listing = Listings.objects.get(pk = id)
    bid = float(request.POST['bid'])
    inwatch = u in listing.watchlist.all()
    comments = Comment.objects.filter(listing = listing)
    if bid > listing.price.bid:
        today = date.today()
        time = today.strftime("%B %d, %Y")
        newbid = Bid(bid = bid, user = u, time = time)
        newbid.save()
        listing.price = newbid
        listing.save()
        return render(request, 'auctions/items.html', {
            'listing' : listing,
            'inwatch' : inwatch,
            'comments' : comments,
            'update' : True,
            'message' : 'Bid placed successfully!'
        })
    else:
        return render(request, 'auctions/items.html', {
            'listing' : listing,
            'inwatch' : inwatch,
            'comments' : comments,
            'update' : False,
            'message' : 'Bidding price should be greater than the current price!!'
        })
    
def closeAuction(request, id):
    listing = Listings.objects.get(pk = id)
    listing.isActive = False
    listing.save()
    inwatch = request.user in listing.watchlist.all()
    comments = Comment.objects.filter(listing = listing)
    return render(request, 'auctions/items.html', {
            'listing' : listing,
            'inwatch' : inwatch,
            'comments' : comments,
            'update' : True,
            'message' : 'You have closed the Auction'
        })

def userBids(request):
    u = request.user
    list = Listings.objects.filter(price__user = u)
    return render(request, 'auctions/userBids.html',{
        'list' : list
    })