from wiki.models import Page
from api.serializer import PageSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class PageList(ListCreateAPIView):
    queryset = Page.objects.all()[:20]
    serializer_class = PageSerializer

class PageDetail(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
