from urllib import request
from urllib import parse

'''
利用request下载页面
自动检测页面编码
'''

if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # 要想使用data,需要使用字典结构
    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url +qs
    print(fullurl)

    #如果直接使用刻度的带参数的url，是不能访问的
    #fullurl = "http://www.baidu.com/s?wd=易烊千玺"

    rsp = request.urlopen(fullurl)
    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()
    print()