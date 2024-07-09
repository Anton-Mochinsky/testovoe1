from rest_framework import serializers
from .models import Bike, Rental, UserHistory
from myproject.myapp.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['bike_id', 'bike_name', 'status']


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['rental_id', 'user', 'bike', 'start_time', 'end_time', 'cost']


class ReturnBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['rental_id', 'end_time']

    def update(self, instance, validated_data):
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.cost = (instance.end_time - instance.start_time).seconds // 3600 * 10  # Пример расчета стоимости аренды
        instance.save()
        return instance


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['history_id', 'user', 'rental']