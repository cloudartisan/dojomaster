from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Attendance


class ListAttendanceView(LoginRequiredMixin, ListView):
    model = Attendance


class DetailAttendanceView(LoginRequiredMixin, DetailView):
    model = Attendance


class UpdateAttendanceView(LoginRequiredMixin, UpdateView):
    model = Attendance


class CreateAttendanceView(LoginRequiredMixin, CreateView):
    model = Attendance


class DeleteAttendanceView(LoginRequiredMixin, DeleteView):
    model = Attendance


class FormAttendanceView(LoginRequiredMixin, FormView):
    model = Attendance
