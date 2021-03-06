from django.apps import apps
from django.contrib import admin

from shopping.models import Clothes, User, Item

# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('user_permissions', 'groups')
    inlines = (ItemInline,)

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('name', 'price')
    search_fields = ('name', 'price')

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass