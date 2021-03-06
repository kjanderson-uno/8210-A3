from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client
from django.urls import reverse_lazy


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('customer_id', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zipcode', 'email')
    template_name = 'client_edit.html'


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('customer_id', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zipcode', 'email')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
