from django.urls import path
from CRT import views
from django.contrib.auth import views as ad

urlpatterns=[
path('',views.home,name='home'),
path('pro/',views.profile,name='profile'),
path('about/',views.about,name='ab'),
path('contact/',views.contact,name='contact'),
path('user/',views.authuser,name='autuser'),
path('breg/',views.beforereg,name='beforerg'),
path('alog/',ad.LoginView.as_view(template_name='html/adminlogin.html'),name='alog'),
path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name='log'),
path('re/',views.regi,name='rg'),
path('ds/',views.dashboard,name='dash'),
path('lgot/',ad.LogoutView.as_view(template_name='html/logout.html'),name='logo'),
path('complaint/',views.complaint,name='complaint'),
path('updf/',views.updf,name='update'),
path('ch/',views.cgf,name='cg'),
path('rst/',ad.PasswordResetView.as_view(template_name='html/resetpassword.html'),name='reset_password'),
path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html/resetpassworddone.html'),name="password_reset_done"),
path('rst_confirm/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html/resetpasswordconfirm.html'),name='password_reset_confirm'),
path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name='html/reset_password_complete.html'),name="password_reset_complete"),
path('acheive',views.acheivements,name="achieve"),
# path('sign/',views.sign,name="sign"),
]

