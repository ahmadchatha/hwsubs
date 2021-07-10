"""hwsubs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from users import views as user_views
from assignments import views as assignment_views
from grades import views as grade_views
from submissions import views as submission_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', user_views.GroupViewSet, basename='group')
router.register(r'assignments', assignment_views.AssignmentViewSet, basename='assignment')
router.register(r'grades', grade_views.GradeViewSet, basename='grade')
router.register(r'submissions', submission_views.SubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
