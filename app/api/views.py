from app.api.models import News
from rest_framework import viewsets
from app.api.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows News to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer