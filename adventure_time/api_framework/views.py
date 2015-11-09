from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from atus.models import Respondent, ActivityResponse, ActivityTitle
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer
import django_filters

def hello(request):
    all_respondents = Respondent.objects.all()
    serialized_data = serializers.serialize("json", all_respondents)
    return HttpResponse(serialized_data, content_type="application/json")

@csrf_exempt
def api_respondent_list_view(request):
    qs = Respondent.objects.all()
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")

@csrf_exempt
def api_respondent_detail_view(request, model_pk):
    qs = Respondent.objects.filter(id=model_pk)
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")

@csrf_exempt
def api_activitytitle_list_view(request):
    qs = ActivityTitle.objects.all()
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")


class RespondentSerializer(ModelSerializer):

    class Meta:
        model = Respondent


class RespondentListView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class RespondentDetailView(RetrieveAPIView):
    queryset = Respondent.objects.filter()
    serializer_class = RespondentSerializer


class ActivityResponseSerializer(ModelSerializer):

    class Meta:
        model = ActivityResponse


class ActivityTitleSerializer(ModelSerializer):

    class Meta:
        model = ActivityTitle


class ActivityResponseListView(ListAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer


class ActivityResponseDetailView(RetrieveAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer


class ActivityTitleListView(ListAPIView):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer


class ActivityTitleDetailView(RetrieveAPIView):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer


"""class RespondentFilterView(ListAPIView):
    serializer_class = RespondentSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Respondent.objects.all()
        new_set = []
        for respondent in queryset:
            if respondent.age <= 50:
                new_set.append(respondent)
        queryset = new_set
        return queryset"""


class RespondentFilterView(django_filters.FilterSet):

    class Meta:
        model = Respondent
        fields = ['age', 'sex', 'education', 'race', 'metro_status', 'labor_status', 'wkly_earnings', 'multiple_job_status',
                  'full_or_part_job_status', 'school_enrollment', 'school_level', 'typical_work_hrs']


def respondent_filter_list(request):
    f = RespondentFilterView(request.GET, queryset=Respondent.objects.all())
    return render_to_response('my_app/template.html', {'filter': f})

