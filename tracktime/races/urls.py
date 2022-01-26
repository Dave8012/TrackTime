from django.urls import path

from . import views

app_name = 'races'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('times/', views.TimesView.as_view(), name='times')
]
