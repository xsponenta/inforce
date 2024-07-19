from rest_framework import generics, permissions
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from datetime import date

class CreateRestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UploadMenuView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(user=self.request.user)
        serializer.save(restaurant=restaurant)

class CurrentDayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Menu.objects.filter(date=date.today())