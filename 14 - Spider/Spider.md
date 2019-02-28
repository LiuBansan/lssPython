#### ProxyHandler处理（代理服务器）
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许平凡访问某一个固定网站，所以代理一定要很多很多
    - 基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Opener
    - 案例v10-ProxyHandler

#### cookie & session
    - 由于http协议的无记忆性，人们为了你不这个缺陷，所采用的一个补充协议
    - cookie是发放给用户（即http浏览器）的一段消息，
    session是保存在服务器上对应的另一半消息，用来记录用户信息
    
- cookie和session的区别
     - 存放位置不同
     - cookie不安全
     - session会保存在服务器上一定时间，会过期
     - 单个cookie保存数据不超过4K,很多浏览器限制一个站点最多保存20个（不是标准）
- session的存放位置
    - 存在服务器
    - 一般情况，session是存放在内存中或者数据库中
    - 没有cookie登录 案例v11-nocookie ,可以看到，没有使用cookie登录网页反馈的是没有登录的状态      
- 使用cookie登录
    - 直接把cookie复制下来，然后手动放入请求头 案例v12-cookie
    - http模块包含一些关于cookie的模块，通过他们我们可 以自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        
        - FikeCookieJar
            - 使用文件管理cookie
            - filename是保存cookie的文件
        
        - MozillaCookieJar(filename, delayload=None, policy=None):
            - 创建与mocilla浏览器cookie.txt兼容FikeCookieJar文件
        
        - LwpCookieJar
            - 创建与libwww-perl标准兼容的Set-Cookie3格式和FikeCookieJar文件
      
        - 他们的关系是：CookieJar --> FikeCookieJar --> MozillaCookieJar & LwpCookieJar
    - 利用cookiejar访问人人，案例v13-cookiejar     
        - 自动使用cookie登录，大致流程
        - 打开登录页面都自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
        
    - handler是Handler的实例，常用参看案例代码
        - 用来处理复杂请求
    
                # 生成cookie的管理器
                cookie_handler = request.HTTPCookieProcessor(cookie)
                
                # 创建HTTP请求管理器
                http_handler = request.HTTPHandler()
                
                # 生成https管理器
                https_handler = request.HTTPSHandler()
        
        
    - 创立handler后，使用opener打开，打开后相应的业务有相应的handler处理
    - cookie作为一个变量，打印出来，案例v14-handler-cookie   
        
        
        
        
        
        
        
        
        
        
        
        
        
