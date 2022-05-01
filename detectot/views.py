from rest_framework.views import APIView
from django.http import JsonResponse

from .TFmodel import MLPredict
from PIL import Image
# upload image for process ML model


class UserUpload(APIView):
    def post(self, request, format=None):
        UploadedImg = request.data['Upload']
        img = Image.open(UploadedImg)
        result = MLPredict(img)

        return JsonResponse({"Detection Result": result}, status=200)
