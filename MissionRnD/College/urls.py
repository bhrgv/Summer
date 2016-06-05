from django.conf.urls import url , include
from django.contrib import admin
from College import views
urlpatterns = [
    url(r'^view/(?P<acronym>[A-Za-z]+)/$',views.view,name='college'),
    url(r'^mail/',views.student,name='student'),
]
