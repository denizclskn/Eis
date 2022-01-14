from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('first_report/<str:pk>/', views.firstReport, name="firstReport"),
    path('report_questions/<str:pk>/', views.createReport, name="reportQuestions"),
    path('delete_report/<str:pk>/', views.deleteReport, name="deleteReport"),
    path('my_reports/', views.myReports, name="myReports"),
    path('logout/', views.logoutUser, name="logout"),
    path('pdf/<str:pk>', views.generatePDF, name="genPDF"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/resetPassword.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/resetPasswordSent.html"), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/resetPasswordForm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/resetPasswordDone.html"), name="password_reset_complete"),


]