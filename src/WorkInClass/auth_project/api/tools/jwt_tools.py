import jwt

from datetime import datetime, timedelta

@staticmethod
def generate_jwt(user, refresh=False):
    if refresh:    
        jwt_payload = {
            "user_id": user.id,
            "email": user.user.email,
            "first_name": user.user.first_name,
            "last_name": user.user.last_name,
            "expiration": str(datetime.utcnow() + timedelta(hours=3)),
            "issued_at_time": str(datetime.utcnow()),
        }
    else:
        jwt_payload = {
            "user_id": user.id,
            "email": user.user.email,
            "first_name": user.user.first_name,
            "last_name": user.user.last_name,
            "expiration": str(datetime.utcnow() + timedelta(hours=1)),
            "issued_at_time": str(datetime.utcnow()),
        }
    jwt_token = jwt.encode(jwt_payload, "SECRET_KEY", algorithm="HS256")
    return jwt_token