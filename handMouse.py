import cv2
import mediapipe as mp
import pyautogui #for moving cursor

#open camera
cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
#draw landmarks 
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand) #display on frame
            landmarks = hand.landmark
            #iterate and get IDs of landmarks
            for id, landmark in enumerate(landmarks):
                #if id == 8:
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    print(x, y)
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0))
                        index_x = screen_width / frame_width * x #make frame entire screen
                        index_y = screen_height / frame_height * y
                        pyautogui.moveTo(index_x,index_y)
                    if id == 4: #when index finger and thumb close perform click operation
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0))
                        thumb_x = screen_width / frame_width * x 
                        thumb_y = screen_height / frame_height * y
                        print('outside',abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 20:
                            print("click")
                            pyautogui.click()
                            pyautogui.sleep(1)
                        
    #print(hands)
    cv2.imshow('hand mouse', frame)
    cv2.waitKey(1)

