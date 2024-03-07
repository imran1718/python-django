from .views import formdata, api
from django.urls import path

urlpatterns = [path("form", formdata, name="view_name"),
               path("api", api)]
