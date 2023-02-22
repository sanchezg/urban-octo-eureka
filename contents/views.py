from django.shortcuts import get_object_or_404, render

from .models import Content


def index(request):
    contents = Content.objects.order_by("-created_at")[:5]
    context = {
        "contents_list": contents,
    }
    return render(request, "contents/index.html", context)


def detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, "contents/details.html", {"content": content})
