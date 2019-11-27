from django.urls import path

from .views import PageList, PageDetail

urlpatterns = [
    path('', PageList.as_view(), name='page_list'),
    path('<slug:slug>', PageDetail.as_view(), name='page_detail')
]
