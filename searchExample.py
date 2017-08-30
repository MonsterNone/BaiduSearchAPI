from . import baiduSearch

keyword = input('请输入搜索关键词：')

convey = input('需要将结果的百度统计链接转换为实际链接吗（y/N）'
               '（不转换会加快结果显示速度）:')

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')

for result in results:
    print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
