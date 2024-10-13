from django.urls import path
from . import views
from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('movies/',views.movielistview, name='movie_list'),
    path('collection/',views.create_collection,name='create_collection'),
    path('collection/<collection_uuid>/',views.list_collections,name="list_collections"),
    path('collection/<uuid:collection_uuid>/',views.update_collection,name="update_collections"),
    path('collection/<uuid:collection_uuid>/',views.delete_collection,name="delete_collection"),
    path('request-count/',views.get_count,name="get_count"),
    path('reset-count/',views.reset_count,name="reset_count"),
]
