from Detector import *

detector = Detector(model_type="PS")   # pass here which type of task you want to do like (for object Detection OD), (for instance Segmentation IS), KP, PS


detector.onImage("data/image1.jpg")
detector.onVideo("data/video.mp4")
