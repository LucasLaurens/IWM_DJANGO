from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


from shopping.models import Clothes, Item, User

# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    """
        Index View
    """

    template_name = "shopping/shop.html"

    def get(self, request, *args, **kwargs):
        clothes = Clothes.objects.all()
        return render(request, self.template_name, {'test_var': 42, 'clothes': clothes})


class Details(LoginRequiredMixin, TemplateView):
    """
        Details View
    """

    template_name = "shopping/details.html"

    def get(self, request, id, *args, **kwargs):
        clothe = get_object_or_404(Clothes, id=id)
        Item.objects.create(user=request.user, clothe=clothe)
        # user = request.user
        # user.clothes.add(clothe)
        # user.items.add(clothe)
        # save an item
        # user.save()
        return render(request, self.template_name, {'clothe': clothe})


class Basket(LoginRequiredMixin, TemplateView):
    """
        Display basket items for a specific user
    """

    template_name = "shopping/basket.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                        {'items': request.user.items.all()})