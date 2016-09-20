from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView,
        CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Class


class ListClassView(LoginRequiredMixin, ListView):
    model = Class


class DetailClassView(LoginRequiredMixin, DetailView):
    model = Class


class UpdateClassView(LoginRequiredMixin, UpdateView):
    model = Class


class CreateClassView(LoginRequiredMixin, CreateView):
    model = Class


class DeleteClassView(LoginRequiredMixin, DeleteView):
    model = Class


class FormClassView(LoginRequiredMixin, FormView):
    model = Class
