import requests

response = requests.get("http://localhost:8080")
print("Response Code:", response.status_code)
print("Response Content:", response.text[:200])  # Print first 200 characters
