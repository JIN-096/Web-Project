import requests
from bs4 import BeautifulSoup

"""
정보센터식당 "/sub03/sub01_01.html?shop_sqno=35"
복지관 교직원식당 "/sub03/sub01_01.html?shop_sqno=36"
카페테리아 첨성 "/sub03/sub01_01.html?shop_sqno=37"
GP감꽃푸드코트"/sub03/sub01_01.html?shop_sqno=46"
복현 카페테리아"/sub03/sub01_01.html?shop_sqno=79"
(외부업체)공학관교직원식당 "/sub03/sub01_01.html?shop_sqno=85"
(외부업체)공학관학생식당"/sub03/sub01_01.html?shop_sqno=86">

현재 교직원 식당과 카페테리아 첨성, 공학관교직원 식당만 운영됨.
"""

# 복지관 교직원 식당.
req = requests.get("http://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=36")
soup = BeautifulSoup(req.text, 'html.parser')
diet_36 = []
for tmp in soup.select('#print > div > table > tbody > tr > td'):
    diet_36.append(tmp.text)

# 카페테리아 첨성.
req = requests.get("http://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=37")
soup = BeautifulSoup(req.text, 'html.parser')
diet_37 = []
day = []
for i in range(5):
    select_key = '#print > div > table > tbody > tr > td:nth-child(' + str(i+1) + ')'
    for tmp in soup.select(select_key):
        for food in tmp.select('li'):
            day.append(food.text)
        diet_37.append(day)
        day = []

# 공학관 교직원식당.
req = requests.get("http://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=85")
soup = BeautifulSoup(req.text, 'html.parser')
diet_85_lunch = []
diet_85_dinner = []
for tmp in soup.select('#print > div:nth-child(2) > table > tbody > tr > td > ul > li > p'):
    diet_85_lunch.append(tmp.text)
for tmp in soup.select('#print > div:nth-child(3) > table > tbody > tr > td > ul > li > p'):
    diet_85_dinner.append(tmp.text)
