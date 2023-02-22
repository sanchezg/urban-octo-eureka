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

    email = factory.Faker("email")
    username = factory.Sequence(lambda n: f"fakeuser_{n}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class SellerUserFactory(UserFactory):
    is_seller = True
