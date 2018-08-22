# 爬取豆瓣正在上映的电影的数据
import requests
from lxml import etree

# 抓取网站html
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/'
response = requests.get(url=url, headers=headers)
text = response.text
# print(response.text)

# 将抓取到的HTML根据一定的规则进行提取数据
html = etree.HTML(text)
ul = html.xpath('//ul[@class="ui-slide-content"]')[0]  # 提取正在上映的电影的数据
# print(ul)
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))
lis = ul.xpath('./li')  # 提取每一个电影的数据
movies = []  # 存放爬取到的所有的上映电影的数据
for li in lis:
    # print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    title = li.xpath('@data-title')  # 电影名
    rate = li.xpath('@data-rate')  # 评分
    duration = li.xpath('@data-duration')  # 电影时长
    region = li.xpath('@data-region')  # 上映地点
    director = li.xpath('@data-director')  # 导演
    actors = li.xpath('@data-actors')  # 演员
    thumbnail = li.xpath('.//img/@src')  # 电影海报

    movie = {
        'title': title,
        'rate': rate,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }
    movies.append(movie)

print(movies)