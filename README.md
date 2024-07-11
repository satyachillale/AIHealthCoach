`curl --location --request POST 'http://127.0.0.1:8000/agents/health_plan/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Prithviraj",
    "age": 25,
    "weight": 94,
    "height": 186,
    "fitness_goals": "lose fat and gain muscle",
    "dietary_preferences": "non veg",
    "mental_health_goals": "lose fat and maintain muscle"
}'`