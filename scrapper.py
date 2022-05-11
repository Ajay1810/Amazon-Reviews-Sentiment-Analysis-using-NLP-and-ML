from bs4 import BeautifulSoup as bs
import requests

link = 'https://www.amazon.in/dp/B07LH5JMHQ?th=1'


page = requests.get(link)
page
page.content

soup = bs(page.content,'html.parser')
print(soup.prettify())

s = soup.find_all('i',class_='review-rating')
star = []
for i in range(0,len(s)):
    star.append(s[i].get_text())
print(star)

rev = soup.find_all('div',class_='review-text-content')
review = []
for i in range(0,len(review)):
    review.append(rev[i].get_text())
print(review)



import pandas as pd
df1 = pd.DataFrame(star)
df2 = pd.DataFrame(review)
df3 = pd.concat([df1,df2], axis = 0, ignore_index = True)
df3.to_csv('scrappedReviews.csv')
