from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.


@api_view(['GET'])
def ngo(request):
    ngo = Ngo.objects.all()
    context = NgoSerializer(ngo, many=True)
    return Response(context.data)


@api_view(['GET'])
def donor(request):
    donor = Donor.objects.all()
    context = DonorSerializer(donor, many=True)
    return Response(context.data)


@api_view(['GET'])
def user(request):
    user = User.objects.all()
    context = UserSerializer(user, many=True)
    return Response(context.data)
