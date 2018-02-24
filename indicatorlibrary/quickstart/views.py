from django.contrib.auth.models import *
from rest_framework import viewsets
from indicatorlibrary.quickstart.serializers import *
from .models import Frequency, Indicator, Source


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FrequencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency to be viewed or edited.
    """
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source to be viewed or edited.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows indicators to be viewed or edited.
    """
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

class AdditionalFieldsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows additional fields to be viewed or edited.
    """
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer