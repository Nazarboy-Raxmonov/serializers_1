from django.shortcuts import render, get_object_or_404
from .models import UsersModels, StaffModels
from .serializers import UserSerializers, StaffSerializers
from django.http import JsonResponse

def UsersDetailsViews(request, user_id):
    user = get_object_or_404(UsersModels,id = user_id)
    user_data = UserSerializers(user)
    return JsonResponse(user_data.data, safe = False)

def StaffDetailsViews(request, staff_id):
    staff = get_object_or_404(StaffModels, id = staff_id)
    staff_data = StaffSerializers(staff)
    return JsonResponse(staff_data.data, safe = False)

def UsersAllViews(request):
    users = UsersModels.objects.all()
    users_data = UserSerializers(users, many = True)
    return JsonResponse(users_data.data, safe = False)

def StaffAllViews(request):
    staffs = UsersModels.objects.all()
    staff_data = UserSerializers(staffs, many = True)
    return JsonResponse(staff_data.data, safe = False)