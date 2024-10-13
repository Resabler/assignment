from django.urls import path, include

urlpatterns = [
    path('collections/', include('collection.urls')),
     path('', include('collection.urls')),
]
