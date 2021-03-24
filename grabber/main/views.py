from django.views.generic import ListView

from news_grabber import Grabber


with open('sources.txt', 'r') as f:
    sources = f.read().splitlines()


class IndexLisView(ListView):
    template_name = 'index.html'
    context_object_name = 'index'

    def get_queryset(self):
        ng = Grabber()
    
        news = [ng.get(item) for item in sources]
        return news
