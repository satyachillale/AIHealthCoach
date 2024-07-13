# AI Health Coach - Backend

This repository contains the backend implementation for the AI Health Coach project. The backend is built using Django and serves as the API layer for the application. It handles user data, interacts with AI agents, and stores generated health plans in a database.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [API Documentation](#api-documentation)

## Project Overview

The AI Health Coach backend provides API endpoints for generating personalized fitness, nutrition, and mental health plans. It leverages multiple AI agents to create these plans based on user data and feedback.

## Setup and Installation

### Prerequisites

- Python 3.9+
- Virtual Environment

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Prithviraj8/AIHealthCoach.git
    cd AIHealthCoach
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
   Or set up a conda env
    conda create -n venv python=3.9
    conda activate venv
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
   or 
    pip3 install -r requirements.txt
    ```

4. **Setup Environment Variables**:
    ```bash
    export OPENAI_API_KEY=<your_openai_api_key>
    export TAVILY_API_KEY=<your_tavily_api_key>
   ```

5. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## API Documentation

### Health Plan API
#### Description: This API endpoint accepts user data and generates a comprehensive health plan that includes a workout plan, a meal plan, and wellness tips.

**Curl Command**:
```bash
curl --location --request POST 'http://127.0.0.1:8000/agents/health_plan/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "latest",
    "age": 25,
    "weight": 50,
    "height": 150,
    "fitness_goals": "gain a little more weight",
    "dietary_preferences": "vegan",
    "mental_health_goals": "gain healthier weight and maybe a little more muscle"
}'
```

### Modified Health Plan
#### Description: This API endpoint accepts user feedback and modifies the existing health plan based on the feedback provided, returning an updated workout plan, meal plan, and wellness tips.

```
curl --location --request POST 'http://127.0.0.1:8000/agents/modified_health_plan/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fitness_feedback": "make it more rigorous",
    "nutrition_feedback": "be on caloric deficit",
    "mental_health_feedback": "All good here"
}'
```

### Guided Health Plan
#### Description: This API endpoint accepts detailed user data along with specific feedback and generates a more targeted health plan, including a workout plan, meal plan, and wellness tips.

```
curl --location --request POST 'http://127.0.0.1:8000/agents/guided_health_plan/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Prithviraj",
    "age": 25,
    "weight": 95,
    "height": 186,
    "fitness_goals": "gain a lot more muscle",
    "dietary_preferences": "non veg",
    "mental_health_goals": "lost fat fast",
    "fitness_feedback": "Need to focus on 1 full body part per day with more reps i.e focus on hypertrophy",
    "nutrition_feedback": "Need more carbs to focus at work",
    "mental_health_feedback": "All good here"
}'
```

## Contributing

1. **Fork the Repository**:
    - Click on the "Fork" button at the top right of this repository's page.

2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/Prithviraj8/AIHealthCoach.git
    cd AIHealthCoach
    ```

3. **Create a Feature Branch**:
    ```bash
    git checkout -b feature-branch-name
    ```

4. **Make Changes**:
    - Implement your changes in the feature branch.

5. **Commit Changes**:
    ```bash
    git add .
    git commit -m "Your commit message"
    ```

6. **Push Changes**:
    ```bash
    git push origin feature-branch-name
    ```

7. **Create a Pull Request**:
    - Go to your forked repository on GitHub and click on the "Pull Request" button to submit your changes for review.
