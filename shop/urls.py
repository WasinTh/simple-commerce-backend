from django.urls import path
from shop import views

urlpatterns = [
    path('register/',views.MemberRegisterView.as_view(), name='member-register'),
    path('login/', views.MemberLoginView.as_view(), name='member-login'),
    path('banner/', views.BannerView.as_view(), name='banner'),
]
