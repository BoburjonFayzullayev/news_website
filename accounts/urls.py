from django.urls import path
from .views import user_login, dashboard_view, user_register, edit_user, EditUserView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # path('login/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', dashboard_view, name='user_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password-done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complite/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', user_register, name='signup'),
    path('profile/edit/', edit_user, name='edit_profile'),
    # path('profile/edit/', EditUserView.as_view(), name='edit_profile')

]