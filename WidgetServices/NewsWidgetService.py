
class NewsWidgetService():
    
    def __init__(self):
        self.__nyt_api = articleAPI('fcc2bc866f604fd6b5f9706f8065f6ef');
    
    def get_news(self):
        # Returns top 3 news from nyt
        # Returns top 3 news from nyt
        
        articles = api.search();
        response = articles['response'];
        docs = response['docs'];
        
        news = [];
        
        counter = 0;
        for doc in docs:
            if counter < 3:
                print doc
                publish_date = doc['pub_date'] if 'pub_date' in doc else None;
                headline = doc['headline'] if 'headline' in doc else None;
                
                if headline != None:
                    headline = headline['main'] if 'main' in headline else None;
                web_url = doc['web_url'] if 'web_url' in doc else None;
                
                multimedia = doc['multimedia'] if 'multimedia' in doc else None;
                image_url = None;
                
                if multimedia != None and len(multimedia) != 0:
                    image_url = multimedia[0]['url'] if 'url' in multimedia[0] else None;
                
                if publish_date != None and headline != None and web_url != None and image_url != None:
                    print 'HI WE"RE IN HERE'
                    snippet = {
                                'headline': headline,
                                'date': publish_date,
                                'web_url': web_url,
                                'image_url': image_url
                               };
                    print snippet          
                    news.append(snippet);
                    counter = counter + 1;
            else:
                break;
        
            return news;
                
                
        
        
        