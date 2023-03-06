import jwt

from datetime import datetime, timedelta

def decode_jwt(request):
    token = request.META.get("HTTP_AUTHORIZATION").split()[1]
    user_info = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
    return user_info

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
