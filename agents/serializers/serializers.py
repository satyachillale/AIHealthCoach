from rest_framework import serializers


class HealthPlanSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=False)
    weight = serializers.FloatField(required=True)
    height = serializers.FloatField(required=True)
    fitness_goals = serializers.CharField(required=True)
    dietary_preferences = serializers.CharField(required=True)
    mental_health_goals = serializers.CharField(required=True)


class ModifiedHealthPlanSerializer(serializers.Serializer):
    fitness_feedback = serializers.CharField()
    nutrition_feedback = serializers.CharField()
    mental_health_feedback = serializers.CharField()


class GuidedHealthPlanSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=False)
    weight = serializers.FloatField(required=True)
    height = serializers.FloatField(required=True)
    fitness_goals = serializers.CharField(required=True)
    dietary_preferences = serializers.CharField(required=True)
    mental_health_goals = serializers.CharField(required=True)
    fitness_feedback = serializers.CharField(required=False, default=None)
    nutrition_feedback = serializers.CharField(required=False, default=None)
    mental_health_feedback = serializers.CharField(required=False, default=None)
