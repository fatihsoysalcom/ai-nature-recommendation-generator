import random

def get_ai_recommendation(weather, mood):
    """Simulates an AI recommending outdoor activities based on weather and mood."""
    recommendations = {
        "sunny": {
            "happy": "Go for a walk in the park and enjoy the sunshine.",
            "calm": "Find a quiet spot outdoors to read a book.",
            "energetic": "Try a hike in a nearby forest or trail.",
            "stressed": "Meditate outdoors in a peaceful natural setting."
        },
        "cloudy": {
            "happy": "Explore a botanical garden or a nature reserve.",
            "calm": "Visit a lake or river for some quiet contemplation.",
            "energetic": "Go for a brisk walk or a bike ride.",
            "stressed": "Listen to the sounds of nature from a sheltered spot."
        },
        "rainy": {
            "happy": "Visit a covered outdoor market or a scenic viewpoint with shelter.",
            "calm": "Enjoy the sound of rain from your balcony or a cozy cafe with a view.",
            "energetic": "Go for a run with appropriate rain gear.",
            "stressed": "Watch the rain from indoors, focusing on its calming effect."
        }
    }

    # Basic AI logic: map inputs to a recommendation
    # In a real app, this would involve more complex models and data
    weather = weather.lower()
    mood = mood.lower()

    if weather in recommendations and mood in recommendations[weather]:
        return recommendations[weather][mood]
    else:
        return "Enjoy some time outdoors, whatever the weather and your mood!"

if __name__ == "__main__":
    print("Welcome to Wander's AI Recommendation!")
    print("Let's help you connect with nature.")

    user_weather = input("What's the weather like today? (sunny, cloudy, rainy): ")
    user_mood = input("How are you feeling? (happy, calm, energetic, stressed): ")

    recommendation = get_ai_recommendation(user_weather, user_mood)

    print("\nBased on your input, our AI suggests:")
    print(f"-> {recommendation}")
    print("\nHave a wonderful time outdoors!")
