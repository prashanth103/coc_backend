# from django.shortcuts import render

# Create your views here.
# clan/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer

@api_view(['GET'])
def members_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)