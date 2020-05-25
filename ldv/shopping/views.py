from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from shopping.models import Clothes

# Create your views here.

class Index(TemplateView):
    """
        Index View
    """

    template_name = "shopping/index.html"

    def get(self, request, *args, **kwargs):
        clothes = Clothes.objects.all()
        return render(request, self.template_name, {'test_var': 42, 'clothes': clothes})


class Details(TemplateView):
    """
        Details View
    """

    template_name = "shopping/details.html"

    def get(self, request, id, *args, **kwargs):
        clothe = get_object_or_404(Clothes, id=id)
        return render(request, self.template_name, {'clothe': clothe})
