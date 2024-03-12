from django.contrib import admin

# Register your models here.
from .models import User,Listings,Category,Comment,Bid

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listings)
admin.site.register(Comment)
admin.site.register(Bid)
    