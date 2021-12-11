from bs4 import BeautifulSoup
import requests
# import lxml
#
# with open ("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title) # title tag with content
# print(soup.title.name) # title tag only
# print(soup.title.string) # content only inside the tag
# print(soup) # all content of html file
# print(soup.prettify()) # indented all the html tag
# print(soup.a) # first anchor tag in the website

# all_anchor_tag = soup.find_all(name = "a") # select all the anchor tags
# print(all_anchor_tag)
#
# for tag in all_anchor_tag: # select only the context inside the tag
#     # print(tag.getText())
#     print(tag.get("href")) # select link

# heading = soup.find(name = "h1", id = "name") #search the first thing
# print(heading)
# print(heading.getText())
#
# section_heading  = soup.find(name = "h3", class_ = "heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
#
# name = soup.select_one(selector = "#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name = "a", class_ = "titlelink")
article_texts = []
article_links = []

for article_tag in articles:

    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_= "score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])


# print(article_texts)
# print(article_links)
# print(article_upvotes)

