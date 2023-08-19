import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# get html
r = requests.get(url)
htmlContent = r.content

# parse html
soup = BeautifulSoup(htmlContent, 'html.parser')

# prettify the parsed content
prettified_html = soup.prettify()
# print(prettified_html)          
 

# Html Tree traversal

# commonly used types of objects:
# print(type(title))  # 1. Tags
# print(type(title.strings)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# markup = "<p><!-- this is commit --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.strings))
# exit()

# get title of the HTML page
title = soup.title
# print(title)

# get all the paragraphs from page

paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')
# # get all the link on the page



# print(anchors)

# # get first element in Html Page
 
# print(soup.find('p'))

# # get element of any element in the Html page

# print(soup.find('p')['class'])

# # find all element with class lead

# print(soup.find_all("p", class_="lead"))

# # get text from tags/soup

# print(soup.find('p').get_text())
# print(soup.get_text())

# all_link = set()
# for link in anchors:
#     if(link != '#'):
#        link = ("https://codewithharry.com" + link.get('href'))
#        all_link.add(link)
#        print(link)



# .content - a tag's children are available as a list 
# .children - a tag's children are available as a generator

navbarSupportContent = soup.find(id='search-toggle')
# for elem in navbarSupportContent.children        :
#     print(elem)

# for item in navbarSupportContent.strings:
#     print(item)

# for item in navbarSupportContent.stripped_strings:
#     print(item)

# print(navbarSupportContent.parent)

# for item in navbarSupportContent.parents:
#     print(item.name)

# print(navbarSupportContent.next_sibling.next_sibling)
# print(navbarSupportContent.previous_sibling)

elem = soup.select('.Toastify')
print(elem)
