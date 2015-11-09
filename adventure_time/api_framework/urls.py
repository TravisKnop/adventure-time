
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from api_framework.views import api_respondent_detail_view, api_respondent_list_view, hello, RespondentListView, \
    RespondentDetailView, ActivityTitleListView, ActivityTitleDetailView, RespondentFilterView


class HouseholdMemberListView(object):
    pass


urlpatterns = [
    url(r'respondent/$', RespondentListView.as_view(), name="api_respondent_list_view"),
    url(r'respondent/(?P<pk>\d+)/$', RespondentDetailView.as_view(), name="api_respondent_detail_view"),
    url(r'respondent/filter/(?P<'age'>\d+)/', RespondentFilterView.as_view(), name="api_respondent_filter_view"),
    url(r'activity/$', ActivityTitleListView.as_view(), name="api_activitytitle_list_view"),
    url(r'activity/(?P<pk>\d+)/$', ActivityTitleDetailView.as_view(), name="api_activitytitle_detail_view"),
]

