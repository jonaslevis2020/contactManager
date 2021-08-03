from typing import Any
from django.forms.models import ModelForm
from django.http import request
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from contact.models import Contact
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q, manager
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.

# def index(request , *args, **kwargs):

#     contacts = Contact.objects.all()
#     total = len(contacts)
#     context = {
#         'contacts':contacts,
#         'total':total
#     }

#     return render(request, 'index.html', context)

# def detail(request,id):
#     contact = get_object_or_404(Contact, pk=id)
#     # contact = Contact.objects.get(id=id)
#     context = {
#         'contact': contact
#     }
#     return render(request, 'detail.html', context)

@login_required
def search(request):
    if (request.GET):
        kw = request.GET['q']
        contacts = Contact.objects.filter(Q(name__icontains=kw)|
                                        Q(phone__icontains=kw)|
                                        Q(email__icontains=kw)|
                                        Q(info__icontains=kw))
        result = contacts.filter(manager = request.user)
        context = {
            'kw':kw,
            'contacts':result,
            'total':len(result)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('index')


#LoginRequiredMixin should be the first parameter
class home_view(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        print(len(contacts.filter(manager = self.request.user)))
        return contacts.filter(manager = self.request.user)


# class search_view(ListView):
#     template_name = 'search.html'
#     model = Contact
#     context_object_name = 'contacts'

class detail_view(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name','email','phone','info','gender','image']
    def form_valid(self, form):
            form_instance = form.save(commit = False)
            form_instance.manager = self.request.user
            form_instance.save()
            messages.success(self.request, "Your contact has been created successfully!!!")
            return redirect('index')

class ContactUpdateView(LoginRequiredMixin, UpdateView):
        model = Contact
        context_object_name = 'contact'
        template_name = 'update.html'
        fields = ['name','email','phone','info','gender','image']

        def form_valid(self, form):
            form_instance = form.save(commit = True)
            contact_name = form_instance.id
            print(contact_name)
            messages.success(self.request, "Successfully updated contact with ID :"+str(contact_name))
            return redirect('detail',form_instance.pk)

    # def form_invalid(self, form: ModelForm) -> HttpResponse:
    #     return super().form_invalid(form)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'
    def delete(self, request: request.HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        messages.success(self.request, "Your contact has been deleted succesfully!")
        return super().delete(request, *args, **kwargs)

def log_out(request):
    logout(request)
    return render(request, 'log_out.html', {})

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')