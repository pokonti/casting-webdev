from django.contrib import admin
from .models import Casting, Ad, Form, Position
# Register your models here.
admin.site.register(Casting)
admin.site.register(Position)
admin.site.register(Form)
admin.site.register(Ad)

