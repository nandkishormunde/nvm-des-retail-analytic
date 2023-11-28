import requests

VAULT_URL = "http://127.0.0.1:8200"
ROLE_ID = "e6b26f7f-996f-da00-625a-839106348aad"
SECRET_ID = "c207c3bf-e018-da98-5546-df256ce7160e"
SECRET_PATH = "secret/data/snow"

def authenticate_with_approle():
        auth_url = f"{VAULT_URL}/v1/auth/approle/login"
        auth_data = {
            "role_id": ROLE_ID,
            "secret_id": SECRET_ID
        }
        try:
            auth_response = requests.post(auth_url, json=auth_data)
            auth_response.raise_for_status()

            token = auth_response.json()["auth"]["client_token"]
            print("token=======", token)
            return token

        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")
            return None

def get_secret( token):
        headers = {
            "X-Vault-Token": token,
        }

        url = f"{VAULT_URL}/v1/{SECRET_PATH}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            secret_data = response.json()["data"]
            return secret_data

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving secret: {e}")
            return None

token = authenticate_with_approle()
secret_data = get_secret(token)
print(secret_data)