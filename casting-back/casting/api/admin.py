from django.contrib import admin
from .models import ApplicantToPosition, Casting, Ad, Form, Position
# Register your models here.
admin.site.register(Casting)
admin.site.register(Position)

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'user')
    search_fields = ('first_name',)
   

admin.site.register(Ad)
admin.site.register(ApplicantToPosition)

