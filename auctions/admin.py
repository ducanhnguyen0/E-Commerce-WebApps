from django.contrib import admin
from .models import User, Category, Listings, Comments, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listings)
admin.site.register(Comments)
admin.site.register(Bid)