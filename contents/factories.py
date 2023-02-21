import factory
from factory.django import DjangoModelFactory

from .models import Content, Kit, KitContent, ContentTag, Bookmark, ContentType, ContentTagColor
from users.factories import UserFactory, SellerUserFactory


class ContentFactory(DjangoModelFactory):
    class Meta:
        model = Content

    user = factory.SubFactory(SellerUserFactory)
    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text", max_nb_chars=256)
    is_free = factory.Faker("boolean")
    content_type = factory.Faker("random_element", elements=[choice[0] for choice in ContentType.CHOICES])


class KitFactory(DjangoModelFactory):
    class Meta:
        model = Kit

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text", max_nb_chars=256)


class KitContentFactory(DjangoModelFactory):
    class Meta:
        model = KitContent

    kit = factory.SubFactory(KitFactory)
    content = factory.SubFactory(ContentFactory)


class ContentTagFactory(DjangoModelFactory):
    class Meta:
        model = ContentTag

    name = factory.Faker("word")
    color = factory.Faker("random_element", elements=[choice[0] for choice in ContentTagColor.CHOICES])


class BookmarkFactory(DjangoModelFactory):
    class Meta:
        model = Bookmark

    content = factory.SubFactory(ContentFactory)
    user = factory.SubFactory(UserFactory)
