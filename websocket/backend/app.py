import asyncio
import websockets
import io
from PIL import Image, ImageMode
from scipy.spatial import distance
from imutils import face_utils
import imutils
import numpy as np
#A series of convenience functions to make basic image processing functions such as translation, 
#rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, 
#and much more easier with OpenCV and both Python 2.7 and Python 3.
import dlib
#WINDOWS: pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
import cv2

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

thresh = 0.25
frame_check = 40
#initializing dlib's face detector (HOG-based) and then creating the facial landmark predictor.
detect = dlib.get_frontal_face_detector() #it returns the default face detector.
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #it takes in an image region containing some object and outputs a set of point locations that define the pose of the object.

#extracting the left and right eye's (x, y)-coordinates.
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



def executeOpenCV(frame, flag):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #.cvtColor():Converts BGR image into GRAY image.
    subjects = detect(gray, 0) #detects faces in the grayscale frame.
    #looping over the face detections.
    for subject in subjects:
            shape = predict(gray, subject) #determining the facial landmarks for the face region.
            shape = face_utils.shape_to_np(shape) #converting the facial landmark (x, y)-coordinates to a NumPy array.
            #extracting the left and right eye coordinates.
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            #using the coordinates for calculating aspect ratio for both eyes.
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            #calculating average aspect ratio.
            ear = (leftEAR + rightEAR) / 2.0
            #computing the convex hull for the left and right eye(convex hull:-the smallest convex shape enclosing a given shape).
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            #visualizing each of the eyes.
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1) #.drawContours():-Draws contours outlines or filled contours.
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1) #(thickness==negative):-the contour interiors are drawn.(maxLevel==1):-the 
                                                                        #function draws the contour(s) and all the nested contours.
            #if ear < thresh:
            if (leftEAR < thresh) | (rightEAR < thresh):
                flag += 2 #incrementing the blink frame counter.
                cv2.putText(frame, '{}'.format(flag), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                if flag >= frame_check:
                    #cv2.putText(image,text,org,fontFace,fontScale,color,thickness)
                    cv2.putText(frame, "   *************ACORDA!****************", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) #to draw a text string.
                    cv2.putText(frame, "****************ACORDA!****************", (10, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                flag= 0

            return frame, flag


async def time(websocket, path):
    flag=0
    while True:
        message = await websocket.recv()
        #pil_image = Image.open(io.BytesIO(message)) #.convert('RGB')
        #image.show()
        #open_cv_image = np.array(pil_image) 
        #print(open_cv_image)
        #open_cv_image = open_cv_image[:, :, ::-1].copy() 
        # now do with your images whatever you want. I used image.show to check it, it was spamming my monitor
        frame = imutils.resize(np.array(Image.open(io.BytesIO(message))) , width=450) #resizing image to maximum of 450 pixels. cv2.resize() can also do the same but in order to
        #maintain aspect ratio imutils.resize() is used.
        try:
            frame, flag = executeOpenCV(frame, flag)
        except: print('Aproxime-se da camer')
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            #to cleanup the camera and close any open windows
            cv2.destroyAllWindows()
            break

        cv2.imshow("Frame", frame)
        
start_server = websockets.serve(time, "127.0.0.1", 3333)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()