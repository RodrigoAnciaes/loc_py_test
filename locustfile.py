from locust import HttpUser, task, between
import os
from dotenv import load_dotenv

# Open the .env file
load_dotenv(override=True)

# Retrieve the endpoint from the environment variable and ensure it includes the scheme
API_ENDPOINT = os.getenv("API_ENDPOINT")
if not API_ENDPOINT.startswith("http"):
    API_ENDPOINT = f"http://{API_ENDPOINT}"
else:
    API_ENDPOINT = f"{API_ENDPOINT}"

class ApiUser(HttpUser):
    # The endpoint is set in the environment variable, including the scheme
    host = API_ENDPOINT
    wait_time = between(1, 5)  # Simulate wait time between tasks

    @task(1)
    def get_users(self):
        self.client.get("/")
