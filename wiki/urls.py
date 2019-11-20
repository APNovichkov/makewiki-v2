from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView
from wiki import views


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('newpage/', PageCreateView.as_view(), name="page-form"),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
