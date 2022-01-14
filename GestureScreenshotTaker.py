import cv2
import time
import HandTrackingModule as htm
import math
import pyautogui

##############################
wCam, hCam = 1080, 720
##############################
count = 0
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # video object created
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(detectionCon=0.7)
while True:
    success, img = cap.read()  # this will give frame
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2-x1, y2-y1)
        print(length)
        if length < 30:
            count += 1
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r"C:/Users/KIIT/PycharmProjects/handtrackingbasics/takenScreenshots/" +str(count)+ ".png")

    cTime = time.time()  # getting current time
    fps = 1 / (cTime - pTime)  # getting fps
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
                3)  # placing the fps meter on
    # on the screen with inbuilt parameters
    cv2.imshow("Image", img)  # for showing in the webcam to run it
    cv2.waitKey(1)