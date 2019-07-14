from django.shortcuts import render
from part2.models import *
from django.http import HttpResponse,JsonResponse
import time,json


# 为用户界面提供初始数据
# render用于返回xml文件，三个参数中，第一个为请求，第二个为xml文件名，第三个为向该请求传递的数据
def ini_ward(request):
    ward_list = Wards.objects.all()
    return render(request,"index.html",{"ward_list":ward_list})


# 添加数据操作
# JsonResponse用于返回json格式数据
def add_ward(request):
    ward = Wards()
    ward.ward_id = 108
    ward.equit_id = 108
    ward.start_date = time.strftime("%Y-%m-%d",time.localtime())
    ward.state = 'u'
    ward.save()
    return JsonResponse({'msg': "插入成功"})


# 删除数据操作
def del_ward(request):
    ward_id = request.GET.get("ward_id")
    ward = Wards.objects.get(ward_id=ward_id)
    ward.delete()
    return JsonResponse({'msg': "删除成功"})


# 更新数据操作
def update_ward(request):
    ward = Wards(**json.loads(request.body))
    ward.save()
    return JsonResponse({'msg': '更新成功'})

