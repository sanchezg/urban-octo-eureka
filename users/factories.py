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

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.set_password(extracted)
        return self.password


class SellerUserFactory(UserFactory):
    is_seller = True
