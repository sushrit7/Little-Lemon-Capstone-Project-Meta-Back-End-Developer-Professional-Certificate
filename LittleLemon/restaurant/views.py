from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    permissions_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]