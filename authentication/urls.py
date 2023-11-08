from django.urls import path
from . import views
from .views import ResultAPIView

urlpatterns = [
    path('signup',views.Signup.as_view(),name='signup' ),
    path('activate/<uid64>/<token>',views.activate, name="activate"),
    path('logout',views.LogoutView.as_view(),name='logout' ),
    path('result/', ResultAPIView.as_view(), name='result-api'),












]