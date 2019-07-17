from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("这是首页")

def get_list(request, hero_name):
	print("hero_name:%s"%hero_name)
	print(reverse('list1',kwargs={"hero_name":hero_name}))
	print(type(hero_name))
	return HttpResponse("得到英雄列表为%s"%hero_name)


'''
def hero_list(request, hero_name):
	return HttpResponse("英雄有%s"%hero_name)
	#return redirect(reverse())

def tiaozhuan(request,herolist):
	return HttpResponse("完成跳转%s"%herolist)
'''