from django.urls import path
from .views import *

urlpatterns = [
    path('restaurants/<str:city_code>/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/filter/', RestaurantFilterView.as_view(), name='restaurant-filter'),
    path('cuisine-add', CuisineAdd.as_view(),name='cuisine-add'),
    path('cuisines/', CuisineListAPIView.as_view(), name='cuisine-list'),
    path('cuisine-update/<int:id>/', CuisineUpdate.as_view(),name='cuisine-update'),
    path('cuisine-delete/<int:id>/', CuisineDelete.as_view(),name='cuisine-delete'),

]