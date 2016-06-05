from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from College.models import Student,College,Marks
from django.db.models import Avg,Count,Max,Min


#imports for Mailing
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def sendMail(toemail,message, from_emailid, password):
    msg = MIMEMultipart()
    msg['Subject'] = 'Mock Test 1 Marks'
    msg['From'] = from_emailid
    msg['To'] = toemail

    text = MIMEText(message)
    msg.attach(text)


    s = smtplib.SMTP('mail.riseup.net:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(from_emailid, password)
    s.sendmail(from_emailid, toemail, msg.as_string())
    s.quit()


def view(request,acronym=None):
    student=None
    college=None
    if(acronym):
        college=College.objects.get(acronym=acronym)
        student = Student.objects.all().filter(college__acronym=acronym)
    else:
        college=College(name="All",acronym="All",email="contact@all.edu",location="all")
        student = Student.objects.all()
    template = loader.get_template('student.html')
    context = {
        'students': student,
        'college' : college,
    }
    result = template.render(context=context, request=request)
    return HttpResponse(result)
def profile(request):
    return render(request,"index.html")
def student(request):
    marks=Marks.objects.all()
    avg=Marks.objects.all().aggregate(total=Avg('total'))
    max = Marks.objects.all().aggregate(max=Max('total'))
    min = Marks.objects.all().aggregate(min=Min('total'))
    count = Marks.objects.all().count()
    template = loader.get_template('report.txt')
    result=""
    for mark in marks:
        context = {
            'marks': mark,
            'highest': max,
            'lowest' : min,
            'average' : avg,
            'total' : count,
        }
        temp = template.render(context=context, request=request)
        result = result+"\n\n"+temp
        try:
            sendMail("bhargav2014duggu@gmail.com",result,"bhargavreddi@riseup.net","Pas#56c927441f739 ")
        except Exception:
            return HttpResponse("Mail Sending Failed")
    return HttpResponse("Mail Sending Successful")