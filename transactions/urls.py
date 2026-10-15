from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .forms import RememberMeAuthForm
from rest_framework.routers import DefaultRouter
app_name = "transactions"

router = DefaultRouter()
router.register(
    "transactions",
    views.TransactionsViewSet,
    basename="transaction",
)

urlpatterns = [
    path("",views.register ,name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='transactions/login_page.html',authentication_form=RememberMeAuthForm), name='login_page'),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("home/",views.home,name="home"),
    path("api/", include(router.urls)),
]