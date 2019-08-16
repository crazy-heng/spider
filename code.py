import requests
import re


def getHTMLText(url):
    try:
        hearder = {
            'user - agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'cookie': 't=e7da0f038d85780f0ca4307847e36bc5; cookie2=1f398af6edd8291b25b24bc22d5605ed; _tb_token_=607e37534b68; cna=6lIIFJ39s0ACAXcnEGK+Drny; thw=cn; alitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; tg=0; enc=bTeKT1FrTi45FehaNuVQVnRHvlrFNHHWtkzSZWhGKSaNHUh%2BtvpAQVGkB1ZW4SlSOqxP0eewIv9do9cZPGzsBw%3D%3D; miid=1114728529241985104; lastalitrackid=www.taobao.com; ctoken=Q4nfiZp17hwgVAZZs9O7rhllor; v=0; publishItemObj=Ng%3D%3D; tracknick=%5Cu6211%5Cu5BB6%5Cu6709%5Cu4E2A%5Cu5C0F%5Cu53C1; lgc=%5Cu6211%5Cu5BB6%5Cu6709%5Cu4E2A%5Cu5C0F%5Cu53C1; dnk=%5Cu6211%5Cu5BB6%5Cu6709%5Cu4E2A%5Cu5C0F%5Cu53C1; UM_distinctid=16b69d15bb62e1-075edf2422941c-37647e03-fa000-16b69d15bb86f; linezing_session=05uzR3j2JTkkmfeGzMr3EbDL_15631978118805oDc_1; unb=367907686; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dBy3K3KI6B6mLoI3w%3D&id2=UNaA2VQJQfZi&nk2=rUsy40XCBCWmUCiR; csg=399bfac7; cookie17=UNaA2VQJQfZi; skt=e76392c3182cdb7e; existShop=MTU2NTkxODQ4NA%3D%3D; uc4=nk4=0%40r7q0tQjwtuch5zoszhoIQPZ1KJmbknY%3D&id4=0%40UgGJjJ70fInJEpsxgcQLG7fgxKw%3D; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%8F%816f; _nk_=%5Cu6211%5Cu5BB6%5Cu6709%5Cu4E2A%5Cu5C0F%5Cu53C1; cookie1=WqVZK0ID%2FrxXxpd0KxuWOGAmOattzhn83pTrcXIXgbo%3D; mt=ci=89_1; JSESSIONID=3529050E90936CDC3F7BE26AFF5B78D5; uc1=cart_m=0&cookie14=UoTaHYefz%2FIh0A%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&tag=8&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; isg=BL6-xnyLbz9BLLq8WxRqLUWeD9LAV7BuQ8Kd8GjHIIH8C17l0I6DiYvph5diM3qR; l=cBTPmUMcvtsWaVyDBOCgVuIJHf_TIIRAguPRwpnwi_5K168_MlbOk8yc3FJ6cjWd9aTB4coM9BJ9-etXiKy06Pt-g3fP.'
        }
        r = requests.get(url, headers=hearder)
        r.raise_for_status()
        r.encoding = r.raise_for_status()
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([title, price])
    except:
        print('解析错误')


def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for i in ilt:
        count += 1
        print(tplt.format(count, i[1], i[0]))


def main():
    goods = '王力安全门'
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    try:
        html = getHTMLText(start_url)
        parsePage(infolist, html)
    except:
        print('出错了')
    printGoodsList(infolist)


if __name__ == '__main__':
    main()

