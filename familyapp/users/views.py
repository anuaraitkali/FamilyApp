from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer

# Create your views here.

def welcome(request):
    return JsonResponse({"message": "Welcome to FamilyApp"})

class RegistrationView(APIView):
    def post (self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User registered successfully"}, status=201)
        return Response(serializer.errors, status=401)


