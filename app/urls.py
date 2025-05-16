from django.urls import path
from app.views import CusCreateAPIView, CusListAPIView, CusDetailAPIView, CusUpdateAPIView, CusDestroyAPIView


urlpatterns = [
    path('list/<slug:slug>/delete', CusDestroyAPIView.as_view(), name='delete'),
    path('list/<slug:slug>/update', CusUpdateAPIView.as_view(), name='update'),
    path('create/', CusCreateAPIView.as_view(), name='create'),
    path('list/', CusListAPIView.as_view(), name='list'),
    path('list/<slug:slug>/detail', CusDetailAPIView.as_view(), name='detail'),
]
