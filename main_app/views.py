from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from.models import Widget
from .forms import WidgetForm
from django.db.models import Sum

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    total_qnt = Widget.objects.aggregate(Sum('quantity'))

    context = {
        'widgets': widgets,
        'widget_form': widget_form,
        'total_qnt': total_qnt
    }
    return render(request, 'index.html', context)

def create_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
       form.save()

    return redirect ('/')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
