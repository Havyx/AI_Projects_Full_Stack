from imutils import face_utils
import cv2
from scipy.spatial import distance

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

#extracting the left and right eye's (x, y)-coordinates.
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

thresh = 0.25
frame_check = 40

def calcula_olhos(shape, frame, flag):
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    #using the coordinates for calculating aspect ratio for both eyes.
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    #calculating average aspect ratio.
    #ear = (leftEAR + rightEAR) / 2.0
    #computing the convex hull for the left and right eye(convex hull:-the smallest convex shape enclosing a given shape).
    leftEyeHull = cv2.convexHull(leftEye)
    rightEyeHull = cv2.convexHull(rightEye)

    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    #using the coordinates for calculating aspect ratio for both eyes.
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    #calculating average aspect ratio.
    #ear = (leftEAR + rightEAR) / 2.0
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
            #cv2.putText(frame, "****************ACORDA!****************", (10, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        flag= 0

    return leftEAR, rightEAR, leftEyeHull, rightEyeHull, frame, flag