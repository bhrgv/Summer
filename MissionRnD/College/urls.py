from django.conf.urls import url , include
from django.contrib import admin
from College import views , college_views
urlpatterns = [
    #url(r'^view/(?P<acronym>[A-Za-z]+)/$',views.view,name='college'),
    url(r'^mail/',views.student,name='student'),
    url(r'^list/$',college_views.CollegeListView.as_view(),name="college_list"),
    url(r'^student/list/$',college_views.StudentListView.as_view(),name="student_list"),
    #url(r'^student/(?P<location>[a-zA-Z]*)/$',college_views.StudentListView.as_view(),name="student_list"),
    url(r'^(?P<pk>[0-9]+)/$',college_views.CollegeDetailView.as_view(),name="college_pk_details"),
    url(r'^(?P<acronym>[-\w]+)/detail$',college_views.CollegeDetailView.as_view(),name="college_acronym_details"),
    url(r'^create/$',college_views.CollegeCreateView.as_view(),name="create_college_details"),
    url(r'^update/(?P<pk>[0-9]+)$',college_views.CollegeUpdateView.as_view(),name="update_college_details"),
    url(r'^delete/(?P<pk>[0-9]+)$',college_views.CollegeDeleteView.as_view(),name="delete_college_details"),
    url(r'^student/create/$',college_views.StudentCreateView.as_view(),name="create_student_details"),
    url(r'^student/update/(?P<pk>[0-9]+)$',college_views.StudentUpdateView.as_view(),name="update_student_details"),
    url(r'^student/delete/(?P<pk>[0-9]+)$',college_views.StudentDeleteView.as_view(),name="delete_student_details"),
    url(r'^marks/list/$',college_views.MarksListView.as_view(),name="marks_list"),
    url(r'^marks/add/$',college_views.MarksCreateView.as_view(),name="create_marks_details"),
    url(r'^marks/update/(?P<pk>[0-9]+)$',college_views.MarksUpdateView.as_view(),name="update_marks_details"),
    url(r'^marks/delete/(?P<pk>[0-9]+)$',college_views.MarksDeleteView.as_view(),name="delete_marks_details"),
]
