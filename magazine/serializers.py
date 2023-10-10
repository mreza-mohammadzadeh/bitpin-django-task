from rest_framework import serializers
from .models import Magazine, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'rating', 'magazine')


class MagazineSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    user_rating = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    class Meta:
        model = Magazine
        fields = ('id', 'title', 'description', 'average_rating', 'user_rating', 'total_rating')

    def get_user_rating(self, obj):
        user = self.context['request'].user
        rating = obj.ratings.filter(user=user).first()
        return rating.rating if rating else None

    def get_total_rating(self, obj):
        return obj.ratings.count()

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(magazine=obj)
        if ratings.count() > 0:
            total_ratings = sum([rating.rating for rating in ratings])
            return total_ratings / ratings.count()
        else:
            return 0
