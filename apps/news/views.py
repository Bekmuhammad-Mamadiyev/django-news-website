from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from apps.news.forms import ContactForm
from apps.news.models import News, Category


def home_views(request):
    categories = Category.objects.all()
    news = News.published.all().order_by('-publish_time')
    jahon_news = News.published.filter(category__name='jahon').order_by('-publish_time')

    home1_news = News.published.first()


    context = {'categories': categories,
               'news': news,
               'jahon_news': jahon_news,
               'home1_news': home1_news,
               }

    return render(request, 'index.html', context)


# def contact_views(request):
#     print(request.POST)
#     form  = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse('<h1>malumotingiz junatildi!</h1>')
#     context = {'form': form}
#     return render(request, 'contact.html', context)


class ContactPageview(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            context = {'form': form}
            return render(request, self.template_name, context)


def new_detail(request, news):

    news = get_object_or_404(News, slug=news)

    return render(request, 'detail.html', {'news': news})


class WorldNewsView(ListView):
    model = News
    template_name = 'world_news.html'
    context_object_name = 'world_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='jahon').order_by('-publish_time')
        return news