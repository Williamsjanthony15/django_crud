from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackDeleteView, SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='listView'),
    path('new/', SnackCreateView.as_view(), name='createView'),
    path('<int:pk>', SnackDetailView.as_view(), name='detailView'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='updateView'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='deleteView'),
]
