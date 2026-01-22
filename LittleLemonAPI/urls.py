from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-items/category", views.CategoriesView.as_view()),
    # transparent alias for backward-compatibility
    path("categories", views.CategoriesView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("groups/managers/users", views.ManagersView.as_view(), name="managers-list"),
    path("groups/managers/users/<int:pk>", views.ManagersRemoveView.as_view(), name="managers-remove"),
    # Backwards-compatible transparent mappings (serve same view without redirect)
    path("groups/manager/users", views.ManagersView.as_view()),
    path("groups/manager/users/<int:pk>", views.ManagersRemoveView.as_view()),
    path("groups/delivery-crew/users", views.DeliveryCrewView.as_view()),
    path("groups/delivery-crew/users/<int:pk>", views.DeliveryCrewRemoveView.as_view()),
    path("cart/menu-items", views.CartView.as_view()),
    # Backwards-compatible alias so /api/cart/orders also works
    path("cart/orders", views.OrderView.as_view()),
    path("order", views.OrderView.as_view()),
    # Transparent alias so both /api/order and /api/orders work
    path("orders", views.OrderView.as_view()),
    path("orders/<int:pk>", views.SingleOrderView.as_view()),
]
