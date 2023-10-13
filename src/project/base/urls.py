from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import PendingList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login, Register


urlpatterns = [
    path('', PendingList.as_view(), name='tasks'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete')
]
