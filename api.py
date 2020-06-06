import requests
import json
import base64

def startlogo():
    print('''
    $$$$$$$$\           $$$$$$$$\            $$$$$$\            $$\ 
$$  _____|          $$  _____|          $$  __$$\           \__|
$$ |       $$$$$$\  $$ |       $$$$$$\  $$ /  $$ | $$$$$$\  $$\ 
$$$$$\    $$  __$$\ $$$$$\     \____$$\ $$$$$$$$ |$$  __$$\ $$ |
$$  __|   $$ /  $$ |$$  __|    $$$$$$$ |$$  __$$ |$$ /  $$ |$$ |
$$ |      $$ |  $$ |$$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |
$$ |      \$$$$$$  |$$ |      \$$$$$$$ |$$ |  $$ |$$$$$$$  |$$ |
\__|       \______/ \__|       \_______|\__|  \__|$$  ____/ \__|
                                                  $$ |          
                                                  $$ |          
                                                  \__|        
                                                ''')
def fofasearch(keyword):
    email="" #email
    key="" #key
    target=base64.b64encode(keyword.encode('utf-8')).decode('utf-8')#先转换utf-8格式再加密再转回utf-8
    page="2" #翻页数
    size="100" #每页返回记录数
    url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+target+"&size="+size
    resp = requests.get(url)
    data_model = json.loads(resp.text)  #将请求到的json字符串解码为python对象
    data_url=[]
    fofaurl=open(keyword+'.txt','w+')
    for results in data_model['results']: #取结果列表
        for url in results[0:1]: #取结果列表中的每个列表的url,需要IP则改为[1:2]
            data_url.append(url)   #添加到列表末尾
    for url in data_url:
        fofaurl.write(url+"\n")  #将列表中的url迭代保存到文件对象中并换行
    fofaurl.close()

if __name__ == '__main__':
    startlogo()
    keyword=input('请输入检索内容:')
    fofasearch(keyword)
    print("检索结果已保存至%s.txt文件中"%(keyword))
