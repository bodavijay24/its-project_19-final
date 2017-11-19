from django.shortcuts import get_object_or_404,render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Members,Farms,Wells,Crop,Vill,Medicare,Dealer,MediUpdates
from .serializers import aSerializer,bSerializer,cSerializer,dSerializer,eSerializer,fSerializer,gSerializer,hSerializer
from pallevelugu.forms import HomeForm
from django.http import HttpRequest

#class Det1(APIView):

 #   def get(self,request):
  #      Household = Households.objects.all()
   #     serializer =Serializer(Household,mjany=True)
    #    return Response(serializer.data)
    #def post(self):
     #   pass
class Det2(APIView):

    def get(self,request):
        mem = Members.objects.all()
        serializer =aSerializer(mem,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class Det3(APIView):

    def get(self,request):
        farm = Farms.objects.all()
        serializer =bSerializer(farm,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class Det4(APIView):

    def get(self,request):
        well = Wells.objects.all()
        serializer =cSerializer(well,many=True)
        return Response(serializer.data)
    def post(self):
        pass
        pass
class Det5(APIView):

    def get(self,request):
        crop = Crop.objects.all()
        serializer =dSerializer(crop,many=True)
        return Response(serializer.data)
    def post(self):
        pass
		
class Det6(APIView):

    def get(self,request):
        vill = Vill.objects.all()
        serializer =eSerializer(vill,many=True)
        return Response(serializer.data)
    def post(self):
        pass
		
class Det7(APIView):

    def get(self,request):
        Medi = Medicare.objects.all()
        serializer =fSerializer(Medi,many=True)
        return Response(serializer.data)
    def post(self):
        pass
		
class Det8(APIView):

    def get(self,request):
        Deal = Dealer.objects.all()
        serializer =gSerializer(Deal,many=True)
        return Response(serializer.data)
    def post(self):
        pass
		
class Det9(APIView):

    def get(self,request):
        Mup = MediUpdates.objects.all()
        serializer =hSerializer(Mup,many=True)
        return Response(serializer.data)
    def post(self):
        pass