from django.urls import path
from assignment1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('users/', views.user_list_dashboard, name='user-list'),
    path('shop/', views.create_shop, name='shop'),
    path('createuser/', views.create_user, name='createuser'),
    path('product/', views.create_product, name='product'),
    path('productcategory/', views.create_product_category, name='product_category'),
    path('productcolour/', views.create_productcolour, name='productcolour'),
    path('order/', views.create_order, name='order'),
    path('cart/', views.create_cart, name='cart'),
    path('review/', views.create_review, name='review'),
    path('shop_input/', views.shop_input, name='shop_input'),
    path('update/<int:id>/', views.update_shop, name='update_shop'),
    path('userinput/', views.user_input, name='userinput'),
    path('productinput/', views.product_input, name='productinput'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('order_input/',views.order_input, name= 'order_input'),
    path('review_input/',views.review_input, name= 'review_input'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)