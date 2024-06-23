import os

project_path = 'YOUR_PROJECT_LOCATION'
opencv_path = 'YOUR_OPENCV_LOCATION\\opencv\\build\\x64\\vc15\\bin\\'

def run (count, w, h, stage):
    os.system(f'{opencv_path}opencv_createsamples.exe -info {project_path}\\train\\temp\\posdata\\posdata.info -vec {project_path}\\train\\temp\\vec\\detect.vec -bg {project_path}\\train\\temp\\negdata\\negdata.info -num {count} -w {w} -h {h}')
    os.system(f'{opencv_path}opencv_traincascade.exe -data {project_path}\\train\\temp\\xml -vec {project_path}\\train\\temp\\vec\\detect.vec -bg {project_path}\\train\\temp\\negdata\\negdata.info -numPos {count} -numNeg {count*4} -numStages {stage} -featureType HAAR -w {w} -h {h}')