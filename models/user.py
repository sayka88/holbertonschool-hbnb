#!/usr/bin/python3

"""Import BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creating User Classs"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password')
        )

        user.id = data.get('id', str(uuid.uuid4()))
        user.created_at = datetime.fromisoformat(
            data.get('created_at', datetime.now().isoformat())
        )
        user.updated_at = datetime.fromisoformat(
            data.get('updated_at', datetime.now().isoformat())
        )
        return user
