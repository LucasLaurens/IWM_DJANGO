from django.urls import path
from shopping.views import Index, Details, Basket
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("<int:id>", Details.as_view(), name="detail"),
    path("basket", Basket.as_view(), name="basket"),
    path("", Index.as_view(), name="shop"),
]