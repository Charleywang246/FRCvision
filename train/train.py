import cv2
import numpy as np
import os
import shutil
import train.command as command
import warnings

project_path = 'D:\\Desktop\\programming\\python\\FRCvision\\'
img_folder = 'resources\\images'
temp_folders = [
    'train\\temp\\posdata\\'
    ,'train\\temp\\negdata\\'
    ,'train\\temp\\vec\\'
    ,'train\\temp\\xml\\'
]

def mouseclick_callback (event, x, y, flags, params):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points[0] = x,y
        if not points[1][0] and not points[1][1]: points[1] = x,y
    if event == cv2.EVENT_RBUTTONDOWN:
        points[1] = x,y

def slice ():
    global points
    
    try: shutil.rmtree('train\\temp')
    except: pass
    
    for folder in temp_folders:
        os.makedirs(folder)

    points = np.zeros((2,2), np.int16)

    cv2.namedWindow('img', 0)
    cv2.setMouseCallback('img', mouseclick_callback)

    for filename in os.listdir(img_folder):
        img = cv2.imread(os.path.join(img_folder, filename))
        if img is None:
            warnings.warn(f'invaild image file: {os.path.join(img_folder, filename)}')
            continue
        if img.shape[0] > 900 or img.shape[1] > 1600:
            scale = max(img.shape[0]/900, img.shape[1]/1600)
            img = cv2.resize(img, (int(img.shape[1]/scale), int(img.shape[0]/scale)))
        
        while True:
            cv2.imshow('img', cv2.rectangle(np.copy(img), points[0], points[1], (0,0,255), 2))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x1,y1 = points[0]
        x2,y2 = points[1]
        if not x1 or not x2 or not y1 or not y2 or not x1-x2 or not y1-y2:
            continue
        posinfo = open(f'{temp_folders[0]}posdata.info', 'a')
        neginfo = open(f'{temp_folders[1]}negdata.info', 'a')
        cv2.imwrite(os.path.join(temp_folders[0],filename), gray[y1:y2, x1:x2])
        posinfo.write(f'{filename} 1 0 0 {x2-x1} {y2-y1}\n')
        cv2.imwrite(f'{temp_folders[1]}1{filename}', gray[:y1, x1:x2])
        neginfo.write(f'{project_path}{temp_folders[1]}1{filename}\n')
        cv2.imwrite(f'{temp_folders[1]}2{filename}', gray[y2:, x1:x2])
        neginfo.write(f'{project_path}{temp_folders[1]}2{filename}\n')
        cv2.imwrite(f'{temp_folders[1]}3{filename}', gray[:, :x1])
        neginfo.write(f'{project_path}{temp_folders[1]}3{filename}\n')
        cv2.imwrite(f'{temp_folders[1]}4{filename}', gray[:, x2:])
        neginfo.write(f'{project_path}{temp_folders[1]}4{filename}\n')
        points = np.zeros((2,2), np.int16)
        posinfo.close()
        neginfo.close()
    
    cv2.destroyAllWindows()

def train (xmlpath):
    command.run(len(os.listdir(temp_folders[0]))-1, 20, 20, 12)
    shutil.copyfile(f'{temp_folders[3]}cascade.xml', f'train\\model\\{xmlpath}')