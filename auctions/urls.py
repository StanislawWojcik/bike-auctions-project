from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


from . import views

app_name = 'auctions'

urlpatterns = [
    path('', views.index, name='index'),
    path('auction_list/', views.auction_list, name='auction_list'),
    path('add_auction/', views.add_auction, name='add_auction'),
    path('edit_auction/<int:auction_list_id>/', views.edit_auction, name='edit_auction'),
    path('delete_auction/<int:auction_list_id>', views.delete_auction, name='delete_auction'),
    path('search/', views.search, name='search'),
    path('auction_view/<int:auction_list_id>', views.auction_view, name='auction_view'),
    path('my_cart/', views.cart_view, name='cart_view'),
    path('buy_view/', views.buy_view, name='buy_view'),
    path('my_auctions/', views.my_auctions, name='my_auctions'),
    path('cart/<int:auction_list_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:items_in_cart>', views.remove_from_cart, name='remove_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)