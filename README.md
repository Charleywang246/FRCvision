## FRCvision by 7130 Future Shock
#### setup
1. download [opencv 3.4.0](https://github.com/opencv/opencv/archive/3.4.0.zip) and unzip
2. git clone
3. change project_path and opencv_path in ./train/command.py (absolute location)

#### usage
in teriminal:
```
cd /d YOUR_PROJECT_LOCATION
python run.py [args]
````
args to choose:
```
options:
  -h, --help            show this help message and exit
  --default             use default setting
  --capture             get images for training
  --slice               slice images to positive and negative images
  --train               train xml model
  --detect              detect objects with webcam
  -xml XMLPATH, --xmlpath XMLPATH
                        port of webcam (default 0)
  -w PORT, --webcam PORT
                        name of xmlfile (default cascade.xml)
```

Explanation:
```
python run.py --default -w PORT -xml NAME
```
do everything
```
python run.py --capture -w PORT
```
Displays the stream from the webcam on the specified port. Press the "x" key to save the current frame to ./resources/images

```
python run.py --slice
```
Slice the image at ./resources/images into a positive image (containing the object to be detected) and a negative image. Left-click to select the upper-left corner of the object, and right-click to select the lower-right corner of the object. The area within the read rectangle will be the positive image.

```
python run.py --train -xml NAME
```
Use positive and negative images to train the xml model, stored in ./train/model. The model name can be set using -xml or --xmlpath (default cascade.xml)
```
python run.py --detect -w PORT -xml NAME
```
Detect objects in the webcam stream on the specified port using the xml model

```
  -xml XMLPATH, --xmlpath XMLPATH
                        port of webcam (default 0)
  -w PORT, --webcam PORT
                        name of xmlfile (default cascade.xml)
```
- xml, xmlpath: \
Set the xml name for training and detection (default cascade.xml). The xml model can be found in ./train/model.
- w, webcam: \
Set the port of the webcam