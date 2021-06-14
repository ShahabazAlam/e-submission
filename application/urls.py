from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from application import views


app_name='application'
urlpatterns = [
    path('', views.index, name='index'),
    path('application/register/', views.register, name='register'),
    path('application/login', views.login_user, name='login'),
    path('application/logout/', views.logout_user, name='logout'),
    # pathapplication/('profile/', views.profile, name='profile'),
    path('application/profile/<department>/', views.profile, name='profile'),
    path('application/profile_t/<department>/', views.profile_t, name='profile_t'),
    path('application/assignment/<assign_id>/', views.detail, name='detail'),
    path('application/assignment_t/<assign_id>/', views.detail_t, name='detail_t'),
    path('application/sol_detail_t/<sol_id>/', views.sol_detail_t, name='sol_detail_t'),
    path('application/submit/<assignment_id>/', views.submit, name='submit'),
    path('application/add_t/<department>/', views.add_t, name='add_t'),
    # path('', views.dashboard, name='dashboard'),
    path('application/t_courses/', views.t_courses, name="t_courses"),
    path('application/s_courses/', views.s_courses, name="s_courses"),
    path('application/filter_t/<semester>/<department>/', views.filter_t, name='filter_t'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete")
]