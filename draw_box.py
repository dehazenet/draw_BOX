# -*- coding: utf-8 -*-
import cv2
import numpy as np
import copy
import os 

global width,height,line_width_or,zoom_width,zomm_height,line_width_zoom,line_color
global img_ori,img


## 读取图像，解决imread不能读取中文路径的问题
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img


#mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy
    global width,height,line_width_or,zoom_width,zomm_height,line_width_zoom,line_color
    global img_ori,img
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        img[:,:,:] = img_ori[:,:,:]
        mask = img[iy:iy+width,ix:ix+height,:]
        mask = cv2.resize(mask,(zoom_width,zomm_height))
        cv2.rectangle(mask, (0,0), (zomm_height,zoom_width), line_color, line_width_zoom)
        img[-zomm_height:,-zoom_width:,:] = mask
        cv2.rectangle(img, (ix,iy), (ix+height,iy+width), line_color, line_width_or)

def draw_box_dir(root_dir,number=0):
    global width,height,line_width_or,zoom_width,zomm_height,line_width_zoom,line_color
    global img_ori,img
    path = './results_box/'
    if not os.path.exists(path):
        os.makedirs(path)

    for root, dirs, files in os.walk(root_dir):
        image_to_show = files[number]
        image_dir = root_dir+'/'+ image_to_show
        print(image_dir)
        #image_dir = cv_imread(image_dir)
        img_ori=cv2.imread(image_dir)
        img = copy.deepcopy(img_ori)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)
        while(1):
            cv2.imshow('image',img)
            if cv2.waitKey(20)&0xFF==27:
                print('@@@@@@@@@@@@@@@')
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(20)&0xFF==13:
                cv2.destroyAllWindows()
                for file_number in range(len(files)):
                    image_dir = root_dir+'/'+files[file_number]
                    img = cv2.imread(image_dir)
                    mask = img[iy:iy+width,ix:ix+height,:]
                    mask = cv2.resize(mask,(zoom_width,zomm_height))
                    cv2.rectangle(mask, (0,0), (zomm_height,zoom_width),line_color, line_width_zoom)
                    img[-zomm_height:,-zoom_width:,:] = mask
                    cv2.rectangle(img, (ix,iy), (ix+height,iy+width), line_color, line_width_or)   
                    cv2.imwrite(path+files[file_number],img)
                break
def draw_box_all(or_w,or_h,or_l,zo_w,zo_h,zo_l,r,g,b,dir_root):
    cv2.destroyAllWindows()
    global ix, iy
    global width,height,line_width_or,zoom_width,zomm_height,line_width_zoom,line_color
    global img_ori,img
    width = or_h
    height = or_w
    zoom_width = zo_h
    zomm_height = zo_w
    line_width_or = or_l
    line_width_zoom = zo_l
    line_color = [b,g,r]
    draw_box_dir(dir_root)