#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


t = Tk()
# t = Tk()
t.title('现代检测技术v1 ') 
#创建两个frame容器
frmL_data = Frame(width=360, height=480,)
frmL_result = Frame(width=520, height=480)

frmL_result.grid(row=0, column=0)
frmL_data.grid(row=0, column=1)

# 添加标签
# 数据点头部
label_xtop = Label(frmL_data,text="数据点部分:",height = 2,width = 10)
label_xtop.grid(row=0,column=0)
# data x部分标签
label_x1 = Label(frmL_data,text="x1:",width = 10)
label_x2 = Label(frmL_data,text="x2:",width = 10)
label_x3 = Label(frmL_data,text="x3:",width = 10)
label_x4 = Label(frmL_data,text="x4:",width = 10)
label_x5 = Label(frmL_data,text="x5:",width = 10)

label_x1.grid(row=1,column=0)
label_x2.grid(row=2,column=0)
label_x3.grid(row=3,column=0)
label_x4.grid(row=4,column=0)
label_x5.grid(row=5,column=0)

# data y部分标签
label_y1 = Label(frmL_data,text="y1:",width = 10)
label_y2 = Label(frmL_data,text="y2:",width = 10)
label_y3 = Label(frmL_data,text="y3:",width = 10)
label_y4 = Label(frmL_data,text="y4:",width = 10)
label_y5 = Label(frmL_data,text="y5:",width = 10)

label_y1.grid(row=1,column=2)
label_y2.grid(row=2,column=2)
label_y3.grid(row=3,column=2)
label_y4.grid(row=4,column=2)
label_y5.grid(row=5,column=2)

# ab 头部
label_abtop = Label(frmL_data,text = "参数部分",height = 2,width = 10)
label_abtop1 = Label(frmL_data,text = "(y = a + bx)",height = 2,width = 10)
label_abtop.grid(row=6,column=0)
label_abtop1.grid(row=6,column=1)

# ab a部分标签
label_L1 = Label(frmL_data,text = "L1:  a =",width = 10)
label_L2 = Label(frmL_data,text = "L2:  a =",width = 10)
label_L3 = Label(frmL_data,text = "L3:  a =",width = 10)
label_L4 = Label(frmL_data,text = "L4:  a =",width = 10)
label_L5 = Label(frmL_data,text = "L5:  a =",width = 10)

label_L1.grid(row=7,column=0)
label_L2.grid(row=8,column=0)
label_L3.grid(row=9,column=0)
label_L4.grid(row=10,column=0)
label_L5.grid(row=11,column=0)

# ab b部分标签
label_b1 = Label(frmL_data,text = "b=",width = 10)
label_b2 = Label(frmL_data,text = "b=",width = 10)
label_b3 = Label(frmL_data,text = "b=",width = 10)
label_b4 = Label(frmL_data,text = "b=",width = 10)
label_b5 = Label(frmL_data,text = "b=",width = 10)

label_b1.grid(row=7,column=2)
label_b2.grid(row=8,column=2)
label_b3.grid(row=9,column=2)
label_b4.grid(row=10,column=2)
label_b5.grid(row=11,column=2)

# 添加输入框
# x部分输入
input_x1 = Entry(frmL_data,width =10)
input_x2 = Entry(frmL_data,width =10)
input_x3 = Entry(frmL_data,width =10)
input_x4 = Entry(frmL_data,width =10)
input_x5 = Entry(frmL_data,width =10)

# 设置x默认输入值
input_x1.insert(0, 2)
input_x2.insert(0, 4)
input_x3.insert(0,6)
input_x4.insert(0, 8)
input_x5.insert(0, 10)

# 布局
input_x1.grid(row=1,column=1)
input_x2.grid(row=2,column=1)
input_x3.grid(row=3,column=1)
input_x4.grid(row=4,column=1)
input_x5.grid(row=5,column=1)

