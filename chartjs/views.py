from django.http import JsonResponse

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'chartjs/index.html')


####################################################

## if you don't want to user rest_framework

# def get_data(request,*args,**kwargs):
#
#     data={
#             "sales" : 100,
#             "person": 10000,
#     }
#
#     return JsonResponse(data) #http response


#######################################################

## using rest_framework classes

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        labels= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)
