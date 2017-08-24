######################################################
#                                                    #
#                    By MonsterNone                  #
#    https://github.com/monsternone/baidusearchapi   #
#                                                    #
######################################################

import requests
from bs4 import BeautifulSoup

# 获取结果页面
url = 'http://www.baidu.com/s?wd='  # 搜索请求网址
keyword = input('请输入搜索关键词：')  # 获取搜索关键词
r = requests.get(url + keyword)
if r.status_code != 200:  # 请求错误（不是200）处理
    print(r.status_code)
    exit(2)
soup = BeautifulSoup(r.text, 'lxml')


# 获取title和c_url，这俩货恰好可以一起
def get_title_and_c_url(result_div):
    r_from = result_div.find('a')  # 先获取第一个<a>，r refers to result
    if not r_from:
        return [None, None]
    for em in r_from.find_all('em'):  # 移除title中的em标签
        em.unwrap()
    return [r_from.get_text(), r_from['href']]


# 获取abstract
def get_abstract(result_div):
    if 'result-op' not in result_div['class']:  # 不是软广
        r_from = result_div.find(class_='c-abstract')
        if not r_from:
            return None
        for em in r_from.find_all('em'):  # 移除abstract中的em标签
            em.unwrap()
        return r_from.get_text()
    else:
        return '百度软广，当前代码版本不予摘要'  # 其实是因为太麻烦


# 获取show_url
def get_show_url(result_div):
    show = result_div.find(class_='c-showurl')
    if not show or show == '<span class="c-showurl"> </span>':  # 有些软广class不一样
        show = result_div.find(class_='c-showurl-color')
    if not show:  # 要是还不一样。。
        return '此结果未能如期获取到show url，提交issue帮助我们做的更好'
    return show.get_text()[:-2]  # 去除末尾/


# 获取结果来源
result_set = soup.find(id='content_left')  # 结果全显示在页面左边
result_set = result_set.find_all('div', class_='c-container')  # 结果class固定，其余为硬广


# 处理结果
class Result(object):  # 定义返回的result类
    def __init__(self, r_index, r_title, r_abstract, show_url, r_url):  # id似乎占用了内部名称，那就用index来代替吧
        self.__index = r_index
        self.__title = r_title
        self.__abstract = r_abstract
        self.__show_url = show_url
        self.__url = r_url

    def index(self):
        return self.__index

    def title(self):
        return self.__title

    def abstract(self):
        return self.__abstract

    def show_url(self):
        return self.__show_url

    def url(self):
        return self.__url


# 返回数组，先清空
results = []

for i in range(len(result_set)):  # 因为要index所以就用range来
    result = result_set[i]  # 其实就是result_div

    t_and_u = get_title_and_c_url(result)
    c_title = t_and_u[0]  # 这个c_title就是title了
    c_url = t_and_u[1]  # c_url是百度的url，需要转换
    c_abstract = get_abstract(result)  # 同title
    c_show_url = get_show_url(result)

    result = Result(i + 1, c_title, c_abstract, c_show_url, c_url)
    results.append(result)

for i in results:
    print('{0} {1} {2} {3} {4}'.format(i.index(), i.title(), i.abstract(), i.show_url(), i.url()))  # 此处应有格式化输出