# y部分输入
input_y1 = Entry(frmL_data,width =10)
input_y2 = Entry(frmL_data,width =10)
input_y3 = Entry(frmL_data,width =10)
input_y4 = Entry(frmL_data,width =10)
input_y5 = Entry(frmL_data,width =10)

# 设置y默认输入值
input_y1.insert(0, 10.046)
input_y2.insert(0, 20.09)
input_y3.insert(0, 30.155)
input_y4.insert(0, 40.125)
input_y5.insert(0, 50.074)


# 布局
input_y1.grid(row=1,column=3)
input_y2.grid(row=2,column=3)
input_y3.grid(row=3,column=3)
input_y4.grid(row=4,column=3)
input_y5.grid(row=5,column=3)

# a部分输入
input_a1 = Entry(frmL_data,width =10)
input_a2 = Entry(frmL_data,width =10)
input_a3 = Entry(frmL_data,width =10)
input_a4 = Entry(frmL_data,width =10)
input_a5 = Entry(frmL_data,width =10)

# 设置y默认输入值
input_a1.insert(0, 0.08)
input_a2.insert(0, 0.07)
input_a3.insert(0, 0.12)
input_a4.insert(0, -0.05)
input_a5.insert(0, 0.07)

input_a1.grid(row=7,column=1)
input_a2.grid(row=8,column=1)
input_a3.grid(row=9,column=1)
input_a4.grid(row=10,column=1)
input_a5.grid(row=11,column=1)

# b部分输入
input_b1 = Entry(frmL_data,width =10)
input_b2 = Entry(frmL_data,width =10)
input_b3 = Entry(frmL_data,width =10)
input_b4 = Entry(frmL_data,width =10)
input_b5 = Entry(frmL_data,width =10)

# 设置y默认输入值
input_b1.insert(0,5.02 )
input_b2.insert(0,5.05 )
input_b3.insert(0,4.95 )
input_b4.insert(0, -4.95)
input_b5.insert(0, 5.00)

input_b1.grid(row=7,column=3)
input_b2.grid(row=8,column=3)
input_b3.grid(row=9,column=3)
input_b4.grid(row=10,column=3)
input_b5.grid(row=11,column=3)

# TEXT控件
# frmL_iresult文本控件，用于插入图片和显示结果
text_result = Text(frmL_result,width=500,height=320)
text_result.grid(row=0,column=0)


#获取输入值x,y,a,b
def get_data():
    x = []
    y = []
    a = []
    b = []
    x.append(float(input_x1.get()))
    x.append(float(input_x2.get()))
    x.append(float(input_x3.get()))
    x.append(float(input_x4.get()))
    x.append(float(input_x5.get()))
#     x.append(input_x1.get())
#     x.append(input_x2.get())
#     x.append(input_x3.get())
#     x.append(input_x4.get())
#     x.append(input_x5.get())

    y.append(float(input_y1.get()))
    y.append(float(input_y2.get()))
    y.append(float(input_y3.get()))
    y.append(float(input_y4.get()))
    y.append(float(input_y5.get()))
#     y.append(input_y1.get())
#     y.append(input_y2.get())
#     y.append(input_y3.get())
#     y.append(input_y4.get())
#     y.append(input_y5.get())
    
#     a.append(float(input_a1.get()))
#     a.append(float(input_a2.get()))
#     a.append(float(input_a3.get()))
#     a.append(float(input_a4.get()))
#     a.append(float(input_a5.get()))
    #由于参数可能存在空值，这里以字符型读取
    a.append(input_a1.get())
    a.append(input_a2.get())
    a.append(input_a3.get())
    a.append(input_a4.get())
    a.append(input_a5.get())
    
#     b.append(float(input_b1.get()))
#     b.append(float(input_b2.get()))
#     b.append(float(input_b3.get()))
#     b.append(float(input_b4.get()))
#     b.append(float(input_b5.get()))
    
    b.append(input_b1.get())
    b.append(input_b2.get())
    b.append(input_b3.get())
    b.append(input_b4.get())
    b.append(input_b5.get())
    return x,y,a,b


#计算参数a，b下的残余误差平方和
def loss(x,y,a,b):
    loss_y = []
    sum_loss = 0
    for i,j in zip(x,y):
#         print(i,j,j-(a+b*i))
        loss_y.append((j-(a+b*i))*(j-(a+b*i)))#残余误差平方
    #残余误差平方和
    for i in loss_y:
        sum_loss += i
    return sum_loss


# 获取所有参数下的残余误差平方和
def all_loss(x,y,a,b):
    all_loss_y = []
    num_ab = []  #记录有效的a，b下标len
    len = 0
    data = get_data()#获取x，y的值，用于调用求残余误差的函数
    for i,j in zip(a,b):
        if i!='' and j!='':
#             print ("if")
            all_loss_y.append(loss(x,y,float(i),float(j)))
            num_ab.append(len)
        len += 1 
    return (all_loss_y,num_ab) 


# 创建函数图,num为直线下标，
def creat_phto(x,y,a,b,num):
    # 动态创建变量
    createVar = locals()
    #直线横坐标的起点，终点
    x1 = np.arange(min(x),max(x),0.01)
    plt.title("function plots")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(x,y, s=20, c="#ff1212", marker='x')
    for i,j,NUM in zip(a,b,num):
        createVar[str(i)] = i+j*x1    #直线表达式
        plt.plot(x1, createVar[str(i)],label='L{}'.format(NUM+1))#画线
    plt.legend(loc='upper left')
    plt.savefig("image.png")
#     plt.show()
    plt.close()
    img = Image.open("image.png")
    img = img.resize((500, 300),Image.ANTIALIAS)
    img.save("3.png")
    
#定义输出结果区函数
def output():
    
    #获取输入x y的值
    data = get_data()
    loss = all_loss(data[0],data[1],data[2],data[3])
#     print (loss)
    #a,b列表用于画图
    a = []
    b = []
    if len(loss[0])==0:
#         print ("0")
        return 0
    else:
        
        text = []
        for i,j in zip(loss[0],loss[1]):
            text.append("L{}:y = {} + {}x  残余误差平方和为：{}".format(j+1,data[2][j],data[3][j],i))
            a.append(float(data[2][j]))
            b.append(float(data[3][j]))
        num = 0
        min_loss = loss[0][0]
        for i in range (len(loss[0])):
            
            if min_loss>loss[0][i]:
                min_loss = loss[0][i]
                num = i
        text.append ("所以，最佳直线为L{}".format(str(loss[1][num]+1)))
        creat_phto(data[0],data[1],a,b,loss[1])
        return text
# Text插入图片




def show():
    try:
        text_result.delete('1.0','end')
        text = output()
        if text==0:
            text_result.insert(END,"\n\n\n\n\n\n   无数据，请先输入数据，至少需要一组参数 a，b")
        else:
            #INSERT表示在光标位置插入内容
            text_result.insert(END,"   ")
            #全局变量才能在文本框中插入图片
            global photo   
            photo = PhotoImage(file='3.png')
            #插入图片
            text_result.image_create(END,image=photo)
            #Text插入文本
            text_result.insert(END,"\n")
            for i in text:
                text_result.insert(END,"           "+i+"\n")
    except BaseException:
        text_result.delete('1.0','end')
        text_result.insert(END,"\n\n\n\n\n\n   异常，请检查数据，参数部分至少需要一组参数 a，b，数据部分需要全部填写 ")

    

# #添加按钮
btnSend = Button(frmL_data, text=' 确 定 ',command=show,width=10,height=2)#在frmL_result容器中添加
btnSend.grid(row=12,column=1)

#固定容器大小
frmL_data.grid_propagate(0)
frmL_result.grid_propagate(0)

mainloop()


# In[ ]:




