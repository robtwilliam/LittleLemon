from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('menu/',views.MenuView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
]
