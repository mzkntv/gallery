from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

api_urls = [
    path('auth/', views.obtain_auth_token),
    path('app/', include('app.urls', namespace='app')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urls, 'gallery'), namespace='api'))
]
