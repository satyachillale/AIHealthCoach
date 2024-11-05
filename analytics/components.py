# analytics/utils.py
from .models import Query
from agents.models import UserData
from django.shortcuts import get_object_or_404

def populate_query_db(validated_data):
    """Extracts specific fields from validated data and populates the Query model."""
    # Extract fields
    user_id = validated_data.get("userId", [])
    fitness_goals = validated_data.get("fitness_goals", [])
    dietary_preferences = validated_data.get("dietary_preferences", [])
    mental_health = validated_data.get("mental_health_goals", [])

    # user_data = get_object_or_404(UserData, userId=user_id)
    user_data_entry = UserData.objects.filter(userId=user_id).first()

    # Create a descriptive query based on user data
    query_text = f"Fitness Goals: {fitness_goals}, Dietary Preferences: {dietary_preferences}, Mental Health Goals: {mental_health}"

    # Create a new Query object with the foreign key to UserData
    query = Query.objects.create(
        userId=user_data_entry,
        query=query_text
    )
