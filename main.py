import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


#step 1: get the html

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#step 2: parse the html

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

#step 3: html tree traversal

#Commanly used types of objects:
#1. print(type(title)) ---- Tag
#2. print(type(title.string)) ------ NavigableString
#3. print(type(soup)) ---- BeautifulSoup
#4. Comment

# markup = "<p><!--this is a comment--->"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))



#Get the title of html page
title = soup.title

#Get all the paragraphs from the page:

paras = soup.find_all('p')
# print(paras)


#get first element in the html page:
print(soup.find('p'))

#get classes of any element in the html page:
print(soup.find('p')['class'])


#find all the elements with class lead:

print(soup.find_all('p',class_="lead"))


#Get the text from the tags/soup:

print(soup.find('p').get_text())
print(soup.get_text())


#Get all the anchors from the page:
anchors = soup.find_all('a')
# print(anchors)

#get all the links on the page:
all_links = set()

for link in anchors:
    if (link.get('href') != '#'):
        linkText = ("https://codewithharry.com"+link.get('href'))
        all_links.add(link)
        print(linkText)



navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent)
print(navbarSupportedContent.contents)

#.contents = A Tag's children are available as a list
#.children = A Tag's children are available as a generator 
#childern are fast as compare to contents bcz content memory m save ho jata h
#nd children iterate krke mil jata h 


# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# for item in navbarSupportedContent.strings:
#      print(item)





# for elem in navbarSupportedContent.contents:
#     print(elem)


# print(navbarSupportedContent.parent)

# print(navbarSupportedContent.parents)

for item in navbarSupportedContent.parents:
    print(item.name)


print(navbarSupportedContent.next_sibling)

print(navbarSupportedContent.next_sibling.next_sibling)

print(navbarSupportedContent.previous_sibling.previous_sibling)