import requests
import urllib.parse
from bs4 import BeautifulSoup
import time

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

def check_price(url):

    response = requests.get(url, headers=headers)
    parsed_url = urllib.parse.urlparse(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup.encode('utf-8')
    if parsed_url.netloc == "www.mediamarkt.nl":
        try:
            if (title := soup.find(itemprop= "name").get_text()) and (instock := soup.find(itemprop = "availability").get_attribute_list("content")) and (price := soup.find(class_ = "price").get_text()):
                if instock[0] == "InStock":
                    print("INSTOCK: "+title.strip()+" for: "+price)
                else:
                    print("NOT INSTOCK: "+title.strip())
        except:
            print("NO DETAILS for: "+title.strip())
            pass
    elif parsed_url.netloc == "www.coolblue.nl":
        #Not Working Yet
        try:
            if (instock := soup.find(itemprop = "availability").get_attribute_list("content")) and (price := soup.find(class_ = "price").get_text()) and (title := soup.find(itemprop= "name").get_text()):
                print(title.strip())
                print(price)
                print(instock)
        except:
            print("No details were found for: "+title.strip())
            pass


while(True):
    check_price("https://www.mediamarkt.nl/nl/product/_nintendo-switch-lite-grijs-1627926.html")
    check_price("https://www.mediamarkt.nl/nl/product/_nintendo-switch-grijs-1635021.html")
    check_price("https://www.mediamarkt.nl/nl/product/_nintendo-switch-oled-wit-tas-racing-wheels-accessoire-1715272.html?rbtc=tra|con|2134463|802fa91837af55ca302c3181f5257914|p|&tduid=802fa91837af55ca302c3181f5257914")
    check_price("https://www.mediamarkt.nl/nl/product/_nintendo-switch-oled-wit-mario-kart-gaming-bundel-1707743.html")
    print("----------------------------------------------------------------------------")
    time.sleep(60)
