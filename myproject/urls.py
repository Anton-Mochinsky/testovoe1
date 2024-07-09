from django.contrib import admin
from django.urls import path
from myproject.myapp.views import RegisterUser, CustomTokenObtainPairView, BikeList, RentBike, ReturnBike, UserHistoryList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUser.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('bikes/', BikeList.as_view(), name='bike_list'),
    path('rent/', RentBike.as_view(), name='rent_bike'),
    path('return/<int:rental_id>/', ReturnBike.as_view(), name='return_bike'),
    path('user/history/', UserHistoryList.as_view(), name='user_history'),
]
