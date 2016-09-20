from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView,
        CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Student


class ListStudentView(LoginRequiredMixin, ListView):
    model = Student


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student


class FormStudentView(LoginRequiredMixin, FormView):
    model = Student
