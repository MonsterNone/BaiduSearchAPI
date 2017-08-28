from baiduSearch import process

with open('../results/百科.txt') as a:
    results = process.page(a.read())
    for i in results:
        print('{0} {1} {2} {3} {4}'.format(i.index, i.title, i.abstract, i.show_url, i.url))  # 此处应有格式化输出
