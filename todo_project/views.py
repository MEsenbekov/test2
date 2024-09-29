# todo_project/views.py
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'  # Укажите ваш шаблон
