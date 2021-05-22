from rest_framework.serializers import ModelSerializer
from bboard.models import Bb


class BbSerializer(ModelSerializer):
    class Meta:
        model = Bb
        exclude = ('published',)
