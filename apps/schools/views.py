from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import School


class ListSchoolView(LoginRequiredMixin, ListView):
    model = School


class DetailSchoolView(LoginRequiredMixin, DetailView):
    model = School


class UpdateSchoolView(LoginRequiredMixin, UpdateView):
    model = School


class CreateSchoolView(LoginRequiredMixin, CreateView):
    model = School


class DeleteSchoolView(LoginRequiredMixin, DeleteView):
    model = School


class FormSchoolView(LoginRequiredMixin, FormView):
    model = School
