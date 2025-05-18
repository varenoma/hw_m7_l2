from django.urls import reverse
from rest_framework import serializers

from .models import ClassQatagon


class QatagonSerializerList(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    update_url = serializers.SerializerMethodField()
    delete_url = serializers.SerializerMethodField()

    class Meta:
        model = ClassQatagon
        fields = ['id', 'toliq_ism', 'detail_url', 'update_url', 'delete_url']

    def urls_def(self, obj, view_name):
        request = self.context.get('request')
        url = reverse(view_name, kwargs={'slug': obj.slug})
        return request.build_absolute_uri(url)

    def get_detail_url(self, obj):
        return self.urls_def(obj, "detail")

    def get_update_url(self, obj):
        return self.urls_def(obj, "update")

    def get_delete_url(self, obj):
        return self.urls_def(obj, "delete")


class QatagonSerializerDetail(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ClassQatagon
        fields = '__all__'
