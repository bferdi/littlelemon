from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

# import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"booking/tables", views.BookingViewSet, basename="Booking")

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view(), name="menu_items"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="single_menu_item"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("", include(router.urls)),
]