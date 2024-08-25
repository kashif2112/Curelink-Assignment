import requests
import json
from datetime import datetime
from typing import Dict, List

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {"Authorization": "Bearer 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"}

def query_huggingface_api(prompt: str) -> Dict:
    """Query the Hugging Face model with the given prompt."""
    data = {"inputs": prompt}
    max_retries = 3
    for i in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=data)
            response.raise_for_status()
            return response.json()[0]
        except requests.RequestException as e:
            print(f"Request error: {e}")
            if i < max_retries - 1:
                time.sleep(1)  # Wait for 1 second before retrying
            else:
                return {}

def load_queries(url: str) -> List[Dict]:
    """Load queries from a JSON file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return []

def extract_ideal_meal(diet_chart: Dict, day: str, time: str) -> str:
    """Extract the ideal meal from the diet chart based on the day and time."""
    if diet_chart and 'meals_by_days' in diet_chart:
        for meal in diet_chart['meals_by_days'].values():
            if meal['day'] == day and meal['time'] == time:
                return meal['description']
    return "Ideal meal not found."

def generate_meal_response(latest_query: str, diet_chart: Dict, medical_profile: str) -> str:
    """Generate a response using the Hugging Face model."""
    current_time = datetime.now()
    day = current_time.strftime('%A')
    time = current_time.strftime('%H:%M')
    
    ideal_meal = extract_ideal_meal(diet_chart, day, time)
    
    prompt = f"""
    Patient Profile: {medical_profile}
    Ideal Meal: {ideal_meal}
    Latest Query: {latest_query}
    Based on the patient's diet chart and medical conditions, provide a concise response to the patient's latest query in the same messaging style they used.
    """
    
    response = query_huggingface_api(prompt)
    return response.get('generated_text', '').strip()

def process_queries(queries: List[Dict]) -> List[Dict]:
    """Process each query and generate responses."""
    responses = []
    for query in queries:
        ticket_id = query.get('ticket_id', 'N/A')
        latest_query = query.get('latest_query', 'No query provided')
        patient_profile = query.get('profile_context', {}).get('patient_profile', "")
        diet_chart = query.get('diet_chart', {})
        medical_profile = patient_profile
        
        generated_response = generate_meal_response(latest_query, diet_chart, medical_profile)
        ideal_response = "This part needs to be determined based on the actual comparison."
        
        responses.append({
            "ticket_id": ticket_id,
            "latest_query": latest_query,
            "generated_response": generated_response,
            "ideal_response": ideal_response
        })
    
    return responses

def save_responses_to_json(responses: List[Dict], filename: str) -> None:
    """Save the responses to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(responses, file, indent=4)

def main() -> None:
    """Main entry point of the script."""
    url = 'https://clchatagentassessment.s3.ap-south-1.amazonaws.com/queries.json'
    queries = load_queries(url)
    
    responses = process_queries(queries)
    
    save_responses_to_json(responses, "output1.json")

if __name__ == "__main__":
    main()
