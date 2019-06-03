import re
import requests

class Spider():
    all_visited = []

    @classmethod
    def crawl(cls, url, depth, visited=all_visited):
        if depth == 0:
            return visited
        r = requests.get(url)
        visited.append(url)
        
        for link in cls.find_links(r.text):
            if link not in visited:
                visited += cls.crawl(link, depth-1, visited)
                visited.append(link)
        return visited

    @staticmethod
    def find_links(html):
        links = []
        results = re.findall(r"(?<=href=\").*?(?=\")", html)
        for r in results:
            if "http" in r:
                links.append(r)
        for link in links:
            print(link)
        return links

    @classmethod
    def get_links(cls):
        return cls.all_visited



if __name__ == '__main__':
    Spider.crawl("http://www.sql-join.com/sql-join-types", 2)
    print(Spider.get_links())
