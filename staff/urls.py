from django.urls import path

from .import views

urlpatterns = [
    path('api/staff/', views.StaffList.as_view(), name="staff"),
]
