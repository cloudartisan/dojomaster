from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import School


class SchoolList(LoginRequiredMixin, ListView):
    model = School


class SchoolDetail(LoginRequiredMixin, DetailView):
    model = School


class SchoolUpdate(LoginRequiredMixin, UpdateView):
    model = School


class SchoolCreate(LoginRequiredMixin, CreateView):
    model = School


class SchoolDelete(LoginRequiredMixin, DeleteView):
    model = School


class SchoolForm(LoginRequiredMixin, FormView):
    model = School
