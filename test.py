from news_grabber import Grabber

ng = Grabber()
news = ng.get('interfax')

print(news)

#url = news[0]['link']
#data = ng.grub(url)
#print(data)