# coding=utf8
import django_filters
from models import *


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['price', 'release_date']