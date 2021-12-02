"""
Script requires one argument which is URL website with article from forbes.pl
Script retrieves the whole text from the website and puts it into local html document.
"""

import sys 
import requests
import webbrowser
import jinja2
import os
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    raise Exception('You need to pass URL address of the Forbes article\nExample:\npython main.py www.forbes.pl/article1')

HTML_FILENAME = 'article.html'
HTML_TEMPLATE_FILE = "template.html"

# Read given url
URL = sys.argv[1]

# Get html content
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Get all the data that is covered on the website
article_div_content = soup.find("div", class_="articleContainer")
    
# Gather all the content together to put in template file
main_website_content = ""
for content in article_div_content:
    main_website_content += str(content)

# Render HTML template file content 
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(HTML_TEMPLATE_FILE)
outputText = template.render(content=main_website_content)

# Create HTML file with main content data
with open(HTML_FILENAME, "w") as f:
    f.write(outputText)

# Open ready document in the browser
webbrowser.open('file://' + os.path.realpath(HTML_FILENAME))
