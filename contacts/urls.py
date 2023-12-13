from django.urls import path
from .views import (contact_list, ContactCreate, ContactDetailView, ContactUpdate, ContactDelete)

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('new/', ContactCreate.as_view(), name='contact_new'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/update/', ContactUpdate.as_view(), name='contact_update'),
    path('<int:pk>/delete/', ContactDelete.as_view(), name='contact_delete'),
]
