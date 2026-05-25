from django.urls import path
from .views import (
    members_list,
    wars_list,
    current_war_attacks,
    attacks_by_war,
    notices_list,
    analytics_overview,
    member_performance,
    sync_clan_members,
    current_war,
    sync_current_war_api,
    current_members_list,
    left_members_list,
    clan_details
)

urlpatterns = [
    path('clan/', clan_details),
    path('members/', members_list),
    path('sync-members/', sync_clan_members),
    path(
        'current-members/',
        current_members_list
    ),
    path(
        'left-members/',
        left_members_list
    ),
    path('wars/', wars_list),
    path('current-war/', current_war),
    path('current-war-attacks/', current_war_attacks),
    path('sync-current-war/', sync_current_war_api),
    path(
    'attacks/<int:war_id>/',
    attacks_by_war
),
    path('notices/', notices_list),
    path('analytics_overview/', analytics_overview),
    path('member_performance/', member_performance)
]