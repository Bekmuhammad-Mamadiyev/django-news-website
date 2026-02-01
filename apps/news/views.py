from django.shortcuts import render, get_object_or_404

from apps.news.models import News, Category


def home_views(request):
    categories = Category.objects.all()
    news = News.published.all()

    context = {'categories': categories, 'news': news}

    return render(request, 'index.html', context)


def contact_views(request):
    return render(request, 'contact.html')



def news_list(request):
    news_list = News.published.all()
    return render(request, 'test/news_list.html', {'news_list': news_list})

def new_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'test/news_detail.html', {'news': news})