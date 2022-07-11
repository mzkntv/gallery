from rest_framework import routers

from . import views

app_name = 'user'

router = routers.SimpleRouter()
router.register(r'register', views.RegisterView, 'register')

urlpatterns = []
urlpatterns += router.urls
