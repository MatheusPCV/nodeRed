from rest_framework.views import APIView
from .serializers import clpSerializer
from .models import clpModel
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


class clpView(APIView):
    def post(self, request):
        serializer = clpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        clp = clpModel.objects.all()
        serializer = clpSerializer(clp, many=True)
        return Response(serializer.data)


class templateView(APIView):
    def get(self, request):
        lastInstance = clpModel.objects.latest("id")

        context = {
            "sensor": lastInstance.Sensor,
            "botao": lastInstance.Botao,
            "ligarobo": lastInstance.LigaRobo,
            "reset": lastInstance.ResetContador,
            "value": lastInstance.ValorContagem,
        }

        return render(request, "index.html", context)
