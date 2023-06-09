from traceback import print_tb
import cv2
import time
from Solu.utils.ObjectDetectorOptions import *
import numpy as np
from threading import Thread

DETECTION_THRESHOLD = 0.1
options = ObjectDetectorOptions(num_threads=4,
                                score_threshold=DETECTION_THRESHOLD)
detector = ObjectDetector(model_path="Solu/assets/plant.tflite", options=options)

class WebcamStream:
    def __init__(self, stream_id=0):
        self.stream_id = stream_id  # default is 0 for primary camera

        # opening video capture stream
        self.vcap = cv2.VideoCapture(self.stream_id)
        if self.vcap.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(5))
        print("FPS of webcam hardware/input stream: {}".format(fps_input_stream))

        # reading a single frame from vcap stream for initializing
        self.grabbed, self.frame = self.vcap.read()
        if self.grabbed is False:
            print('[Exiting] No more frames to read')
            exit(0)

        # self.stopped is set to False when frames are being read from self.vcap stream
        self.stopped = True

        # reference to the thread for reading next available frame from input stream
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads keep running in the background while the program is executing

    # method for starting the thread for grabbing next available frame in input stream
    def start(self):
        self.stopped = False
        self.t.start()

        # method for reading next frame

    def update(self):
        while True:
            if self.stopped is True:
                break
            self.grabbed, self.frame = self.vcap.read()
            if self.grabbed is False:
                print('[Exiting] No more frames to read')
                self.stopped = True
                break
        self.vcap.release()

    # method for returning latest read frame
    def read(self):
        return self.frame

    # method called to stop reading frames
    def stop(self):
        self.stopped = Truefrom traceback import print_tb
2
import cv2
3
import time
4
from Solu.utils.ObjectDetectorOptions import *
5
import numpy as np
6
from threading import Thread
7
​
8
DETECTION_THRESHOLD = 0.1
9
options = ObjectDetectorOptions(num_threads=4,
10
                                score_threshold=DETECTION_THRESHOLD)
11
detector = ObjectDetector(model_path="Solu/assets/plant.tflite", options=options)
12
​
13
class WebcamStream:
14
    def __init__(self, stream_id=0):
15
        self.stream_id = stream_id  # default is 0 for primary camera
16
​
17
        # opening video capture stream
18
        self.vcap = cv2.VideoCapture(self.stream_id)
19
        if self.vcap.isOpened() is False:
20
            print("[Exiting]: Error accessing webcam stream.")
21
            exit(0)
22
        fps_input_stream = int(self.vcap.get(5))
23
        print("FPS of webcam hardware/input stream: {}".format(fps_input_stream))
24
​
25
        # reading a single frame from vcap stream for initializing
26
        self.grabbed, self.frame = self.vcap.read()
27
        if self.grabbed is False:
28
            print('[Exiting] No more frames to read')
29
            exit(0)
30
​
31
        # self.stopped is set to False when frames are being read from self.vcap stream
32
        self.stopped = True
33
​
34
        # reference to the thread for reading next available frame from input stream
35
        self.t = Thread(target=self.update, args=())
36
        self.t.daemon = True  # daemon threads keep running in the background while the program is executing
37
​
38
    # method for starting the thread for grabbing next available frame in input stream
39
    def start(self):
40
        self.stopped = False
41
        self.t.start()
42
​
43
        # method for reading next frame
44
​
45
    def update(self):
46
        while True:
47
            if self.stopped is True:
48
                break
49
            self.grabbed, self.frame = self.vcap.read()
50
            if self.grabbed is False:
51
                print('[Exiting] No more frames to read')
52
                self.stopped = True
53
                break
54
        self.vcap.release()
55
​
56
    # method for returning latest read frame
57
    def read(self):
58
        return self.frame

def gen_frames():
    webcam_stream = WebcamStream(stream_id=0)  # stream_id = 0 is for primary camera
    webcam_stream.start()
    while True:
        try:
            frame = webcam_stream.read()

            # adding a delay for simulating time taken for processing a frame
            # delay value in seconds. so, delay=1 is equivalent to 1 second

            image = cv2.resize(frame, (512, 512))
            image_np = np.asarray(image)
            detections = detector.detect(image_np)
            image_np = visualize(image_np, detections)
            frame = cv2.imencode('.jpg', image_np)[1]
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n'
            key = cv2.waitKey(1)


        except Exception as e:
            print(e)




gen_frames()
