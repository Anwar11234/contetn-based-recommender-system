import requests

# Replace with the URL where your FastAPI app is running
API_URL = "https://anwar101-recommendation-api.hf.space/recommendations"

# Test case 1: Existing course
course_data = {"title": "Introduction to Artificial Intelligence"}
response = requests.post(API_URL, json=course_data)

# Check for successful response
if response.status_code == 200:
  print("Recommendations for", course_data["title"], ":")
  print(response.json())
else:
  print("Error:", response.status_code)