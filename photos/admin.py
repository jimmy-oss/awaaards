from django.contrib import admin
from .models import Photo,Category,Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Profile)
