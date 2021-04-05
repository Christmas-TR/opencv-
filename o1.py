import cv2
import numpy as np
# import matplotlib as plt
# import os
#
# #
# # img = cv.imread('pic.jpg',0)
# # cv.imshow('image',img)
# # k = cv.waitKey(0)
# # if k == 27:
# #     cv.destroyAllWindows()
# # elif k == ord('s'):
# #     cv.imwrite('pic.jpg',img)
# #     cv.destroyAllWindows()



# cap = cv2.VideoCapture(0)
#
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destoryAllWindows()



#
# cap = cv2.VideoCapture('pubg.mp4')
#
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destoryAllWindows()


#
# cap = cv2.VideoCapture(0)
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#         out.write(frame)
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()



# img=np.zeros((512,512,3), np.uint8)
# cv2.line(img,(0,0),(511,511),(255,0,0),5)
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# cv2.circle(img,(447,63), 63, (0,0,255), -1)
# cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts=pts.reshape((-1,1,2))
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(0,100,0),2)
#
#
#
# winname = 'example'
# cv2.namedWindow(winname)
# cv2.imshow(winname, img)
# cv2.waitKey(0)
# cv2.destroyWindow(winname)


#
# randomByteArray = bytearray(os.urandom(120000))
# flatnumyarry = np.array(randomByteArray)
#
# grayimge = flatnumyarry.reshape(300,400)
# cv2.imwrite = ('RandomGray.png',grayimge)
#
# brgimge = flatnumyarry.reshape(100,400,3)
# cv2.imwrite = ('RandomColour.png',brgimge)
#
#
# winname = 'example'
# cv2.namedWindow(winname)
# cv2.imshow(winname, grayimge)
# # cv2.imshow(winname, brgimge)
# cv2.waitKey(0)
# cv2.destroyWindow(winname)



#利用摄像头捕获帧流‘10’
# cameraCapture = cv2.VideoCapture(0)
#
# fps = 30
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# )
#
# VideoWriter = cv2.VideoWriter('MyOutputVid.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size
# )
#
# success,frame = cameraCapture.read()
# numFramesRemaining = 10*fps - 1
# while success and numFramesRemaining > 0 :
#     VideoWriter.write(frame)
#     success,frame = cameraCapture.read()
#     numFramesRemaining -= 1
#
# cameraCapture.release()



#
# #mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)
# # 创建图像与窗口并将窗口与回调函数绑定
# img=np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20)&0xFF==27:
#         break
# cv2.destroyAllWindows()




# 当鼠标按下时变为 True
drawing=False
# 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode=True
ix,iy=-1,-1
# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
# 当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
# 当鼠标左键按下并移动是绘制图形。 event 可以查看移动， flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线， 3 代表了笔画的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
                # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
# 当鼠标松开停止绘画。
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False
        # if mode==True:
            # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
            # cv2.circle(img,(x,y),5,(0,0,255),-1)

img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('m'):
        mode=not mode
    elif k==27:
        break

























