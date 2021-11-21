import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

###

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        title = a_tag.text
        star = tr.select_one('td.point').text
        rank = tr.select_one('td > img')['alt']
        doc = {
            'rank' : rank,
            'title' : title,
            'star' : star
        }
        db.movies3.insert_one(doc)

movie = db.movies3.find_one({'title':'매트릭스'})
mat_star = movie['star']
same_stars = list(db.movies3.find({'star':mat_star},{'_id':False}))
for same_star in same_stars:
    mat_same_star = same_star['title']
    print(mat_same_star)
db.movies3.update_one({'title':'매트릭스'},{'$set':{'star':"0"}})
