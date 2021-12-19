from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from django.http import HttpResponseRedirect
from .forms import StaffForm
from .models import Staff
from .serializer import StaffSerializer
from django.contrib import messages
from django.contrib.postgres.search import SearchVector


class StaffList(ListAPIView) :
    queryset = Staff.objects.filter(parent__isnull=True)
    serializer_class = StaffSerializer


@login_required()
def show_staff(request):
    data = request.GET
    try :
        sort_by = list(data.keys())[0]
    except :
        sort_by = 'id'

    employees = Staff.objects.order_by(sort_by)
    employees = employees | Staff.objects.order_by(sort_by)

    return render(request,
                  'staff_list.html',
                  {'employees' : employees, }
                  )


@login_required()
def staff_add(request, ):
    if request.method == 'POST':
        staff_form = StaffForm(data=request.POST)
        if staff_form.is_valid() :
            staff_form.save()
            messages.success(request, 'New Staff Added successfully')
            return HttpResponseRedirect("/")
        else :
            messages.error(request, 'Error creating your post')
            print(messages.get_messages(request))

    else :
        staff_form = StaffForm()

    return render(request, 'staff_add.html', {'staff_form' : staff_form, })


@login_required()
def staff_update(request, id):
    staff = get_object_or_404(Staff, pk=id, )
    staff_form = StaffForm(request.POST, instance=staff)

    if request.method == 'POST':
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, 'Staff info updated successfully')
            return HttpResponseRedirect(reverse('home'))
        else :
            messages.error(request, 'Error updating ')

    else:
        data_prepopulated = {'name' : staff.name, 'job_title' : staff.job_title, 'salary' : staff.salary,
                             'parent' : staff.parent}  # 'tags':post.tags
        staff_form = StaffForm(initial=data_prepopulated)

    return render(request, 'staff_update.html', {'staff_form' : staff_form, })


@login_required()
def staff_delete(request, id) :
    staff = get_object_or_404(Staff, pk=id, )
    data_prepopulated = {'name': staff.name, 'job_title': staff.job_title, 'salary': staff.salary,
                         'parent' : staff.parent}  # 'tags':post.tags
    staff_form = StaffForm(initial=data_prepopulated)
    if request.method == 'POST' :
        staff.delete()
        messages.success(request, 'Staff deleted successfully')
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'staff_delete.html', {'staff' : staff, 'staff_form' : staff_form})


@login_required()
def post_search(request) :
    if request.method == "POST" :
        query = request.POST['query']
        results = Staff.objects.all().annotate(
            search=SearchVector('job_title', 'name'),
        ).filter(search=query)
        return render(request, 'search.html',
                      {
                          'query' : query,
                          'results' : results
                      })
    else :
        return render(request, 'search.html',
                      {})


class StaffListView(ListView) :
    model = Staff
    template_name = 'orgchart/table.html'

    def get_queryset(self, *args, **kwargs) :
        qs = super(StaffListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("id")
        return qs
