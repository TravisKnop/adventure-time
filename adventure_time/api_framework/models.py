from django.db import models

# Create your models here.
import django_filters
from atus.models import Respondent


class RespondentFilter(django_filters.FilterSet):
    class Meta:
        model = Respondent
        fields = {'age': ['lt', 'gt'], 'sex': ['exact']}


