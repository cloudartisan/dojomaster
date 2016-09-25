from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Grading


class ListGradingView(LoginRequiredMixin, ListView):
    model = Grading


class DetailGradingView(LoginRequiredMixin, DetailView):
    model = Grading


class UpdateGradingView(LoginRequiredMixin, UpdateView):
    model = Grading


class CreateGradingView(LoginRequiredMixin, CreateView):
    model = Grading


class DeleteGradingView(LoginRequiredMixin, DeleteView):
    model = Grading


class FormGradingView(LoginRequiredMixin, FormView):
    model = Grading
