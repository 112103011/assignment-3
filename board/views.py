from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Comment
import json

@require_http_methods(["GET"])
def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    data = [{"id": c.id, "name": c.name, "text": c.text, "created_at": c.created_at.strftime("%Y-%m-%d %H:%M:%S")} for c in comments]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def post_comment(request):
    name = request.POST.get("name")
    text = request.POST.get("text")
    if name and text:
        comment = Comment.objects.create(name=name, text=text)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

def index(request):
    return render(request, "board/index.html")
