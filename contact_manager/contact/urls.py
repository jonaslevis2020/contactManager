from os import name

from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home_view.as_view(), name='index'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('detail/<int:pk>/', views.detail_view.as_view(), name='detail'),
    path('search/', views.search, name='search'),
    path('contacts/create', views.ContactCreateView.as_view(), name='create'),
    path('contacts/update/<int:pk>/', views.ContactUpdateView.as_view(), name='update'),
    path('contacts/delete/<int:pk>/', views.ContactDeleteView.as_view(), name='delete')
]