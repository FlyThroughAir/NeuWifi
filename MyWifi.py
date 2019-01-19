from MyCrawl import MyCrawl
from LoadData import LoadData
from MyEmail import MyEmail
import random
import math
import time
import os
import datetime


class MyWifi(MyCrawl):

    def __init__(self):

        self.headerFiles={
            "abslogout": "conf/wifi_abslogout_header",
            "login": "conf/wifi_login_header",
            "auth": "conf/wifi_auth_header",
            "logout": "conf/wifi_logout_header"
    }
        self.paramFiles={
            "abslogout": "conf/wifi_abslogout_params",
            "login": "conf/wifi_login_params",
            "auth": "conf/wifi_auth_params",
            "logout": "conf/wifi_logout_params"
        }

        self.outFiles = {
            "abslogout": "out/abslogout.txt",
            "login": "out/login.txt",
            "auth": "out/auth.txt",
            "logout": "out/logout.txt"
        }

        ld = LoadData()
        urls = ld.loadUrls('conf/urls')
        self.urls={
            "abslogout":urls['abslogout'],
            "login": urls['login'],
            "logout": urls['logout'],
            "auth": urls['auth']
        }

        edatas = ld.loadParams('conf/email',split="=")
        self.eml = MyEmail()
        self.eml.setUser(edatas['msg_from'],edatas['msg_to'],edatas['passwd'])

        # self.absLogoutUrl = "http://ipgw.neu.edu.cn/include/auth_action.php"
        # self.loginUrl = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&"
        # self.logoutUrl = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&"
        # self.authUrl = "http://ipgw.neu.edu.cn/include/auth_action.php?"

        self.ld = ld
        if not os.path.exists("out"):
            os.mkdir('out')
        if not os.path.exists('conf'):
            print("配置文件损坏，无法运行，请自行查看代码修复！很容易")




    def __format_time__(self, sec):
        sec = int(float(sec))
        h = int(math.floor(sec // 3600))
        m = int(math.floor((sec % 3600) // 60))
        s = sec % 3600 % 60
        out = ""
        if (h < 10):
            out += "0" + str(h) + " : "
        else:
            out += str(h) + " : "

        if (m < 10):
            out += "0" + str(m) + " : "
        else:
            out += str(m) + " : "

        if (s < 10):
            out += "0" + str(s) + ""
        else:
            out += str(s) + ""

        return out

    def login(self):

        ld = self.ld
        url = self.urls['login']
        headerFiles = self.headerFiles
        paramFiles = self.paramFiles
        outFiles = self.outFiles

        headers = ld.loadHeaders(headerFiles['login'])
        params = ld.loadParams(paramFiles['login'],split=":")
        #the_page = self.getHtlPost(url=url, headers=headers, params=params)
        the_page = self.getHtmlUrllib(url,params,headers)
        html = str(the_page.decode(encoding='utf8'))
        ld.saveFile(html, outFiles['login'])

        index = html.find("连接网络(Connect)")
        if index>0:
            return False
        else:
            return True



    def get_auth_info(self):

        ld = self.ld
        url = self.urls['auth']
        headerFiles = self.headerFiles
        paramFiles = self.paramFiles
        outFiles = self.outFiles

        k = math.floor(random.random() * (100000 + 1))
        url = url + "k=" +str(k)
        params = ld.loadParams(paramFiles['auth'],split=":")
        params['key']=k
        headers = ld.loadHeaders(headerFiles['auth'])
        self.getHtmlUrllib(url,params,headers)
        #the_page = self.getHtlPost(url=url, headers=headers, params=params)
        the_page = self.getHtmlUrllib(url, params, headers)
        html = the_page.decode(encoding='utf8')
        if len(html)>0:#zxvf zcvf
            infos = []
            items = html.split(',')
            if items!=None:
                infos.append("已用流量: "+str(int(items[0])//1000//1000)+"MB")
                infos.append("已用时长: "+self.__format_time__(items[1]))
                infos.append("帐户余额:	"+str(items[2]))
                infos.append("IP地址:	" + str(items[-1]))
                ld.saveLines(infos,outFiles['auth'])
                ip_addr = items[-1]
                outParams = ld.loadParams(paramFiles['logout'],':')
                lines=[]
                for k,v in outParams.items():
                    if k=='user_ip':
                        lines.append(k+": "+ip_addr)
                    else:
                        lines.append(k + ": " + v)
                ld.saveLines(lines,paramFiles['logout'])
                content = "\n".join(lines)
                self.eml.setContent("实验室服务器信息",content)
                self.eml.send()


        #print(the_page)
        #ld.saveFile(html,'auth.txt')


    def absLogout(self):
        ld = self.ld
        url = self.urls['abslogout']
        headerFiles = self.headerFiles
        paramFiles = self.paramFiles
        outFiles = self.outFiles

        headers = ld.loadHeaders(headerFiles['abslogout'])
        params = ld.loadParams(paramFiles['abslogout'], ':')

        # the_page = self.getHtlPost(url=url, headers=headers, params=params)
        the_page = self.getHtmlUrllib(url, params, headers)
        html = the_page.decode(encoding='utf8')
        # print(html)
        ld.saveFile(html, outFiles['abslogout'])


    def logout(self):
        ld = self.ld
        url = self.urls['logout']
        headerFiles = self.headerFiles
        paramFiles = self.paramFiles
        outFiles = self.outFiles

        headers = ld.loadHeaders(headerFiles['logout'])
        params = ld.loadParams(paramFiles['logout'],':')
        #the_page = self.getHtlPost(url=url, headers=headers, params=params)
        the_page = self.getHtmlUrllib(url, params, headers)
        html = the_page.decode(encoding='utf8')
        #print(html)
        ld.saveFile(html,outFiles['logout'])


    def test(self):
        headerFiles = self.headerFiles
        paramFiles = self.paramFiles
        outFiles = self.outFiles

        for k in headerFiles:
            print(k,headerFiles[k],paramFiles[k],outFiles[k])



def login():
    mw = MyWifi()
    print("开始连接！")
    stime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("当前时间:", stime)
    if not mw.login():
        print("已有在线，断开连接！")
        mw.absLogout()
        time.sleep(1)
        print("再次开始连接！")
        mw.login()

    time.sleep(1)
    mw.get_auth_info()
    print("连接完成！")


def logout():
    mw = MyWifi()
    print("断开连接！")
    stime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("当前时间:", stime)
    if not mw.login():
        print("已有在线，断开连接！")
        mw.absLogout()
    print("已经断开！")


if __name__ == '__main__':
    import argparse
    switch  = {'login':login, 'logout':logout}
    parser = argparse.ArgumentParser()
    #print("please input  'python MyWifi -h' to call for help")
    parser.add_argument('--type', type=str, default='login', help='input "login" or "logout" ')
    args = parser.parse_args()
    fun = switch[args.type]
    fun()



# 使用crontab来进行系统定时启动操作。、、、、

