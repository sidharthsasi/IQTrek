from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny  


# Create your views here.




class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (AllowAny,)  
    filter_backends = [filters.OrderingFilter]  
    ordering = ['-rating']  

    def get_queryset(self):
        queryset = super().get_queryset()
        city_code = self.request.GET.get('city_code')
        if city_code:
            queryset = queryset.filter(city_code=city_code)
        return queryset

class RestaurantFilterView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (AllowAny,)  
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        table_booking = self.request.GET.get('table_booking')
        online_delivery = self.request.GET.get('online_delivery')
        Cuisines = self.request.GET.get('cuisine')

        if table_booking:
            queryset = queryset.filter(table_booking=True)
        if online_delivery:
            queryset = queryset.filter(online_delivery=True)
        if Cuisines:
            for cuisine in Cuisines.split(','):
                queryset = queryset.filter(cuisines__contains=cuisine.strip())  
        return queryset



class CuisineAdd(APIView):

    def post(self, request):
        serializer = CuisineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Cuisine Successfully Added'},status=status.HTTP_201_CREATED)
    



class CuisineListAPIView(generics.ListAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer




class CuisineUpdate(APIView):
    def put(self,request,id):
        
        cusn = Cuisine.objects.get(id=id)
        serializer = CuisineSerializer(cusn,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Cuisine data updated'})
        


    def patch(self, request, id):
        
        cusn = Cuisine.objects.get(id=id)
        serializer = CuisineSerializer(cusn,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Cuisine partially updated'})
        



class CuisineDelete(APIView):

    def delete(self, request, id):
        
        cusn = get_object_or_404(Cuisine, id=id)
        cusn.delete()
        return Response({'message':'Data Deleted'})