from django.urls import path
from .views import CreateRestaurantView, UploadMenuView, CurrentDayMenuView

urlpatterns = [
    path('create/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('upload_menu/', UploadMenuView.as_view(), name='upload_menu'),
    path('current_day_menu/', CurrentDayMenuView.as_view(), name='current_day_menu'),
]