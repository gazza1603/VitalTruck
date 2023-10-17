from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('summary/', views.summary_view, name='summary'),
    path('vehicle/', views.vehicle_view, name='vehicle'),
    path('vital_app/update_status/<str:vehicleId>/<str:status>/', views.update_status, name='update_status'),
    path('download_report/<str:status>/', views.download_report, name='download_report'),
    path('graphs/', views.graphs, name='graphs'),
    path('reports/', views.report_view, name='reports'),

]