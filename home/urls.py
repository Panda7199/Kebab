from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('category_product/<int:id>/<slug:slug>', views.category_product, name='category_product'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('cheff/', views.cheff, name='cheff'),
    path('cheff_detail/<int:id>', views.cheff_detail, name='cheff_detail'),
    path('comment_cheff/<int:id>', views.comment_cheff, name='comment_cheff'),
]
