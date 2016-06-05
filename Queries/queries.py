__author__ = 'Bhargav'
import django
import sys,os
#from django.core.management import setup_environ
#from MissionRnD import settings

sys.path.append("C:/MissionRnD/")
os.environ["DJANGO_SETTINGS_MODULE"] = "MissionRnD.settings"
django.setup()
from College.models import *
#print all Colleges
query1=College.objects.all()
#print query1.query
#print query1


#print the College Count
query2=College.objects.all().count()
#print query2
import pprint


#get acronym and email of all Colleges
query3=list(College.objects.values_list('acronym','email'))
#print query3
#pprint.pprint(query3)


#list the Colleges based on acronym ASC
query4=College.objects.order_by('acronym')
#print query4.query
#print query4



#list the Colleges based on Location DESC
query5=College.objects.order_by('-location')
#print query5.query
#print query5



#list first 5 Colleges based on Location DESC
query6=College.objects.order_by('-location')[:5]
#print query6.query
#print query6


#list first 6-10 Colleges based on Location DESC
query7=College.objects.order_by('-location')[5:10]
#print query7.query
#print query7


#list first 11 to end Colleges based on Location DESC
query8=College.objects.order_by('-location')[10:]
#print query8.query
#print query8


#how many colleges in each location
from django.db.models import Count
query9=College.objects.values('location').annotate(count=Count('location'))
#print query9.query
#print query9


#colleges names in each location sort by location
from django.db.models import Count
query10=College.objects.values('name').order_by('location')
#print query10.query
#print query10



#how many colleges in each location sort by count DESC
from django.db.models import Count
query11=College.objects.values('location').annotate(count=Count('location')).order_by('-count')
print query11.query
print query11


#acronym and contact of college in each location sort by location
from django.db.models import Count
query12=College.objects.values('acronym','email').order_by('location')
#print query12.query
#print query12


#get count of all students
query13=Student.objects.all().count()
#print query13


#get students who have rohit int their name
query14=Student.objects.filter(name__icontains='rohit')
print query14.query
print query14


#get all students from bvritn
query15=Student.objects.all().filter(college__acronym='bvritn')
#print query15.query
#print query15


#get college acronym and count of students in that college
query16=Student.objects.values('college__acronym').annotate(count=Count('college__acronym'))
#print query16.query
#print query16


#get college acronym and count of students in that college in sorted desc count
query17=Student.objects.values('college__acronym').annotate(count=Count('college__acronym')).order_by('-count')
#print query17.query
#print query17


#get college acronym and count of students in that college in sorted desc count - 2
query18=Student.objects.values('college__acronym').annotate(count=Count('college__acronym')-2).order_by('-count')
#print query18.query
#print query18


#get location and student count sorted by desc
query19=Student.objects.values('college__location').annotate(count=Count('college__location')).order_by('-count')
#print query19.query
#print query19


#get location with max student count
from django.db.models import Max
query20=Student.objects.values('college__location').annotate(count=Count('college__location')).order_by('count').aggregate(Max('count'))
print query20


#Identify the Problem
#get teacher;s count and student count in a particular college
#query21=Student.objects.values('college__acronym').annotate(count=Count('college__acronym'))
#query22=Teacher.objects.values('college__acronym').annotate(count=Count('college__acronym'))
query21=College.objects.annotate(count1=Count('student',distinct=True)).annotate(count2=Count('teacher',distinct=True)).values("acronym","count1","count2")
print query21.query
print query21


#Sort by total desc - get total, name and college acronym
query22=Marks.objects.values_list("total","name__name","name__college__acronym").order_by("-total")
#print query22.query
#print list(query22)


#Sort by total desc those who got >= 30 - get total, name and acronym
query22=Marks.objects.values_list("total","name__name","name__college__acronym").filter(total__gt=30).order_by("total")
#print query22.query
#print query22


#Get total student count
query23=Marks.objects.all().count()
#print query23.query
print query23


#Get of folks who got >=30
#query24


#average score and student count for each college
from django.db.models import Avg
query25=Marks.objects.all().values('total').annotate(count=Count('name__college__acronym'))
print query25


#class min, average and max -> Coming from the MockTest1 (ie) only for non-dropped students.


#min max and average over all colleges -> Coming from College model assuming that dropped students are also valid class students. Did it really change?


#min max and average over all colleges -> Change query so that even students with missing data are considered for averages (they bring down the average)


#min max and avg per college -> from mocktest1 side (for only non dropped students)


#min max and avg per college sorted by average desc-> from college side (for non dropped students)


#min max and avg per college sorted by Max desc-> from college side (considering dropped students as valid students with no marks)

"""
import smtplib
#from email.mime.MIMEImage import MIMEImage
from email.mime.multipart import MIMEMultipart
import pygal
from django.db.models import Min
#import urllib
def chart():
    a=Marks.objects.values('name__college__acronym').annotate(min=Min('total'),max=Max('total'),avg=Avg('total'))
    college=[]
    MIN=[]
    MAX=[]
    AVG=[]
    for i in a:
        MIN.append(i['min'])
        MAX.append(i['max'])
        AVG.append(i['avg'])
        college.append(i['name__college__acronym'])
    line_char=pygal.Bar()
    line_char.title="College Marks"
    line_char.x_labels=college
    line_char.add('MAX',MAX)
    line_char.add('MIN', MIN)
    line_char.add('AVG', AVG)
    file_name="min_max_avg.png"
    line_char.render_to_png(file_name)
chart()
"""