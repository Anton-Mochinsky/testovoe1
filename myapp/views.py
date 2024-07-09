from rest_framework.views import APIView
from .models import Bike
from .serializers import BikeSerializer
from rest_framework import status
from myproject.myapp.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from datetime import datetime
from .models import Bike, Rental
from .serializers import RentalSerializer
from .serializers import ReturnBikeSerializer
from .models import UserHistory
from .serializers import UserHistorySerializer

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response(serializer.errors, status=400)


class BikeList(APIView):
    def get(self, request):
        bikes = Bike.objects.filter(status='available')
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)


class RentBike(APIView):
    def post(self, request):
        user = request.user
        rented_bike = user.rental_set.all().filter(end_time=None).first()

        if rented_bike:
            return Response({'error': 'You have already rented a bike'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        bike_id = data.get('bike_id')
        bike = Bike.objects.get(bike_id=bike_id)

        if bike.status == 'rented':
            return Response({'error': 'The bike is already rented'}, status=status.HTTP_400_BAD_REQUEST)

        rental = Rental(user=user, bike=bike, start_time=datetime.now())
        rental.save()
        bike.status = 'rented'
        bike.save()

        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReturnBike(APIView):
    def put(self, request, rental_id):
        rental = Rental.objects.get(rental_id=rental_id)
        serializer = ReturnBikeSerializer(rental, data=request.data)

        if serializer.is_valid():
            rented_bike = rental.bike
            rented_bike.status = 'available'
            rented_bike.save()

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserHistoryList(APIView):
    def get(self, request):
        user = request.user
        user_history = UserHistory.objects.filter(user=user)
        serializer = UserHistorySerializer(user_history, many=True)
        return Response(serializer.data)