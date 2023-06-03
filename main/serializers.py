from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Country, Category, Tiket, CategoryTikets, BankCard
from review.serializers import CommentSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = instance.average_rating
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True, context=self.context).data
        return rep 


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class TiketSerializer(serializers.ModelSerializer):
    arrival = serializers.CharField(source='arrival.title')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Tiket
        fields = ['id', 'flight_name', 'departure_date', 'arrival_date', 'price', 'flight_time', 'quantity', 'category', 'arrival', ]


class CategoryTiketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTikets
        fields = ['id', 'name', 'baggage', 'hand_luggage', 'nutrtion', 'exchange_return', 'preferred_seat_selection', 'business_lounge', 'separate_landing', 'separate_reception_desk']



class BankCardSerializer(ModelSerializer):
    class Meta:
        model = BankCard
        fields = '__all__'