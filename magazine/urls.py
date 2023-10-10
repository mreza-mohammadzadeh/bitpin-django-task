from django.urls import path

from magazine.views import MagazineList, RatingCreate

urlpatterns = [
    path('magazines', MagazineList.as_view(), name='magazine-list'),
    path('ratings', RatingCreate.as_view(), name='rating-create'),
]
