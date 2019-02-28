from urllib import request

if __name__ == '__main__':

    url = 'http://space.bilibili.com/64514021'
    headers = {
        'cookie':'buvid3=4C79F631-B49A-4ADD-A0FB-1E3BC8816A9981641infoc; LIVE_BUVID=AUTO7215504762556157; sid=821twf4u; DedeUserID=64514021; DedeUserID__ckMd5=0b0d591860e9838a; SESSDATA=b03b4e11%2C1553068298%2C950a9421; bili_jct=8196e8f281235ec7613db4c01fea95f3; _uuid=0DE09C22-CD84-9F07-6E99-88A35259A84B02427infoc; _dfcaptcha=4cc75e2502c213fb3309335d70229ddf; UM_distinctid=168ff96f7fe2d9-01225694c2bd5f-32564d7a-100200-168ff96f7ff463; CNZZDATA2724999=cnzz_eid%3D331161110-1550474894-https%253A%252F%252Fpassport.bilibili.com%252F%26ntime%3D1550474894; bp_t_offset_64514021=221699387122267858; finger=edc6ecda; im_notify_type_64514021=0; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1550476444; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1550476471; fts=1550476492'   }

    req = request.Request(url, headers = headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open('bilibili.html', 'w', encoding='utf-8') as f:
        f.write(html)
