from django.shortcuts import render, get_object_or_404

from apps.news.models import News


def news_list(request):
    news_list = News.objects.all()
    return render(request, 'test/news_list.html', {'news_list': news_list})

def new_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'test/news_detail.html', {'news': news})