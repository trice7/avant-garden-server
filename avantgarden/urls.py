"""avantgarden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from avantgardenapi.views import GardenPlantView, GardenView, PlantTypeView, PlantView, register_user, check_user, CommentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gardens', GardenView, 'garden')
router.register(r'garden_plants', GardenPlantView, 'garden_plant')
router.register(r'plants', PlantView, 'plant')
router.register(r'plant_types', PlantTypeView, 'plant_type')
router.register(r'comments', CommentView, 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
