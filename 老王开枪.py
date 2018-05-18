class Person(object):
    '''人的类'''
    def __init__(self, name):
        self.name = name
        self.gun = None
        self.hp = 100

    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有枪%s"%(self.name,self.hp, self.gun)
        else:
            if self.hp >0:
                return "%s的血量为%d,他没有枪%s"%(self.name, self.hp, self.gun)
            else:
                return "%s 已挂"%self.name

    def install_zidan(self, dan_jia_temp, zidan_temp):
        '''把子弹安装到弹夹中'''
        dan_jia_temp.save_zidan(zidan_temp)

    def install_danjia(self, gun_temp, danjia_temp):
        '''将弹夹安装在枪中'''
        gun_temp.save_danjia(danjia_temp)

    def naqiang(self, gun_temp):
        '''老王拿起一把枪'''
        self.gun = gun_temp

    def kou_ban_ji(self, diren):
        '''让枪发射子弹打敌人'''
        self.gun.fire(diren)

    def diao_xue(self, sha_shang_li):
        self.hp -= sha_shang_li

class Gun(object):
    '''枪类'''
    def __init__(self,name):
        self.name = name
        self.danjia = None

    def save_danjia(self, danjia_temp):
        self.danjia = danjia_temp

    def fire(self, diren):
        zidan_temp = self.danjia.tanchu_zidan()
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print("弹夹中没有子弹了！")

    def __str__(self):
        if self.danjia:
            return "枪的信息为:%s,%s" % (self.name,self.danjia )
        else:
            return "枪的信息为:%s,这把枪没有弹夹"%(self.name)


class Danjia(object):
    '''弹夹类'''
    def __init__(self, max_num):
        self.max_num = max_num
        self.zidan_list = []

    def save_zidan(self, zidan_temp):
        self.zidan_list.append(zidan_temp)

    def tanchu_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

    def __str__(self):
        return "弹夹的信息为:%d/%d"%(len(self.zidan_list), self.max_num)

class Zidan(object):
    def __init__(self, sha_shang_li):
        self.sha_shang_li = sha_shang_li

    def dazhong(self, diren):
        diren.diao_xue(self.sha_shang_li)

def main():
    pass

#创建一个老王对象
laowang = Person("老王")
#创建一个枪对象
ak47 = Gun("AK47")
#创建一个弹夹
dan_jia = Danjia(20)
#创建一些子弹
for i in range(15):
    zi_dan = Zidan(10)
#创建一个敌人
    gebi_laosong = Person("隔壁老宋")
#老王把子弹安装到弹夹中
    laowang.install_zidan(dan_jia, zi_dan)
#老王把弹夹安装在枪中
    laowang.install_danjia(ak47, dan_jia)

#测试弹夹的信息
#print (dan_jia)
#测试枪的信息
#print(ak47)
#老王拿枪
laowang.naqiang(ak47)
#测试老王对象
print(laowang)
#老王开枪打敌人
laowang.kou_ban_ji(gebi_laosong)
print(gebi_laosong)
print(laowang)

if __name__ == "__main":
    main()
