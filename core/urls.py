from django.urls import path
from core.views import *

urlpatterns = [
    # path('', index, name='home'),
    path('home/<int:page_count>/', index, name='home'),
    # path('home/', ClothesList.as_view(), name='home'),
    path('home2/', home2, name='home2'),
    path('home3/<int:page_count>/', home3, name='home3'),
    # path('home3/', Home3List.as_view(), name='home3'),
    path('contact/', contact, name='contact'),
    # path('blog/', blog, name='blog'),
    path('blog/', BlogList.as_view(), name='blog'),
    path('shop/', product, name='shop'),
    path('shop/<int:page_count>/', product, name='shop'),
    path('about/', about, name='about'),
    path('features/', features, name='features'),
    path('product/<slug:slug>/', single_product, name='single-product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('update-quantity/<int:product_id>/<str:quantity>/', update_quantity, name='update-quantity'),
    path('blog-detail/<int:id_>/', blog_detail, name='blog-detail'),
    path('general-search/', general_search, name='general-search'),
    path('change_wish/<int:product_id>/', change_whish, name='change-wish'),
    path('add_review/<int:product_id>/', add_review, name='add-review'),
    path('add-blog-comment/<int:blog_id>/', add_blog_comment, name='add-blog-comment')
]