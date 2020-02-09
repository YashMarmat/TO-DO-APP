from django.urls import path
from .views import(
    ScheduleList,
    ScheduleCreate,
    ScheduleUpdate,
    ScheduleDelete,
) 


urlpatterns = [
    path('', ScheduleList.as_view(), name = 'home'),
    path('schedule/create/', ScheduleCreate.as_view(), name = 'schedule_create'),
    path('schedule/<int:pk>/update/', ScheduleUpdate.as_view(), name = 'schedule_update'),
    path('schedule/<int:pk>/delete/', ScheduleDelete.as_view(), name = 'schedule_delete'),
]