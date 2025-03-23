from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serilaizers import *
from manager.models import *
from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import UploadedFile
from PIL import Image
# Create your views here.


class PortfolioView(APIView):
    def get(self, request):
        try:
            portfolio = Portfolio.objects.all()
            return Response(
                {"message": "portfolio retrieved successfully", "data": PortfolioSerializer(portfolio, many=True).data},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "failed to retrieve portfolio", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientView(APIView):
    def get(self, request):
        try:
            clients = Client.objects.all()
            return Response(
                {"message": "clients retrieved successfully", "data": ClientSerializer(clients, many=True).data},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "failed to retrieve clients", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FAQView(APIView):
    def get(self, request):
        try:
            faqs = FAQ.objects.all()
            return Response({
                "message": "FAQs retrieved successfully",
                "data": FAQSerializer(faqs, many=True).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "failed to retrieve clients", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReviewView(APIView):
    def post(self, request):
        data = request.data
        missing_fields = [field for field in ['name', 'comment'] if not data.get(field)]
        if missing_fields:
            return Response({"error": f"Missing required fields: {', '.join(missing_fields)}"},
                            status=status.HTTP_400_BAD_REQUEST)

        image = data.get('image')
        if not image or not isinstance(image, UploadedFile):
            return Response({"error": "Invalid image file"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            img = Image.open(image)
            img.verify()  # Validate the image format
        except Exception:
            return Response({"error": "Uploaded file is not a valid image."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            review = Review.objects.create(name=data.get('name'), image=image, comment=data.get('comment'))
            return Response({
                "message": "Review uploaded successfully",
                "data": ReviewSerializer(review).data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "Failed to upload review",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            reviews = Review.objects.order_by('-id')[:5]
            return Response({
                "message": "Reviews retrieved successfully",
                "data": ReviewSerializer(reviews, many=True).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to retrieve reviews",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientImagesVIew(APIView):
    def get(self, request, id):
        try:
            client = get_object_or_404(Client, pk=id),
            images = ClientImage.objects.filter(client=id)
            return Response({
                "message": "Images retrieved successfully",
                "images": ClientImageSerializer(images, many=True).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message":"Failed to get images",
                "error":str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HomeView(APIView):
    def get(self, request):
        try:
            home = Home.objects.first()
            return Response({
                "message":"Home details fetched successfully",
                "data":HomeSerializer(home).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message":"error fetching home details",
                "error":str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AboutView(APIView):
    def get(self, request):
        print("dog")
        try:
            about = About.objects.first()
            print(about.top_image.url)
            return Response({
                "message":"About details retrieved successfully",
                "data":AboutSerializer(about).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message":"Error retrieving about details",
                "error":str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

