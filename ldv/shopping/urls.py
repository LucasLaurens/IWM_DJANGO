from django.urls import path
from shopping.views import Index, Details

urlpatterns = [
    path("", Index.as_view()),
    path("<int:id>", Details.as_view()),
]