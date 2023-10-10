from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from magazine.models import Magazine, Rating
from magazine.serializers import MagazineSerializer, RatingSerializer


class MagazineList(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        magazine_id = self.request.data.get('magazine')
        existing_rating = Rating.objects.filter(user=user, magazine_id=magazine_id).first()

        if existing_rating:
            # If the user has already rated this magazine, update the existing rating.
            existing_rating.rating = serializer.validated_data['rating']
            existing_rating.save()
        else:
            # If the user hasn't rated this magazine before, create a new rating.
            serializer.save(user=user)
