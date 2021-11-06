from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_widget, name="create_widget"),
    path('delete/<int:pk>/', views.WidgetDelete.as_view(), name = "widget_delete")
]