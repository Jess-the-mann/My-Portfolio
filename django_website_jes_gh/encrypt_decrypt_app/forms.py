from django import forms
from rest_framework import serializers
from .models import *
from .simple_encryption import *
#from drf_braces.serializers.form_serializer import FormSerializer

class CryptForm(forms.ModelForm):
    #hide = forms.HiddenInput()
    class Meta:
        model = Cryption
        fields = "__all__"
        widgets = {
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'enter your message',
                'text-align' : 'center',
                'background-color' : 'lightgreen',
                }),
            'start_key': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 160px;',
                'placeholder': 'enter a number'
                }),
            'key_increment': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 160px;',
                'placeholder': 'enter a number'
                }),
            'key_increments_increment': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 160px;',
                'placeholder': 'enter a number'
                }),
        }
class CryptSerializer(serializers.ModelSerializer):
    #encrypted_message = serializers.SerializerMethodField()
    class Meta:
        model = Cryption
        fields = "__all__"
        #fields = ["id","message","start_key","key_increment","key_increments_increment","encrypted_message"]
        extra_kwargs = {"encrypted_message":{'allow_null':True}}
    '''def get_encrypted_message(self, message):
        encrypted_message = self.fields
        encrypted_message = str(encrypted_message)
        encryption = message
        encryption = encryption
        #return Response([str(l),str(encryption)])
        msg = encryption['message']
        key1 = encryption['start_key']
        key2 = encryption['key_increment']
        key3 = encryption['key_increments_increment']
        encrypted_message = encoding_time(msg,key1,key2,key3)
        encrypted_message = encrypted_message[0
        return encrypted_message'''
    
        
    #encoding_time()
    #encrypted_message = forms.TextInput('Enter your message here: ')