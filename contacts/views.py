from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Contact

def home(request):
    return render(request, 'home.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

class ContactCreate(CreateView):
    model = Contact
    fields = ['name', 'email', 'notes']
    success_url = reverse_lazy('contact_list')
    template_name = 'contacts/contact_form.html'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 'email', 'notes']
    success_url = reverse_lazy('contact_list')
    template_name = 'contacts/contact_form.html'

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contacts/contact_confirm_delete.html'
