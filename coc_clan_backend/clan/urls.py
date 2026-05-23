from django.urls import path
from .views import members_list, wars_list, attacks_list, notices_list, analytics_overview, member_performance, sync_clan_members

urlpatterns = [
    path('members/', members_list),
    path('sync-members/', sync_clan_members),
    path('wars/', wars_list),
    path('attacks/', attacks_list),
    path('notices/', notices_list),
    path('analytics_overview/', analytics_overview),
    path('member_performance/', member_performance)
]