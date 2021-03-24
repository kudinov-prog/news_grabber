import feedparser
from newspaper import Article


class Grabber():
    """ Класс граббера. В словаре sources находятся ссылки для парсинга
    """

    sources = { 
        'interfax':'http://www.interfax.ru/rss.asp',
        'lenta':'http://lenta.ru/rss',
        'kommersant':'http://www.kommersant.ru/RSS/news.xml',
        'm24':'http://www.m24.ru/rss.xml'
    }
    
    def setNewUrl(self, url, name):
        self.sources[name] = url

    def get(self, sources, limit = 3):

        feed = feedparser.parse(self.sources.get(sources))
        
        result = [
            {
                'title': item['title'],
                'link': item['link'],
                'desc': item['description'],
                'published': item['published']
            }
            for item in feed['items']]

        if limit is None:
            return result
        elif limit > 0:
            return result[0:limit]
        return []

    def grub(self, url):
        article = Article(url, language='ru')
        article.download()
        article.parse()
        return {
            'title': article.title,
            'image': article.top_image,
            'content': [
                paragraph for paragraph in article.text.split('\n') if paragraph
                ]
        }
