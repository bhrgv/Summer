# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from models import College,Student,Marks
class CollegeListView(ListView):
    model = College
    # template_name =
    # context_object_name =
    #adding extra context
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(PublisherDetail, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context
    pass
class StudentListView(ListView):
    model = Student
    template_name = 'student.html'
    context_object_name = 'students'

    def get_queryset(self):
        location = self.request.GET.get("location")
        # location = self.kwargs.get("location")
        if location:
            return Student.objects.filter(college__location__iexact=location)
        else:
            return Student.objects.all()

    # adding extra context
    # sending urls GETS , POST , url
    # http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
    def get_context_data(self, **kwargs):
        location = self.request.GET.get("location")
        #location = self.kwargs.get("location")
        # Call the base implementation first to get a context
        context = super(StudentListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if location:
            context['name'] = location
        else:
            context['name'] = 'Mission R&D'
        return context

class CollegeDetailView(DetailView):
    model = College
    def get_object(self, queryset=None):
        acronym = self.kwargs.get("acronym")
        if acronym:
            return College.objects.get(acronym__iexact=acronym)
        else:
            return College.objects.get(pk=self.kwargs['pk'])
#template name should be model_list.html
# class StudentListView(ListView):
#     model = Student
#     pass


class CollegeCreateView(CreateView):
    model = College
    fields = ['name','location','acronym','email']

    def get_success_url(self):
        return reverse('college_list')
        # return super(CollegeCreateView, self).get_success_url()


class CollegeUpdateView(UpdateView):
    model = College
    fields = ['name','location','acronym','email']

    def get_success_url(self):
        return reverse('college_list')
        # return super(CollegeCreateView, self).get_success_url()

class CollegeDeleteView(DeleteView):
    model = College
    def get_success_url(self):
        return reverse('college_list')
        # return super(CollegeCreateView, self).get_success_url()

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','college','email','dbfolder','dropout']

    def get_success_url(self):
        return reverse('student_list')
        # return super(CollegeCreateView, self).get_success_url()

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','college','email','dbfolder','dropout']

    def get_success_url(self):
        return reverse('student_list')
        # return super(CollegeCreateView, self).get_success_url()

class StudentDeleteView(DeleteView):
    model = Student
    def get_success_url(self):
        return reverse('student_list')
        # return super(CollegeCreateView, self).get_success_url()

class MarksListView(ListView):
    model = Marks
    template_name = 'marks.html'
    context_object_name = 'marks'

    def get_queryset(self):
        location = self.request.GET.get("location")
        # location = self.kwargs.get("location")
        if location:
            return Marks.objects.filter(name__college__location__iexact=location)
        else:
            return Marks.objects.all()

    # adding extra context
    # sending urls GETS , POST , url
    # http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
    def get_context_data(self, **kwargs):
        location = self.request.GET.get("location")
        #location = self.kwargs.get("location")
        # Call the base implementation first to get a context
        context = super(MarksListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if location:
            context['name'] = location
        else:
            context['name'] = 'Mission R&D'
        return context

class MarksCreateView(CreateView):
    model = Marks
    fields = ['name','transform','from_custom_base26','get_pig_latin','top_chars','total']

    def get_success_url(self):
        return reverse('marks_list')
        # return super(CollegeCreateView, self).get_success_url()

class MarksUpdateView(UpdateView):
    model = Marks
    fields = ['name','transform','from_custom_base26','get_pig_latin','top_chars','total']

    def get_success_url(self):
        return reverse('marks_list')
        # return super(CollegeCreateView, self).get_success_url()

class MarksDeleteView(DeleteView):
    model = Marks
    def get_success_url(self):
        return reverse('marks_list')
        # return super(CollegeCreateView, self).get_success_url()