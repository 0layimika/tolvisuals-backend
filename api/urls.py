from django.urls import path
from.views import *
urlpatterns=[
    path("portfolio",PortfolioView.as_view(), name='portfolio'),
    path("clients", ClientView.as_view(), name='clients'),
    path('faq',FAQView.as_view(), name='faq'),
    path('review', ReviewView.as_view(), name='review'),
    path("clients/<int:id>",ClientImagesVIew.as_view(), name='client-images'),
    path("home", HomeView.as_view(), name='home-be'),
    path("about", AboutView.as_view(), name='about')
]