from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('product-detail/<str:pk>/', views.product_detail, name="product-detail"),
    path('create-product/' , views.createProduct, name="create-product"),
    path('product-detail/<str:pk>/', views.product_detail, name='product-detail'),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
    path('delete-all/', views.deleteAllProducts, name="delete-all"),
    path('issue-items/<str:pk>/', views.issue_items, name='issue-items'),
    path('receive-items/<str:pk>/', views.receive_items, name='receive-items'),
    path('list-history/', views.list_history, name='list-history'),
]