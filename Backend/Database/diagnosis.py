from database.supabase import supabase


def save_test_diagnosis():
    data = {
        "image_url": "test_image.jpg",
        "description": "Brown spots on rice leaves",
        "latitude": 12.34,
        "longitude": 56.78,
        "predicted_disease": "Rice Blast",
        "confidence": 0.90
    }

    result = supabase.table("diagnoses").insert(data).execute()
    return result