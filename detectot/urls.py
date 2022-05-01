from django.urls import path
from detectot.views import UserUpload


urlpatterns = [
    path('Upload/', UserUpload.as_view(), name='ImageUpload'),
]
