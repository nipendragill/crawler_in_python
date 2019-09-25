import requests    
import re    
from urllib.parse import urlparse 

class Crawler:    
    def __init__(self, starting_url):    
        self.starting_url = starting_url                       
        self.urls_visited = set()    
       
    def get_html(self, url):    
        try:    
            html = requests.get(url)    
        except Exception as e:     
            return None
        return html.content.decode('latin-1')    

    def get_links(self, url):    
        html = self.get_html(url)      
        links = None 
        if html is not None:
            links = re.findall(r'href=[\'"]?([^\'" >]+)', html)         

        return set(filter(lambda x: 'http' in x, links))                

    def crawl(self, url):                   
        for link in self.get_links(url):    
            if link in self.urls_visited:        
                continue                    
            print(link)                 
            self.urls_visited.add(link)                
            self.crawl(link)     

    def start(self):
        self.crawl(self.starting_url)                            

if __name__ == "__main__":    
    crawler = Crawler('https://www.python.org')    
    crawler.start()