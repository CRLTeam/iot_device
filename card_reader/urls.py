from django.urls import path

from card_reader import views

urlpatterns = [
    path('', views.index, name='index'),
    path('command/', views.command),
    path('status/', views.status),
    path('settings/', views.devsettings),
    path('monitor/', views.monitor),
    path('simulation/', views.simulation),
    path('simulation/start/', views.start),
    path('simulation/stop/', views.stop),
    path('monitor/stats/', views.stats),

]