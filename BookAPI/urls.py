from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = []+router.urls

"""
  POSTMAN COLLECTION :
  https://api.postman.com/collections/17985660-494fc0ec-1d41-44b2-bd40-ccf8652ce2ac?access_key=PMAT-01GVNF94Q3MD1XKJQRVFS29DVZ
"""