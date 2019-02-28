from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建HTTP请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名和密码，用来获取登录cookie凭证
    '''

    # 此url需要从登录的请求出提取
    url = 'https://passport.bilibili.com/login'

    # 此键值需要从登录form的两个对应的input中提取name属性
    data = {
        'login-username':'1670350470@qq.com',
        'login-passwd':'liusha0912'
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'https://space.bilibili.com/64514021'
    # 如果已经执行了login函数，则opener自动已经包含相应的值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('rr.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()