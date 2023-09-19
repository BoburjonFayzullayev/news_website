from django.urls import path
from .views import news_list, news_detail, homepageView, contacpageView, errorpageView

urlpatterns =[
    path('', homepageView, name='home_page' ),
    path('news/', news_list, name= "all_news_list"),
    path('news/<int:id>/', news_detail, name='news_detail_page'),
    path('contact-us/', contacpageView, name='contact_page' ),
    path('404/', errorpageView, name='error_page'),
]