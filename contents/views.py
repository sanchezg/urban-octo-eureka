from django.http import Http404
from django.shortcuts import render

from .models import Content


def index(request):
    contents = Content.objects.order_by("-created_at")[:5]
    context = {
        "contents_list": contents,
    }
    # output = f"These are the latest 5 contents: {[x.name for x in contents]}"
    return render(request, "contents/index.html", context)


def detail(request, content_id):
    try:
        content = Content.objects.get(pk=content_id)
    except Content.DoesNotExist:
        raise Http404("Specified content does not exist")
    return render(request, "contents/details.html", {"content": content})
