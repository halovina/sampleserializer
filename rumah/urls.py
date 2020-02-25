from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # # api
    path('api/v1/property/',views.Property145Listings.as_view(), name='property-listings'),
    # path('api/v1/posts/<int:pk>',views.book_element, name='book_element')

]