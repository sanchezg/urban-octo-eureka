from django.http import HttpResponse

from .models import Content


def index(request):
    contents = Content.objects.order_by("-created_at")[:5]
    output = f"These are the latest 5 contents: {[x.name for x in contents]}"
    return HttpResponse(output)
