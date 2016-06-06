from django.conf.urls import url , include
from django.contrib import admin
from College import views , college_views
urlpatterns = [
    url(r'^view/(?P<acronym>[A-Za-z]+)/$',views.view,name='college'),
    url(r'^mail/',views.student,name='student'),
    url(r'^college/$',college_views.CollegeListView.as_view(),name="college_list"),
    url(r'^student/$',college_views.StudentListView.as_view(),name="student_list"),
    #url(r'^student/(?P<location>[a-zA-Z]*)/$',college_views.StudentListView.as_view(),name="student_list"),
    url(r'^college/(?P<pk>[0-9]+)',college_views.CollegeDetailView.as_view(),name="college_pk_details"),
    url(r'^college/(?P<acronym>[-\w]+)/detail$',college_views.CollegeDetailView.as_view(),name="college_acronym_details"),
    url(r'^college/create/$',college_views.CollegeCreateView.as_view(),name="create_college_details"),
]
