from rest_framework import filters
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import ClassQatagon
from .serializer import QatagonSerializerList, QatagonSerializerDetail

# Create your views here.

# http://127.0.0.1:8000/api/create/ yaratish


class CusListAPIView(ListAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerList
    filter_backends = [filters.SearchFilter]
    search_fields = ['toliq_ism']

    def get_queryset(self):
        queryset = ClassQatagon.objects.all()

        tugilgan_sana = self.request.query_params.get('tugilgan_sana')

        if tugilgan_sana:
            queryset = queryset.filter(tugilgan_sana__gte=tugilgan_sana)

        return queryset


class CusDetailAPIView(RetrieveAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'


class CusCreateAPIView(CreateAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'


class CusUpdateAPIView(UpdateAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'


class CusDestroyAPIView(DestroyAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'
