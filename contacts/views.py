from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
# Create your views here.

class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = ([permissions.IsAuthenticated])
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    


    
class ContactDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = ([permissions.IsAuthenticated])
    lookup_field = 'id' # the field to look up the contact
    
    

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)