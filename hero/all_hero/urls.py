from django.urls import path,re_path
from . import views
#from django.urls import converters,register_converter



urlpatterns=[
	path('', views.index),
	#path('tiaozhuan/<herolist>', views.tiaozhuan, name='gohere'),
	#re_path(r'detail/(?P<hero_name>\w+|(\w+\+\w+)+)/', views.hero_list),
	path('getlist/<cate:hero_name>/', views.get_list, name='list1'),
]