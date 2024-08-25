# Curelink-Assignment
Overview
This project uses the Hugging Face API to generate responses to patient queries based on their diet chart and medical conditions. The goal is to provide personalized dietary advice to patients with Polycystic Ovary Syndrome (PCOS).
Features
Loads patient queries from a JSON file
Extracts relevant information from the diet chart and medical profile
Generates responses using the Hugging Face API
Saves responses to a new JSON file
Requirements
Python 3.8+
requests library
Hugging Face API key
Usage
Clone the repository:
Install dependencies: pip install requests
Replace API_URL and headers in main.py with your Hugging Face API key
Run the script: python main.py
Input JSON File
The input JSON file should have the following structure:
JSON
[
    {
        "ticket_id": "12345",
        "latest_query": "What should I eat for breakfast?",
        "profile_context": {
            "patient_profile": "Age - 25\nPatient Preferences - Veg\n",
            "diet_chart": {
                "id": 42470,
                "updated_at": "2024-06-13T06:58:28.664932Z",
                "start_date": "2024-06-14T04:44:45Z",
                "notes": "<ul><li>Eat less salt Increase food like- green leafy vegetables, whole grains, nuts etc.</li><li>Add short and frequent meals, chew food properly.</li><li>Walking post meals (post lunch and dinner after 20mins for 15-17mins)</li></ul><p>Seed cycle- 1 tbsp sunflower seeds + sesame seeds/ 1 tbsp flax seeds + pumpkin seeds - (Practice seed cycling – 4 types of seeds are included in it- pumpkin seeds, flax seeds, sesame seeds and sunflower seeds. Starting from your day of menses to day 14th have pumpkin &amp; flax seeds for the estrogen boost and from day 14 to 28th day your menses start having sesame + sunflower seeds for the progesterone boost.)</p><p>Please check and share empty stomach weight on the last day of your diet chart </p>",
                "hindi_notes": "",
                "language": "en-us",
                "created_by_id": "b9748b68-f7c3-4161-aec3-0ba9c8baa6b1",
                "diet_chart_template_id": 3188,
                "meals": null,
                "is_draft_template": false,
                "meals_by_days": {
                    "0": {
                        "day": "Monday",
                        "time": "08:00",
                        "description": "Oatmeal with fruits"
                    },
                    "1": {
                        "day": "Tuesday",
                        "time": "08:00",
                        "description": "Greek yogurt with nuts"
                    }
                },
                "diet_chart_url": "https://clchatagentassessment.s3.ap-south-1.amazonaws.com/42470_8c91-9810039676ee_CL.pdf"
            }
        }
    }
]
Output JSON File
The output JSON file will have the following structure:
JSON
[
    {
        "ticket_id": "12345",
        "latest_query": "What should I eat for breakfast?",
        "generated_response": "You can have oatmeal with fruits for breakfast.",
        "ideal_response": "This part needs to be determined based on the actual comparison."
    }
]
