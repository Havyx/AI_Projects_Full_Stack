import sys
from eyes import calcula_olhos
from imutils import face_utils
import dlib
#WINDOWS: pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
import cv2

#initializing dlib's face detector (HOG-based) and then creating the facial landmark predictor.
detect = dlib.get_frontal_face_detector() #it returns the default face detector.
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #it takes in an image region containing some object and outputs a set of point locations that define the pose of the object.

def executeOpenCV(frame, flag):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #.cvtColor():Converts BGR image into GRAY image.
    subjects = detect(gray, 0) #detects faces in the grayscale frame.
    #looping over the face detections.
    for subject in subjects:
        
        shape = predict(gray, subject) #determining the facial landmarks for the face region.
        shape = face_utils.shape_to_np(shape) #converting the facial landmark (x, y)-coordinates to a NumPy array.
        #extracting the left and right eye coordinates.

        leftEAR, rightEAR, leftEyeHull, rightEyeHull, frame, flag = calcula_olhos(shape, frame, flag)

        return frame, flag