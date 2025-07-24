from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('submit_case/', views.submit_case_view, name='submit_case'),
    path('my_cases/', views.my_cases_view, name='my_cases'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('change_status/<int:case_id>/', views.change_case_status, name='change_case_status'),
    path('update_case/<int:case_id>/', views.update_case, name='update_case'),
    path('delete_case/<int:case_id>/', views.delete_case, name='delete_case'),
]
