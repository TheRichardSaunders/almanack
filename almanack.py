import re
import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://archive.org/stream/poorrichardsalma00franrich/poorrichardsalma00franrich_djvu.txt")
almanack = bs(page.content, 'html.parser')
quotes=[]

for line in almanack.find("pre").contents[0].split("\n\n"):
    # All quotes are handily numbered
    if re.search("^\d{1,3}\.", line): 
        _,quote = line.strip().replace("\n","").replace('*','').split('. ',1)
        quotes.append( quote )
