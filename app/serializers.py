from rest_framework.serializers import ModelSerializer
from app.models import clpModel

class clpSerializer(ModelSerializer):
    class Meta:
        model = clpModel
        fields = '__all__'