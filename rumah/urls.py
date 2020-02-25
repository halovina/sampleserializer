from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/property/',views.Property145Listings.as_view(), name='property-listings'),

]