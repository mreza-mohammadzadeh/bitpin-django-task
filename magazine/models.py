from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from user.models import User


class Magazine(models.Model):
    user = models.ForeignKey(User, related_name='magazine', on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    description = models.TextField()

    @staticmethod
    def mag_create(request):
        return Magazine.objects.create(title=request.data['title'], description=request.data['description'],
                                       user=request.user)


class Rating(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
