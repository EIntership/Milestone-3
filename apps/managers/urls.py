from rest_framework import routers
from django.urls import path
from apps.managers.views import (
    TaskView,
    TaskDetailView,
    MyTaskView,
    CompletedTaskView,
    AssignTaskToUser,
    CompleteTaskView,
    CommentAddView,
    CommentView,
    TimeWorkView,
    # TimeFinishWorkView,
    TimeView,
    # TimeFinishView,
    TaskMonthView,
    TopBiggestTimeTask,
)

router = routers.SimpleRouter()
router.register(r'work-time', TimeWorkView)
router.register(r'time', TimeView)

urlpatterns = [
    path('task', TaskView.as_view(), name='create-task-view'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-info-view'),
    path('top-biggest-time-task', TopBiggestTimeTask.as_view(), name='task-time-log-view'),
    path('time-month', TaskMonthView.as_view(), name='task-time-log-view'),
    path('mytask', MyTaskView.as_view(), name='my-task-view'),
    path('completed-task', CompletedTaskView.as_view(), name='completed-task'),
    path('add-task-to-user/<int:pk>', AssignTaskToUser.as_view(), name="add-task-to-user"),
    path('complete-task/<int:pk>', CompleteTaskView.as_view(), name="complete-task-view"),
    path('add-comment', CommentAddView.as_view(), name="comment-add-view"),
    path('comment/<int:pk>', CommentView.as_view(), name="comment-view"),
    # path('start-work-time', TimeWorkView.as_view(), name="start-work-time"),
    # path('finish-work-time/<int:pk>', TimeFinishWorkView.as_view(), name="finish-work-time", ),
    # path('start-time', TimeView.as_view(), name="start-work-time"),
    # path('finish-time/<int:pk>', TimeFinishView.as_view(), name="finish-work-time"),

]
urlpatterns += router.urls
