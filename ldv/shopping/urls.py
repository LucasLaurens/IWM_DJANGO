from django.urls import path

from shopping.views import Index, Details, Basket, Login, Logout


urlpatterns = [
    path("", Index.as_view(), name="shop"),
    path("<int:id>", Details.as_view(), name="details"),
    path("basket", Basket.as_view(), name="basket"),

    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
]