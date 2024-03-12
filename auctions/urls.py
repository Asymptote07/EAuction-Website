from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create', views.createListing, name='create'),
    path('catList', views.catList, name='catList'),
    path('item/<int:id>', views.item, name = 'item'),
    path('removeFromWatchlist/<int:id>', views.removeFromWatchlist, name = 'removeFromWatchlist'),
    path('addToWatchlist/<int:id>', views.addToWatchlist, name = 'addToWatchlist'),
    path('watchlist', views.watchlist, name = 'watchlist'),
    path('addComment/<int:id>', views.addComment, name = 'addComment'),
    path('userListings', views.userListings, name = 'userListings'),
    path('addBid/<int:id>' , views.addBid, name = 'addBid'),
    path('closeAuction/<int:id>', views.closeAuction, name = 'closeAuction'),
    path('userBids', views.userBids, name ='userBids'),
]
