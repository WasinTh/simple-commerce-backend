from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from shop.models import Member, Banner
from shop.serializers import MemberCreateSerializer, MemberLoginSerializer, BannerSerializer
from django.contrib.auth.models import User


class MemberRegisterView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer

    
class MemberLoginView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = MemberLoginSerializer

class BannerView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer