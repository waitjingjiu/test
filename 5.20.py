# -*- coding: utf-8 -*-
import sys
import copy

database=[]

#1，从文件中读取图书信息

users=[['admin','admin'],['user','user']]
#flag=False     #状态码，判断是否登录成功



#####################################
#######以下为各个函数#################

def load_database():
    #实现加载数据库

    f=open('D:/tes.txt','w')

    line=f.readline().strip() #先打开第一行

    #filesize=f.st_size #显示加载过程
    # fileload=0

    #循环读取每一行
    while line:
        db=line.strip().split(' ')
        database.append(db)

        #fileload+=len(line)
        # print "Having load %2.2f%"%(fileload/filesize)

        line=f.readline().strip()

    print ('LOAD SUCCESS!')

    print(database)#测试！！！！

    f.close()


def add_database():
    #实现数据录入保存
    book_num=input(u'输入书号：')
    author=input(u'输入作者：')
    title=input(u'输入标题：')
    publishing=input(u'输入出版社：')
    price=input(u'输入定价：')
    database.append([book_num,author,title,publishing,price])
    print ('录入成功！')
    

def text_save():
    f=open('D:/tes.txt','w')
    for i in range(len(database)):
        for j in range(len(database[i])):
            f.write(database[i][j][:])
            f.write(' ')
        f.write('\n')
        f.flush()
    
    f.close()




def fun():
    #实现书籍查询，增加，删除，显示功能

    load_database()
    
    while True:

        print('\n***************************************')

        print('********  增加书籍--------1  **********')

        print('********  删除书籍--------2  **********')

        print('********  查找书籍--------3  **********')

        print('********  修改书籍--------4  **********')

        print('********  查看所有书籍----5  **********')

        print('********  返回主界面------6  **********')

        print('********  退出------------0  **********')

        print('***************************************\n')

        value=int(input('请输入对应数字:'))
        if value==1:
            add_database()
        elif value==2:
            delete_database()
        elif value==3:
            find_database()
        elif value==4:
            change_database()
        elif value==5:
            show_all_database()
        elif value==6:
            main()
        elif value==0:
            text_save()
            sys.exit(0)


def delete_database():
    #实现删除数据功能
    find_database()
    print ("是否确认删除？y/n:")
    xx='n'
    xx=input('')
    if xx=='y':
        del database[find_to_del]
        print ("删除成功！")


    
def show_all_database():
    print ('\n-----------------------------------------------------------------------------------')
    print ('       书号         作者             标题               出版社         定价          ')

    for i in range(len(database)):
        for j in range(len(database[i])):
            print("%10s"%database[i][j],end="")
        print ('\n')
    print ('--------------------------------------------------------------------------------------\n')

find_to_del=None

def find_database():
    print ("搜索书号请输入1")
    print ("搜索作者请输入2")
    print ("搜索标题请输入3")
    
    v=int(input())

    key=input('请输入书号/作者/标题：')
    long=range(len(database))

    global find_to_del

    if v==1:
        for i in long:
            if key==database[i][0]:
                print (database[i][0])
                print (database[i][1])
                print (database[i][2])
                print (database[i][3])
                print (database[i][4])
                find_to_del=i
                print (find_to_del)
                break

        if i==long[-1]:
            print ("无此书号，请重新输入！")
    if v==2:
        for i in long:
            if key==database[i][1]:
                print (database[i][0])
                print (database[i][1])
                print (database[i][2])
                print (database[i][3])
                print (database[i][4])
                find_to_del=i
                print (find_to_del)
                break

        if i==long[-1]:
            print ("无此作者，请重新输入！")
    if v==3:
        for i in long:
            if key==database[i][2]:
                print (database[i][0])
                print (database[i][1])
                print (database[i][2])
                print (database[i][3])
                print (database[i][4])
                find_to_del=i
                print (find_to_del)
                break

        if i==long[-1]:
            print ("无此作者，请重新输入！")
        #此处只查找一此，可加上循环，重复查找！！！
        

        
def change_database():
    #修改数据库内容
    find_database()
    xx='n'
    xx=input('是否确认修改此数据？y/n') 
    if xx=='y':
        database[find_to_del][0]=input('请输入修改后的书号：')    
        database[find_to_del][1]=input('请输入修改后的作者：')    
        database[find_to_del][2]=input('请输入修改后的标题：')    
        database[find_to_del][3]=input('请输入修改后的出版社：')    
        database[find_to_del][4]=input('请输入修改后的定价：')
        print ("修改成功！")



def login():
    #实现登录
    username=input(u'please import name:')
    password=input(u'please import password:')
    if [username,password] in users:
        print ("login success!")
        fun()
    else:
        print ("Your username or password is false.please login again!")

def register():
    #实现注册

    username=input(u'please import name:')
    #此处使用raw_input()函数失败！！


    password=input(u'please import password:')
    users.append([username,password])
    print ("register success!")


def main():
    while 1:
        print('\n\n    **********************')

        print('    *欢迎来到图书管理系统*')

        print('    **********************\n')

        print('*********************************')

        print('******   登录-------1  **********')

        print('******   注册-------2  **********')

        print('******   退出-------0  **********')

        print('*********************************\n')

        v=int(input('请输入对应的数字：'))

        if v==2:

            register()

        elif v==1:

            login()
        elif v==0:
            text_save()

            sys.exit(0)
    


main()

