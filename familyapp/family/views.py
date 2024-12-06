from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def FamilyInfo(request):
    return JsonResponse({"message": "This will show Family information"})
