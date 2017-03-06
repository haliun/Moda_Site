from django.utils import timezone
from haystack import indexes
from moda.models import Clothes
import datetime
class ClothesIndex(indexes.SearchIndex, indexes.Indexable):
    text=indexes.CharField(document=True, use_template=True)
    clothes_name=indexes.CharField(model_attr='clothes_name')
    clothes_description=indexes.CharField(model_attr='clothes_description')
    clothes_brand=indexes.CharField(model_attr='clothes_brand')
    clothes_dateupload=indexes.DateTimeField(model_attr='clothes_dateupload', null=True)

    def get_model(self):
        return Clothes

    def index_queryset(self, using=None):
        return self.get_model().objects.all()