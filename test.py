import os
from firebase import Firebase
import jwt
from dotenv import load_dotenv
load_dotenv()

config = {
  "apiKey": os.environ.get("FIREBASE_APIKEY"),
  "authDomain": os.environ.get("FIREBASE_AUTHDOMAIN"),
  "databaseURL": os.environ.get("FIREBASE_DATABASEURL"),
  "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
  "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
  "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
  "appId": os.environ.get("FIREBASE_APP_ID"),
  "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
  }
firebase = Firebase(config)
auth = firebase.auth()

# Login user
user = auth.sign_in_with_email_and_password("test@gmail.com", "123456")
token = user['idToken']

# Decode token (optional)
payload = jwt.decode(token, options={"verify_signature": False})
print(payload["email"])

# Check verified
info = auth.get_account_info(token)
print(info["users"][0]["emailVerified"])
