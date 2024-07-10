from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet


# Create your views here.
from agents.serializers.serializers import FitnessAgentSerializer
from pprint import pprint

class Agents(GenericViewSet):

    def fitness(self, request):
        result = {"message": None, "error": None}
        serializer = FitnessAgentSerializer
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        print('request data: \n')
        pprint(validated_data)

        workflow = Workflow()



