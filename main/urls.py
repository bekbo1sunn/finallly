from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CountryViewSet, 
                    CategoryViewSet, 
                    TiketViewSet, 
                    CategoryListCreateAPIView, 
                    CountryListAPIView, 
                    TiketListAPIView, 
                    CategoryTiketsViewSet, 
                    BankCardViewSet
                    )


router = DefaultRouter()
router.register("countrys", CountryViewSet)
router.register("category", CategoryViewSet)
router.register("tikets", TiketViewSet)
router.register("category_tikets", CategoryTiketsViewSet)
router.register("bank_card", BankCardViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("category/list/", CategoryListCreateAPIView.as_view()),
    path("country/list/", CountryListAPIView.as_view()),
    path("tiket/list/", TiketListAPIView.as_view()),
]