from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length = 64)

    def __str__(self) :
        return f"{self.categoryName}"

class Bid(models.Model):
    bid = models.FloatField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'user_bid')
    time = models.CharField(max_length = 20, default = '10 February, 2024')
    
    def __str__(self) :
        return f'{self.bid} by {self.user}'

class Listings(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 600)
    imgurl = models.CharField(max_length = 1090)
    price = models.ForeignKey(Bid, on_delete = models.CASCADE, blank = True, null = True, related_name = 'bid_listing')
    isActive = models.BooleanField(default = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'user_listing')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = True, null = True, related_name = 'item')
    watchlist = models.ManyToManyField(User, blank = True, null = True, related_name= 'user_watchlist')
    time = models.CharField(max_length = 20, default = '10 February, 2024')
    def __str__(self):
        return f"{self.title} || {self.category}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'user_comment')
    listing = models.ForeignKey(Listings,  on_delete = models.CASCADE, blank = True, null = True, related_name = 'listing_comment')
    message = models.CharField(max_length = 300)
    time = models.CharField(max_length = 20, default = '10 February, 2024')

    def __str__(self) :
        return f"{self.author}'s comment on {self.listing}" 

