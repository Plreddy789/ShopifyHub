from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.ViewCart.as_view()),
    path('cart/add/', views.AddToCart.as_view()),
    path('cart/increase/<int:cart_item_id>/', views.IncreaseProductQuantity.as_view()),
    path('cart/remove/<int:cart_item_id>/', views.RemoveFromCart.as_view()),
    path('cart/apply-discount/', views.ApplyDiscount.as_view()),
    path('cart/save-for-later/<int:cart_item_id>/', views.SaveForLater.as_view()),
    path('cart/persistent/', views.PersistentCart.as_view()),

]
