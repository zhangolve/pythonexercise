import requests, re, time
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0'}
pages = []
# #获取音频ID模块
# for n in range(1, 3):
#     urls = 'http://www.ximalaya.com/4932085/album/3160816?page=' + str(n)
#     html = requests.get(urls, headers=header)
#     time.sleep(2)
#     page = re.findall('href="/4932085/sound/(.*?)/" hashlink title=', html.text)
#     pages.extend(page)


# #去重音频ID
# pages = list(set(pages))
# #排序音频ID
# pages.sort()


# ret: 0
# msg: "0"
# trackId: 185851951
# uid: 1266964
# albumId: 23457286
# title: "《斗罗大陆》第001章 唐门，唐三（戴耳机听哦，效果最佳~）"
# domain: "http://audiopay.cos.xmcdn.com"
# totalLength: 12205730
# sampleDuration: 0
# sampleLength: 0
# isAuthorized: true
# apiVersion: "1.0.0"
# seed: 5088
# fileId: "22*23*9*6*25*12*39*45*48*48*39*64*28*39*48*36*39*31*43*22*42*29*36*24*9*23*22*64*64*67*66*55*22*18*42*9*0*9*33*37*1*44*41*48*67*7*12*17*40*67*19*"
# buyKey: "313131393732373231"
# duration: 1507
# ep: "3kNrPox/Sn5Sj6gKPokctQtfTRxyh3KVHIAZKVW0C3upyrOO36/YmLwJ1v/d16kxW7UjznYCcKV82/T3xgEQ074VPg=="
# highestQualityLevel: 2
# downloadQualityLevel: 1
# authorizedType: 0

# https://s1.xmcdn.com/yx/ximalaya-web-static/last/dist/scripts/3bcca3117.js



    #    var o = t.seed
    #             , i = t.fileId
    #             , a = t.ep
    #             , u = t.duration
    #             , s = t.domain
    #             , l = t.apiVersion
    #             , c = function(t, e) {
    #             var n = new gt(t).cg_fun(e);
    #             return "/" === n[0] ? n : "/".concat(n)
    #         }(o, i)
    #             , f = Et(a);
    #         f.duration = u;
    #         var p = function(t) {
    #             var e = t;
    #             return "http://audiopay.cos.xmcdn.com" === t ? e = t.replace("http:", "https:") : (t.indexOf("audio.pay.xmcdn.com") > -1 && (e = "https://vod.xmcdn.com"),
    #             e)
    #         }(s)
    #             , h = "".concat(p, "/download/").concat(l).concat(c)
    #             , d = "".concat(h, "?").concat(e.stringfy(f));
    #         n(d)
    #     }
    # }

def dict2obj(data):
    """将字典对象转换为可访问的对象属性"""
    if not isinstance(data, dict):
        raise ValueError('data must be dict object.')

    def _d2o(d):
        _d = {}
        for key, item in d.items():
            if isinstance(item, dict):
                _d[key] = _d2o(item)
            else:
                _d[key] = item
        return SimpleNamespace(**_d)

    return _d2o(data)


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)

url = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=23457286&pageNum=1';


def get_cookies(): 
    f=open('./cookie.txt','r')#打开所保存的cookies内容文件
    cookies={}#初始化cookies字典变量
    for line in f.read().split(';'):   #按照字符：进行划分读取
        name,value=line.strip().split('=',1)
        cookies[name]=value  #为字典cookies添加内容
    return cookies


def get_all_album():
    album = requests.get(url, headers=header, cookies=get_cookies())
    print(album.json())
    data = album.get('data')
    tracks = data.get('tracks')
    for track in tracks:
        trackId = track.get('trackId')
        title = track.get('title')


get_all_album();


# #下载音频模块
# for m in pages:
#     time.sleep(2)
#     #开始拼接json网址
#     json_usr = 'http://www.ximalaya.com/tracks/' + m + '.json'
#     #开始提交json网址
#     html_json = requests.get(json_usr, headers=header)
#     #开始提取音频网址和音频名称
#     music_url = html_json.json()['play_path_64']
#     music_name = html_json.json()['title']
#     #开始下载音频,保存为二进制数据
#     music_data = requests.get(music_url,headers = header).content
#     #下载到本地
#     with open('%s.m4a'%music_name,'wb') as f:
#         f.write(music_data)
#         print('正在下载....',music_name)