import requests


url = "http://127.0.0.1:5000/api/users"


# =========================
# POST - Create
# =========================

user = {
    "username": "Sanjay",
    "skill": "Python"
}

response = requests.post(url, json=user)

print("\n===== POST =====")
print("Status:", response.status_code)
print("Response:", response.json())


# =========================
# PUT - Update
# =========================

update_url = "http://127.0.0.1:5000/api/users/Sanjay"

update_data = {
    "skill": "Python + Django"
}

response = requests.put(update_url, json=update_data)

print("\n===== PUT =====")
print("Status:", response.status_code)
print("Response:", response.json())


# =========================
# GET - Read
# =========================

response = requests.get(url)

print("\n===== GET =====")
print("Status:", response.status_code)
print("Response:", response.json())


# =========================
# DELETE - Delete
# =========================

delete_url = "http://127.0.0.1:5000/api/users/Sanjay"

response = requests.delete(delete_url)

print("\n===== DELETE =====")
print("Status:", response.status_code)

if response.headers.get("Content-Type", "").startswith("application/json"):
    print("Response:", response.json())
else:
    print("Response:", response.text)


# =========================
# GET after DELETE
# =========================

response = requests.get(url)

print("\n===== GET AFTER DELETE =====")
print("Status:", response.status_code)
print("Response:", response.json())