#!/usr/bin/python
# -*- coding: UTF-8 -*-
##完成版 測試中
import os
import sys
import time
import psutil
import os
import datetime

def delDir(dir,t=80):
    #獲取文件夾下所有文件夾及文件
    files = os.listdir(dir)
    for file in files:
        filePath = dir + "/" + file
        #判斷是否文件
        if os.path.isfile(filePath):
            #最後一次修改時間
            last = int(os.stat(filePath).st_mtime)
            #上一次開啟的时间
            #last = int(os.stat(filePath).st_atime)
            #NOW
            now = int(time.time())
            #刪除過期文件
            if (now - last >= t):
                os.remove(filePath)
                print(filePath + '已過期' +" was removed!")
        elif os.path.isdir(filePath):
            #如果是文件夾繼續刪除
            delDir(filePath,t)
            #如果是空文件夾繼續刪除
            if not os.listdir(filePath):
                os.rmdir(filePath)
                print(filePath + '已過期' +" was removed!")
        
def delDir1(dir,t=80):
    #獲取文件夾下所有文件夾及文件
    list = os.listdir(dir)
    #对文件修改时间进行升序排列
    list.sort(key=lambda fn:os.path.getmtime(dir+'\\'+fn))
    print(list)
    #获取最舊修改时间的文件
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(dir+list[0]))
    #获取文件所在目录
    filePath = os.path.join(dir,list[0])
    print(filePath)
    print("最舊的文件(夾)："+list[0])
    print("时间："+filetime.strftime('%Y-%m-%d %H-%M-%S'))

    if os.path.isfile(filePath):
        #刪除過期文件
            os.remove(filePath)
            print(filePath + " was removed!")
    elif os.path.isdir(filePath):
        #如果是文件夾繼續刪除
        delDir(filePath,t)
        #如果是空文件夾繼續刪除
        if not os.listdir(filePath):
            os.rmdir(filePath)
            print(filePath + " was removed!")
        

def go(pathin):
# if __name__ == '__main__':
    #獲取路徑
    # path =  u"D:\\aviimage\\" 
    path =  u""+ pathin +"" 
    # path = u''path+''
    # path1 = u'D:\\aviimage\\'
    print('監控路徑請確認是否為:',path,'\n')
    #設定過期時間
    # t = int(input('保留近期幾天內的檔案(單位天):'))*86400
    t = 180*86400
    print(t,':秒','\n')
    # t = int(input('保留多久以前的檔案(單位天):'))
    #設定定期清理時間
    # ts = int(input('輸入多久清理一次(單位秒):'))
    ts = 0
    print(ts,':秒','\n')
    # while True:
    localtime = time.asctime( time.localtime(time.time()) )
    print('正在監控硬碟剩餘空間 路徑為:',path)
    #記憶體 內存
    # mem = psutil.virtual_memory()
    # print(mem)
    ##硬碟SD
    disk = psutil.disk_io_counters()
    # print(disk)
    # print(psutil.disk_usage('D:').percent)
    usepercent = psutil.disk_usage('D:').percent
    free = 100-int(usepercent)
    time.sleep(ts)
    # print(usepercent)
    
    if usepercent >= 15 and usepercent < 99:
        delDir(path,t)
        word="Time:"+localtime+'  (嘗試清除中 ,只清除3個月之前檔案','(使用空間:',str(usepercent)+'%','剩餘空間:',str(free)+'%)'
        print(localtime,word,'\n')
        word=str(word)
        f = open('log.txt', 'a')
        f.write(word+"\n")

    elif usepercent >= 99:
        delDir1(path,t)
        word="Time:"+localtime+'  (warning over 90% ,clean the oldest file','(used:',str(usepercent)+'%','free:',str(free)+'%)'
        print(word,'\n')
        word=str(word)
        f = open('log.txt', 'a')
        f.write(word)
        # time.sleep(ts)

    else:
        word="Time:"+localtime+"  (now it's free enough",'(used:',str(usepercent)+'%','free:',str(free)+'%)'
        word=str(word)
        print(word,'\n')
        f = open('log.txt', 'a')
        f.write(word)
        # time.sleep(ts)
    # return usepercent,free