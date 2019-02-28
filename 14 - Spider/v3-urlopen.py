from urllib import request
import chardet

if __name__ == "__main__":
    url = "https://movie.douban.com/subject/27119586/"
    rsp = request.urlopen(url)

    print(type(rsp))
    print(rsp)


    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html = rsp.read()


    # 使用get取值保证不会出错


    html = html.decode()
    print()