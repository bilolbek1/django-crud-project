from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from crud.forms import PeopleCreateForm
from crud.models import People


# Create your views here.

class BaseView(View):
    def get(self, request):
        people = People.objects.all()
        search = request.GET.get('q', '')
        queryset = People.objects.all().order_by('-id')[:7]


        if search:
            people = people.filter(
                Q(job__icontains=search) | Q(name__icontains=search)
            )
        count = people.count()




        context = {
            'count': count,
            'people': people,
            'query': queryset
        }
        return render(request, 'base.html', context)



class PeopleCreateView(View):
    def get(self, request):
        people = PeopleCreateForm()

        context = {
            'people': people
        }
        return render(request, 'create.html', context)

    def post(self, request):
        people = PeopleCreateForm(data=request.POST)

        if people.is_valid():
            people.save()
            return redirect(reverse('base'))

        else:
            context = {
                'people': people
            }
            return render(request, 'create.html', context)




class PeopleEditView(View):
    def get(self, request, id):
        people = People.objects.get(id=id)
        people_form = PeopleCreateForm(instance=people)

        context = {
            'people': people,
            'people_form': people_form
        }
        return render(request, 'update.html', context)


    def post(self, request, id):
        people = People.objects.get(id=id)
        people_form = PeopleCreateForm(instance=people, data=request.POST)

        if people_form.is_valid():
            people.save()
            return redirect(reverse('base'))

        else:
            context = {
                'people': people,
                "people_form": people_form
            }
            return render(request, 'update.html', context)



class PeopleDeleteView(View):
    def get(self, request, id):
        people = People.objects.get(id=id)
        people.delete()
        return redirect(reverse('base'))