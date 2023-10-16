from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.response import Response
from .forms import *
from .models import *
from rest_framework import generics
from .simple_encryption import *
from django.views.generic.edit import FormView
from django.core import serializers, exceptions
import json

# Create your views here.
def index(request):
    return render(request,'index.html')

class CryptView(generics.ListCreateAPIView):
    queryset = Cryption.objects.all()
    serializer_class = CryptSerializer
    def post(self, request, *args, **kwargs):
        encryption = CryptSerializer(request.data)
        encryption = encryption.data
        msg = encryption['message']
        key1 = encryption['start_key']
        key2 = encryption['key_increment']
        key3 = encryption['key_increments_increment']
        encrypted_message = encoding_time(msg,key1,key2,key3)
        encrypted_message = encrypted_message[0]
        encoded=Cryption(message=msg,start_key=key1,key_increment=key2,key_increments_increment=key3)
        encoded = CryptSerializer(encoded,data=(CryptSerializer(encoded).data))
        if encoded.is_valid(): 
            encoded.save()
        new_msg = "Here is your encrypted message, Don't forget to copy it to your clipboard: "+ encrypted_message
        return Response(new_msg)
def custom_500(request):
    return render(request, '500.html', status=500)
class CryptFormView(FormView):
    template_name = "crypt_page.html"
    form_class = CryptForm
    success_url = '/success/'
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        msg = CryptForm(request.POST)
        msg1 = msg.save()
        encryption = msg.data
        msg = encryption['message']
        key1 = int(encryption['start_key'])
        key2 = int(encryption['key_increment'])
        key3 = int(encryption['key_increments_increment'])
        encrypted_message = encoding_time(msg,key1,key2,key3)
        for items in Cryption.objects.filter(message=msg):
            if (items.start_key == key1):
                if (items.key_increment == key2):
                    if items.key_increments_increment == key3:
                        pk = items.id
            else:
                pk=None
        crypt = {"pk":pk,"msg":encrypted_message[0],"start_key":encrypted_message[1],"key_increment":encrypted_message[2],"key_increments_increment":encrypted_message[3]}
        context = {"crypt":crypt}
        return render(request, 'success.html',context)
class SingleCryptView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cryption.objects.all()
    serializer_class = CryptSerializer
    def get(self, request, *args, **kwargs):
        inst = self.get_object()
        context = CryptSerializer(inst)
        context = context.data
        context = {"crypt":context}
        return render(request, 'encrypt_to_decrypt.html',context)
        msg = Cryption.objects.get(pk=pk)
class DeCryptFormView(FormView):
    template_name = "decrypt_page.html"
    form_class = CryptForm
    success_url = '/success/'
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        msg = CryptForm(request.POST)
        encryption = msg.data
        msg = str(encryption['message'])
        key1 = int(encryption['start_key'])
        key2 = int(encryption['key_increment'])
        key3 = int(encryption['key_increments_increment'])
        encrypted_message = decoding_time(msg,key1,key2,key3)
        msg = encrypted_message
        context = {"msg":msg}
        return render(request, 'decrypt.html',context)
