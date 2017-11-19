from rest_framework import serializers

from .models import Members,Farms,Wells,Crop,Vill,Medicare,Dealer,MediUpdates

#class Serializer(serializers.ModelSerializer):

 #   class Meta:
  #      model=Households
   #     fields='__all__'
class aSerializer(serializers.ModelSerializer):

    class Meta:
        model=Members
        fields='__all__'
class bSerializer(serializers.ModelSerializer):

    class Meta:
        model=Farms
        fields='__all__'

class cSerializer(serializers.ModelSerializer):

    class Meta:
        model=Wells
        fields='__all__'

class dSerializer(serializers.ModelSerializer):

    class Meta:
        model=Crop
        fields='__all__'
		
class eSerializer(serializers.ModelSerializer):

    class Meta:
        model=Vill
        fields='__all__'
class fSerializer(serializers.ModelSerializer):

    class Meta:
        model=Medicare
        fields='__all__'
class gSerializer(serializers.ModelSerializer):

    class Meta:
        model=Dealer
        fields='__all__'
class hSerializer(serializers.ModelSerializer):

    class Meta:
        model=MediUpdates
        fields='__all__'
