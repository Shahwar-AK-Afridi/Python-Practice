import requests
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup('<b class="boldest" nigga = "hello">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))

print(tag.name)
# <class 'bs4.element.Tag'>

tag.name = "h1"
print(tag.name)

print(tag["class"])
print(tag.attrs)


tag["id"] = "hello world"
tag["python"] = "beautiful soup"
print(tag)


css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
print(css_soup.p['class'])

p_tag = css_soup.p
print(p_tag["class"])
# ['body']

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')

p2_tag = css_soup.p
print(p2_tag["class"])
# ['body', 'strikeout']

rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
a_tag = rel_soup.a
p_tag = rel_soup.p
print(a_tag["rel"])

a_tag["rel"] = ["index", "content"]

print(a_tag["rel"])
print("here it is")
print(type(a_tag["rel"]))
print(a_tag)
print(p_tag)

a_text = rel_soup.a
print(a_text.string)
print(type(a_text.string))



unicode_String = str(a_text.string)

print(unicode_String)
print(type(unicode_String))

a_text.string.replace_with("Not a homepage")
print(a_text.string)



soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup)
#print(soup.head)
head_tag = soup.find("head")
print(head_tag)
print(type(head_tag))

a_tags = soup.find_all("a")
print(a_tags)
print(type(a_tags))
print(type(list(a_tags)))


html_tag = soup.html
print(html_tag.contents)


head_tag = soup.head
print(head_tag)

print(head_tag.contents)
#print(type(head_tag.contents))

title_tag = head_tag.contents[0]
print(title_tag)

print(title_tag.string)

string = title_tag.contents[0]
print(string)

print(soup.head.title.string)

print(soup.contents)
print("------------------------------------------------------")

for child in soup.children:
    print(child)
print("dddddddddddddddddddddddddddddddddd")
for child in soup.html.children:
    print(child)

print("--------------------------------------")

for child in soup:
    print(child)

print("----------------------------learning .decendents-------------------------------------")


print(len(list(soup.children)))

print(len(list(soup.descendants)))
print(len(list(head_tag.descendants)))

for child in soup.children:
    print(child)

print("----------------------------------------")
for child in soup.descendants:
    print(child)