from rest_framework import serializers


 # user_data = {
 #        "name": "Prithviraj",
 #        "age": 25,
 #        "weight": 94,
 #        "height": 186,
 #        "fitness_goals": "lose fat and gain muscle",
 #        "dietary_preferences": "non veg",
 #        "mental_health_goals": "lose fat and maintain muscle"
 #    }

class FitnessAgentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    weight = serializers.IntegerField(required=True)
    height = serializers.IntegerField(required=True)
    fitness_goals = serializers.CharField(required=True)
    dietary_preferences = serializers.CharField(required=True)
    mental_health_goals = serializers.CharField(required=True)
