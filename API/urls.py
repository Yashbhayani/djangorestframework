from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('user', Post_User),
    path('file', Post_FILE),
    path('userupdate/<id>', Update_User),
    path('userdelete/<id>', Delete_User),
    path('book/', BookAPI.as_view()),
]
