from rest_framework import serializers
from manager.models import *

class PortfolioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Portfolio
        fields = ['id','category','image','image_url']

    def get_image_url(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/dd7laegor/{obj.image}"
        return None

class ReviewSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['id','name','image','comment','image_url']

    def get_image_url(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/dd7laegor/{obj.image}"
        return None


class ClientImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ClientImage
        fields = ['id', 'client', 'image', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/dd7laegor/{obj.image}"
        return None


class ClientSerializer(serializers.ModelSerializer):
    images = ClientImageSerializer(many=True, read_only=True)  # Nested images

    class Meta:
        model = Client
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()
    image_4 = serializers.SerializerMethodField()
    image_5 = serializers.SerializerMethodField()
    image_6 = serializers.SerializerMethodField()
    image_7 = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = ['text', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7']

    def get_image_url(self, obj, image_field):
        image = getattr(obj, image_field)
        return image.url if image else None

    def get_image_1(self, obj):
        return self.get_image_url(obj, "image_1")

    def get_image_2(self, obj):
        return self.get_image_url(obj, "image_2")

    def get_image_3(self, obj):
        return self.get_image_url(obj, "image_3")

    def get_image_4(self, obj):
        return self.get_image_url(obj, "image_4")

    def get_image_5(self, obj):
        return self.get_image_url(obj, "image_5")

    def get_image_6(self, obj):
        return self.get_image_url(obj, "image_6")

    def get_image_7(self, obj):
        return self.get_image_url(obj, "image_7")

class AboutSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = ['text','image','image_url']
    def get_image_url(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/dd7laegor/{obj.image}"
        return None