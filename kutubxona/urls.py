from django.urls import path
from .views import StaffAllViews,UsersAllViews,StaffDetailsViews,UsersDetailsViews

urlpatterns = [
    path('user/details/<int:user_id>', UsersDetailsViews),
    path('staff/details/<int:staff_id>', StaffDetailsViews),
    path('users/all', UsersAllViews),
    path('staff/all', StaffAllViews)
]