import factory
from factory.django import DjangoModelFactory

from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = (
            "username",
            "email",
        )

    username = factory.Sequence(lambda n: f"fakeusername{n}")
    email = factory.Sequence(lambda n: f"fakeemail{n}@email.com")
    first_name = "John"
    last_name = "Rambo"


class SellerUserFactory(UserFactory):
    is_seller = True
