from django.contrib import admin
from .models import Ground
from .models import MyUsers
from .models import Booking
from .models import Slot

# Register your models here.
# admin.site.register(Ground)
admin.site.register(MyUsers)
# admin.site.register(Booking)
admin.site.register(Slot)

@admin.register(Ground)
class GroundAdmin(admin.ModelAdmin):
    list_display=('name','address','phone')
    ordering = ('name',)
    search_fields = ('name','address')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ('user',('name','venue'),'slot','book_date','description')
    list_display = ('user','name','slot','venue','book_date')
    list_filter = ('book_date','venue')
    ordering = ('book_date',)
# class BookingAdmin(admin.ModelAdmin):
#     fields = (('name','venue'),'slot','book_date','description','manager')
#     list_display = ('name','slot','venue')
#     list_filter = ('book_date','venue')
#     ordering = ('book_date',)
"""
Username: admin
Password: bookturf
"""