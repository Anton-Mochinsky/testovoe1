from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('bikes/', views.BikeList.as_view(), name='bike_list'),
    path('rent/', views.RentBike.as_view(), name='rent_bike'),
    path('return/<int:rental_id>/', views.ReturnBike.as_view(), name='return_bike'),
    path('user/history/', views.UserHistoryList.as_view(), name='user_history'),
]