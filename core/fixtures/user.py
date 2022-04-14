from core.user.models import User


data_user = {
    "email": "testuser@yopmail.com",
    "password": "12345678",
    "username": "testuser",
    "id":"1"
}

User.objects.create_user(**data_user)
