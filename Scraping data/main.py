# ####Introduction to Web Scraping#####
# from bs4 import BeautifulSoup

# #Alternative parsing module
# import lxml

# with open("website.html") as file:
#         contents = file.read()

# #This is how you make soup
# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.title)
# # print(soup.title.string)

# # Prettify will add indentation to the soup.
# # print(soup)
# # print(soup.prettify())

# # You can access the first tag of any kind by using .p or .a or .h1 etc.
# # print(soup.p)

# # You can create a list of all occurances of tag with find_all()
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
#     #getText() gets the text in the tag.
#     # print(tag.getText())
#     # get() can get the value of any tag attribute.
#     # print(tag.get("href"))

# # find() works like find_all() but just gets the first occurance.
# # You can also find by id.
# heading = soup.find(name="h1", id="name")
# # print(heading)

# #You can also find by class_ name. 
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))

# #You can also find by using a CSS Selector:
# print(soup.select_one(selector=".company a"))
# print(soup.select("a"))


# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://news.ycombinator.com/")

# soup = BeautifulSoup(response.text, "html.parser")
# articless = soup.findAll(name="span", class_="titleline")

# article_links = []
# article_texts = []

# for result in articless:
#     texts = result.getText()
#     article_texts.append(texts)
#     links = result.select_one(selector="a").get("href")
#     article_links.append(links)
 

# scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# # print(article_texts)
# # print(article_links)
# largesr_number = max(scores)
# largesr_index = scores.index(largesr_number)
# print(largesr_index)
# print(article_links[largesr_index])
# print(article_texts[largesr_index])

import requests
from bs4 import BeautifulSoup
import csv

responce = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(responce.text, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]

with open("movies.txt", "a") as file :
    for movie in movies:
        file.write(movie +"\n")

with open('movies.csv', 'w') as file:
    for movie in movies:
       file.write(movie + "\n")