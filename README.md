## 施工ing......请带好安全帽

---

# 百度搜索接口,通过python3

## 依赖库

* bs4
* lxml
* requests

## 使用说明

将baiduSearch放在代码根目录里

### 调用

``` python3
import baiduSearch （pyCharm中可能会报错，不要管，运行没问题）
baiduSearch.search(keyword, **kwargs)
```

#### keyword

搜索关键词

#### kwargs

convey=True/False (默认为False)

转换结果的baidu统计url为实际url（有的网站比较慢）

### 返回结果

结果类型为自定义的Results

* index 序号，供用户输入选择（searchBot学习功能会用到）
* title 标题
* abstract 简介
* show_url 应该是域名
* url 网址（百度跳转或者实际网址）
* convey_url() 转换百度链接

## 例程

见searchExample.py

---

> 这是SearchBot项目的一部分
