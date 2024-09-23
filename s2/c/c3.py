import turtle as t #导入turtle库，并取别名为s
#自定义函数入口
def draw(r,a,len): #r半径 a角度 len长度
    t.seth(-40) #初始化画笔，并让他朝向40度
    for i in range(len): #循环绘制
        t.circle(r,a) #画圆,半径为r，角度为a
        t.circle(-r,a) #画圆,半径为-r，角度为a   r为正时，圆心在画笔上方；r为负时，圆心在画笔下方
    t.circle(r,a / 2) # 画圆, 半径为r，角度为a/2
    t.fd(r) # 画一条r dpi的直线
    t.circle(16,180) # 画圆，半径为16dpi，角度为180度
    t.fd(40 * 2 / 3) # 画一条26dpi的直线
#主函数入口
if __name__=='__main__':
    t.setup(650,350,200,200) #设置画布大小为650*350，距离(0,0)有长200宽200的偏移量
    t.penup() # 抬起画笔
    t.fd(-255) # 画笔移动-255dpi（正数向前，负数向后）
    t.pendown() # 落笔
    t.pensize(25) # 画笔粗细为25dpi
    t.pencolor("linen") # 画笔颜色为亮灰
    draw(40,80,4) # 绘制尺寸为40，角度为80，长度为4
    t.done() #显示窗格