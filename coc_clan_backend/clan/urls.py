from django.urls import path
from .views import members_list, wars_list, attacks_list, notices_list

urlpatterns = [
    path('members/', members_list),
    path('wars/', wars_list),
    path('attacks/', attacks_list),
    path('notices/', notices_list),
]