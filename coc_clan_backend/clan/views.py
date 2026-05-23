# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Member, War, Attack, Notice
from .serializers import MemberSerializer, WarSerializer, AttackSerializer, NoticeSerializer

@api_view(['GET'])
def members_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def wars_list(request):
    wars = War.objects.all().order_by('-created_at')

    serializer = WarSerializer(wars, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def attacks_list(request):

    attacks = Attack.objects.select_related(
        'member',
        'war'
    ).order_by('-attack_time')

    serializer = AttackSerializer(attacks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def notices_list(request):

    notices = Notice.objects.all().order_by('-created_at')

    serializer = NoticeSerializer(notices, many=True)

    return Response(serializer.data)

