from django.urls import path
from . import views

handler500 = views.custom_500
urlpatterns = [
    path('', views.index, name='index'),
    path('crypt/', views.CryptFormView.as_view(), name='crypt'),
    path('crypt1', views.CryptView.as_view(), name='crypt_messanger'),
    path('decrypt/', views.DeCryptFormView.as_view(), name='crypt_msg'),
    path('crypt/<int:pk>/', views.SingleCryptView.as_view(), name='crypt-decrypt'),
    path('error', views.custom_500),
]