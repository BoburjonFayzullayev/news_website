from django.urls import path
from .views import news_list, news_detail,  errorpageView, ContactPageView, HomepageView, \
    LocalNewsView, TechnolgyNewsView, SportNewsView, ForeignNewsView, NewsDeleteView, NewsUpdateView, NewsCreateView

urlpatterns =[
    path('', HomepageView.as_view(), name='home_page' ),
    path('news/', news_list, name= "all_news_list"),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page' ),
    path('404/', errorpageView, name='error_page'),
    path('local/', LocalNewsView.as_view(), name="local_news_page"),
    path('techno/', TechnolgyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),

]