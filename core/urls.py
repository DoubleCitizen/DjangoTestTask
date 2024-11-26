from django.urls import path

from . import views

urlpatterns = [
    path('car/create', views.CarCreateView.as_view(), name='create_car'),
    path('car/list', views.CarListView.as_view(), name='list_car'),
    path('car/<pk>', views.CarView.as_view(), name='retrieve_car'),
    path('car/<pk>/update', views.CarUpdateView.as_view(), name='update_car'),
    path('car/<pk>/delete', views.CarDeleteView.as_view(), name='delete_car'),
    path('comment/create', views.CommentCreateView.as_view(), name='create_car'),
    path('comment/list', views.CommentListView.as_view(), name='comment_car'),
    path('comment/<pk>', views.CommentView.as_view(), name='comment_car'),
    path('comment/<pk>/update', views.CommentUpdateView.as_view(), name='comment_car'),
    path('comment/<pk>/delete', views.CommentDeleteView.as_view(), name='comment_car'),
]