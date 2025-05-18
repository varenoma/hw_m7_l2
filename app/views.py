from rest_framework import filters
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from .models import ClassQatagon
from .serializer import QatagonSerializerList, QatagonSerializerDetail

# Create your views here.

# http://127.0.0.1:8000/api/create/ yaratish


class IsOwnerOrSuperUserForEdit(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user or request.user.is_superuser


class CusListAPIView(ListAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerList
    filter_backends = [filters.SearchFilter]
    search_fields = ['toliq_ism']
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]


class CusCreateAPIView(CreateAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CusUpdateAPIView(UpdateAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrSuperUserForEdit]


class CusDestroyAPIView(DestroyAPIView):
    queryset = ClassQatagon.objects.all()
    serializer_class = QatagonSerializerDetail
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrSuperUserForEdit]
