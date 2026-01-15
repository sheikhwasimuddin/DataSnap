from firebase import Firebase
import jwt

config = {
  "apiKey": "AIzaSyAc7MIazEXzi7EIkygP--ik13T-i1DcHHI",
  "authDomain": "forms-6e835.firebaseapp.com",
  "databaseURL": "https://forms-6e835-default-rtdb.firebaseio.com",
  "projectId": "forms-6e835",
  "storageBucket": "forms-6e835.appspot.com",
  "messagingSenderId": "361932182221",
  "appId": "1:361932182221:web:ca1436672474e601fb4f84"
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
