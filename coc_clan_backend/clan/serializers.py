from rest_framework import serializers
from .models import Member, War, Attack, Notice

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class WarSerializer(serializers.ModelSerializer):
    class Meta:
        model = War
        fields = '__all__'

class AttackSerializer(serializers.ModelSerializer):

    member_name = serializers.CharField(
        source='member.name',
        read_only=True
    )

    class Meta:
        model = Attack
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'