import baiduSearch

results = baiduSearch.search('python', convey=True)

for i in results:
    print(i.url)
