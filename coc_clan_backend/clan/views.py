# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Member, War, Attack, Notice
from .serializers import MemberSerializer, WarSerializer, AttackSerializer, NoticeSerializer

from .services.coc_service import get_clan_members
from .services.member_sync import sync_members

@api_view(['GET'])
def members_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sync_clan_members(request):

    clan_tag = "#2Y2VGRQCY"

    data = get_clan_members(clan_tag)

    clan_members = data.get('items', [])

    sync_members(clan_members)

    return Response({
        "message": "Members synced successfully",
        "total_members": len(clan_members)
    })

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

@api_view(['GET'])
def analytics_overview(request):
    from django.db.models import Sum, Avg, Count

    total_wars = War.objects.count()
    total_stars = War.objects.aggregate(Sum('our_stars'))['our_stars__sum'] or 0
    total_destruction = War.objects.aggregate(Avg('our_destruction'))['our_destruction__avg'] or 0
    total_attacks = Attack.objects.count()
    attacks_used = Attack.objects.filter(attack_used=True).count()

    data = {
        'total_wars': total_wars,
        'total_stars': total_stars,
        'avg_destruction': round(total_destruction, 2),
        'total_attacks': total_attacks,
        'attacks_used': attacks_used,
    }

    return Response(data)

@api_view(['GET'])
def member_performance(request):
    from django.db.models import Avg, Count

    members = Member.objects.all()
    result = []

    for m in members:
        attacks = m.attacks.all()
        total_attacks = attacks.count()
        used_attacks = attacks.filter(attack_used=True).count()
        avg_stars = attacks.aggregate(Avg('stars'))['stars__avg'] or 0
        avg_destruction = attacks.aggregate(Avg('destruction_percentage'))['destruction_percentage__avg'] or 0

        result.append({
            'member': m.name,
            'total_attacks': total_attacks,
            'used_attacks': used_attacks,
            'avg_stars': avg_stars,
            'avg_destruction': round(avg_destruction, 2)
        })

    return Response(result)