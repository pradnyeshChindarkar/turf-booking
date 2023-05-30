from . import views
from django.urls import path

#URLConf
urlpatterns = [
    path('',views.index, name="home"),
    path('bookit/',views.bookit, name="bookIt"),
    path('bookit/form/<str:name>',views.form, name="form"),
    path('bookit/form/<str:name>/savebooking',views.saveBooking, name="formSub"),
    path('bookingreceipt',views.book_receipt, name='receipt'),
    # path('pay/',views.form, name="payment"),
    # path('formbook/',views.payment,name="pay" )
]
