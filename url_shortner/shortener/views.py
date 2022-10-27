from django.http.response import JsonResponse, HttpResponseBadRequest
from shortener.serializers import UrlSerializer
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from .models import Url
from rest_framework import status
import uuid


@api_view(["POST"])
def create(request):
    url_serializer = UrlSerializer(data=request.data)
    if url_serializer.is_valid():
        uuid_str = str(uuid.uuid4())[:5]
        url_serializer.save(uuid=uuid_str)
        return JsonResponse(
            {"success": True, "result": request.build_absolute_uri(f"/{uuid_str}")},
            status=status.HTTP_201_CREATED,
        )
    return JsonResponse(
        {"success": False, "error": "URL is not valid"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET"])
def get(request, uuid):
    try:
        url_details = Url.objects.get(uuid=uuid)
    except Url.DoesNotExist:
        return HttpResponseBadRequest()
    return redirect(url_details.link)
