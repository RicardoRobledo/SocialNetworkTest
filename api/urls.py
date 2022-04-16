from django.urls import path
from .views import GruposViewSet
from rest_framework.routers import SimpleRouter


'''
urlpatterns = [
    path('', GruposViewSet.as_view(), name='home'),
]
'''


router = SimpleRouter()
router.register('grupos/', GruposViewSet, basename='grupos')

urlpatterns = router.urls