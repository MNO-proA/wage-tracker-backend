from django.urls import path
from .views import WorkHourListCreateView, WorkHourRetrieveUpdateDeleteView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeAbsenceViewSet

router = DefaultRouter()
router.register('employee-absences', EmployeeAbsenceViewSet, basename='employee-absence')


urlpatterns = [
    path('work-hours/', WorkHourListCreateView.as_view(), name='workhour-list-create'),
    path('work-hours/<int:pk>/', WorkHourRetrieveUpdateDeleteView.as_view(), name='workhour-retrieve-update-delete'), 
    path('', include(router.urls)),
]


