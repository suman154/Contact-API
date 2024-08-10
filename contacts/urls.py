from django.urls import path
from . views import ContactList, ContactDetails

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetails.as_view()),
]
