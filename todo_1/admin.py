from atexit import register
from django.contrib import admin
from todo_1.models import contact,blog

# Register your models here.
admin.site.register(contact)
admin.site.register(blog)
