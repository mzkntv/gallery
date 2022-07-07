from rest_framework import routers

from . import views

app_name = 'app'

router = routers.SimpleRouter()
router.register(r'images', views.PictureViewSet, 'image')

urlpatterns = []
urlpatterns += router.urls
