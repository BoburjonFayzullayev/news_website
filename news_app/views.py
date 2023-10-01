from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from .models import News, Category
from .forms import Contactform

def news_list(request):
    news_list= News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)

def homepageView(request):
    categories = Category.objects.all()
    news_list = News.published.order_by("publish_time")[:4]
    local_one = News.published.filter(category__name = "Mahalliy").order_by("publish_time")[:1]
    local_news = News.published.all().filter(category__name = "Mahalliy").order_by("publish_time")[1:6]
    context = {
        'news_list': news_list,
        'categories':categories,
        'local_one': local_one,
        'local_news': local_news,
    }
    return render(request, 'news/index.html', context)

class  HomepageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.order_by("publish_time")[:4]
        # context['local_one'] = News.published.filter(category__name = "Mahalliy").order_by("publish_time")[:1]
        context['mahalliy_news']= News.published.all().filter(category__name = "Mahalliy").order_by("publish_time")[:5]
        context['xorij_xabarlari'] = News.published.all().filter(category__name="Xorij").order_by("publish_time")[:5]
        context['sport_xabarlari'] = News.published.all().filter(category__name="sport").order_by("publish_time")[:5]
        context['texnologiya_xabarlari'] = News.published.all().filter(category__name="Texnologiya").order_by("publish_time")[:5]


        return context


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = "mahalliy_yangiliklar"

    def get_queryset(self):
        news = News.published.all().filter(category__name="Mahalliy")
        return news
class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = "xorij_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorij")
        return news
class TechnolgyNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = "texnologiya_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnologiya")
        return news
class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = "sport_yangiliklar"


    def get_queryset(self):
        news = self.model.published.all().filter(category__name="sport")
        return news






# def contacpageView(request):
#
#     form = Contactform(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse(" <h2> Biz bog`langaningiz uchun rahmat")
#     context = {
#         "form": form
#     }
#
#     return render(request, 'news/contact.html', context)


class ContactPageView(TemplateView):
    template_name = "news/contact.html"



    def get(self, request, *args, **kwargs):
        form = Contactform()
        context = {
            "form":form
        }
        return render(request, 'news/contact.html', context)
    def post(self, request, *args, **kwargs):
        form = Contactform(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse(" <h2> Biz bog`langaningiz uchun rahmat </h2>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)





def errorpageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)



class NewsUpdateView(UpdateView):
    model = News
    template_name = 'crud/edit_news.html'
    fields = ['title', 'body', 'image', 'status', 'category']

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')


