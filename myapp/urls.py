# from django.urls import path
# from . import views

# urlpatterns = [
#     path('hello-world/', views.hello_world, name='hello_world'),
#         path('get-data/', views.get_data, name='get_data'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet

router = DefaultRouter()
router.register(r'tests', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


