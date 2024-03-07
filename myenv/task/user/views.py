from django.shortcuts import render
from .models import MyModel
from .form import MyForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def formdata(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phonenumber = form.cleaned_data["phonenumber"]
            password = form.cleaned_data["password"]
            print(name, email, phonenumber, password)
            MyModel.objects.create(name=name, email=email, phonenumber=phonenumber,
                                   password=password)
            return HttpResponse("data saved successfully")
    else:
        form = MyForm()

    return render(request, "login.html", {"form": form})


@api_view(['GET'])
def api(request):
    if request.method == 'GET':
        data = MyModel.objects.all().values()
        print(data)
        return Response({'status': "true", "form_data": data})
