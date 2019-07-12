from django.shortcuts import render
from django.http import HttpResponse
from part1.models import Wards


def hello(request):
    ward_list = Wards.objects.all()
    for ward in ward_list:
        print(ward.ward_id)
        print(ward.equit_id)
        print(ward.start_date)
        print(ward.state)
    return HttpResponse("Hello Django")
