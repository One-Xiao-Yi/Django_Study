from django.shortcuts import render
from part2.models import *
from django.http import HttpResponse,JsonResponse
import time,json


def ini_ward(request):
    ward_list = Wards.objects.all()
    return render(request,"index.html",{"ward_list":ward_list})


def add_ward(request):
    ward = Wards()
    ward.ward_id = 108
    ward.equit_id = 108
    ward.start_date = time.strftime("%Y-%m-%d",time.localtime())
    ward.state = 'u'
    ward.save()
    return JsonResponse({'msg': "插入成功"})


def del_ward(request):
    ward_id = request.GET.get("ward_id")
    ward = Wards.objects.get(ward_id=ward_id)
    ward.delete()
    return JsonResponse({'msg': "删除成功"})


def update_ward(request):
    ward = Wards(**json.loads(request.body))
    ward.save()
    return JsonResponse({'msg': '更新成功'})

