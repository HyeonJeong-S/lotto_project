from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('buy/', views.buy_lotto, name = 'buy_lotto'),
    path('check/', views.check_result_page, name = 'check_result_page'),
    path('check/<int:round>/', views.check_result, name = 'check_result'),
    path('draw/', views.draw_numbers, name = 'draw_numbers')
]
