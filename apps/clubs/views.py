from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView,
        CreateView, DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Club


class ListClubView(LoginRequiredMixin, ListView):
    model = Club


class DetailClubView(LoginRequiredMixin, DetailView):
    model = Club


class UpdateClubView(LoginRequiredMixin, UpdateView):
    model = Club


class CreateClubView(LoginRequiredMixin, CreateView):
    model = Club


class DeleteClubView(LoginRequiredMixin, DeleteView):
    model = Club


class FormClubView(LoginRequiredMixin, FormView):
    model = Club
