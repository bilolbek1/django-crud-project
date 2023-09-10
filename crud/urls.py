from django.urls import path

from crud.views import BaseView, PeopleCreateView, PeopleEditView, PeopleDeleteView

urlpatterns = [
   path('', BaseView.as_view(), name='base'),
   path('create/', PeopleCreateView.as_view(), name='create'),
   path('edit/<int:id>/', PeopleEditView.as_view(), name='edit'),
   path('delete/<int:id>/', PeopleDeleteView.as_view(), name='delete'),
]