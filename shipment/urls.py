from django.urls import path

from . import views

urlpatterns = [
    path('', views.tpc_dashboard, name="tpc-dashboard"),
    path('register/new', views.register, name='register'),
    path('all-user', views.AllUserListView.as_view(), name="all-users"),
    path('user-delete/<int:id>', views.user_delete, name="user-delete"),
    path('update-user/<int:pk>', views.UserUpdateView.as_view(), name='update_user'),
]