from django.urls import path

from .import views

urlpatterns = [
    path('api/staff/', views.StaffList.as_view(), name="staff"),
    path('', views.show_staff, name="home"),
    path('add/', views.staff_add, name="staff_add"),
    path('update/<int:id>/', views.staff_update, name="staff_update"),
    path('delete/<int:id>/', views.staff_delete, name="staff_delete"),
    path('search/', views.post_search, name='staff_search'),

]
