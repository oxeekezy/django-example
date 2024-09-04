from merch.models import Categories
from django import template

register = template.Library()


# Шаблонный тег для получения категорий
@register.simple_tag()
def categories_tag():
    return Categories.objects.all()
