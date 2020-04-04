from eyes import calcula_olhos
from imutils import face_utils
import dlib
import cv2
#from mongodb import QExpertDB
#handleDB = QExpertDB()
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def executeOpenCV(frame, flag):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0) #detecta faces no frame gray.
    for subject in subjects:
        shape = predict(gray, subject) #determina as landmarks facias para a região do rosto.
        shape = face_utils.shape_to_np(shape) #converte as coordenadas das landmarks faciais (x, y) em NumPy array.
        leftEAR, rightEAR, leftEyeHull, rightEyeHull, frame, flag = calcula_olhos(shape, frame, flag)
        #handleDB.atualiza({'score_name': 'rafael_2', 'score_value': flag, 'cost': 0.007})
        cv2.imshow("Frame", frame)
        return frame

#WINDOWS: pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f