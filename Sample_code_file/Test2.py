import cv2 as cv
import screeninfo as screen
import numpy as np
import time


#port
Cam_port_0 = 0 #Right Camera
Cam_port_1 = 1 #Left Camera


Left_cam = "Left_View"
Right_cam = "Right_View"

monitor = screen.get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height


#Timer
b = 0

def delay(a):
    time.sleep(a)
    return a

def Counter():
    global b
    b += 1
    return b

def Steps():
    delay(1)
    result = Counter()
    print(result)


#Left_Camera_Screen_Position
Left_x_pos = 600
Left_y_pos = 200 

#Right_Camera_Scree_Position
Right_x_pos = 100
Right_y_pos = 200

#left_Filter_position:
L_top_pos = (0,0)
L_bottom_pos = (220,480)
box_color = (0,255,0)
box_thickness = 2

#right_Filter_position:
R_top_pos = (420,0)
R_bottom_pos = (640,480)


# #test_rectangle
# T_Top_pos= (220,0)
# T_Bottom_pos = (230,10)
# T_color = (150,0,150)
# T_thickness = -1


#ROI for Turning Right
L_ROI_Top_pos = (220,0) 
L_ROI_Bottom_pos = (420,480)
ROI_Box_color = (200,0,200)
ROI_thickness = 3


#ROI for Turning Left
R_ROI_Top_pos = (220,0) 
R_ROI_Bottom_pos = (420,480)
ROI_Box_color = (200,0,200)
ROI_thickness = 3


Cam1 = cv.VideoCapture(Cam_port_1)
Cam2 = cv.VideoCapture(Cam_port_0)

print("Scree Resolution: "+ str(screen_width) + " x " + str(screen_height))

while True:
    Steps()
    isture , V1 = Cam1.read()
    istrue , V2 = Cam2.read()

    L_height, L_width = V1.shape[:2]
    R_height, R_width = V2.shape[:2]


    L_img_array = np.frombuffer(V1, dtype=np.uint8).reshape((L_height, L_width, 3))
    R_img_array = np.frombuffer(V2, dtype=np.uint8).reshape((R_height, R_width, 3))  


    #cv.imshow(Left_cam, V1)
    Left_pos = cv.rectangle(L_img_array,L_top_pos,L_bottom_pos,box_color,box_thickness)
    #test_box = cv.rectangle(Left_pos,T_Top_pos,T_Bottom_pos,T_color,T_thickness)
    Left_ROI_box = cv.rectangle(Left_pos,L_ROI_Top_pos,L_ROI_Bottom_pos,ROI_Box_color,ROI_thickness)
    cv.imshow("Left Filter", Left_ROI_box)
    cv.moveWindow("Left Filter", 120,100)
    Left_ROI_Crop = L_img_array[0:480,220:420]
    Left_ROI_Grey = cv.cvtColor(Left_ROI_Crop, cv.COLOR_BGR2GRAY)
    cv.imshow("Left ROI", Left_ROI_Crop)
    cv.moveWindow("Left ROI", 1400, 100)


    #cv.imshow(Right_cam, V2)
    Right_pos = cv.rectangle(R_img_array,R_top_pos,R_bottom_pos,box_color,box_thickness)
    Right_ROI_box = cv.rectangle(Right_pos,R_ROI_Top_pos,R_ROI_Bottom_pos,ROI_Box_color,ROI_thickness)
    cv.imshow("Right Filter", Right_ROI_box)
    cv.moveWindow("Right Filter", 760, 100)
    Right_ROI_Crop = R_img_array[0:480,220:420]
    cv.imshow("Right ROI", Right_ROI_Crop)
    cv.moveWindow("Right ROI", 1600, 100)

    cv.imwrite("Left_reference.jpg", Left_ROI_Grey)
    cv.imwrite("Right_reference.jpg", Right_ROI_Crop)

    image1 = cv.imread('Left_reference.jpg', cv.IMREAD_GRAYSCALE)
    #image2 = cv.imread('captured_photo.jpg', cv.IMREAD_GRAYSCALE)

    # Detect feature points (using Shi-Tomasi corner detector)
    feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    p0 = cv.goodFeaturesToTrack(image1, mask=None, **feature_params)

    # Calculate optical flow (i.e., track feature points)
    p1, st, err = cv.calcOpticalFlowPyrLK(image1, Left_ROI_Grey, p0, None)

    # Get the movement of points
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # Calculate the mean shift (translation) of points
    shift_x = np.mean(good_new[:, 0] - good_old[:, 0])
    shift_y = np.mean(good_new[:, 1] - good_old[:, 1])

    print(f"Shift in x: {shift_x}, Shift in y: {shift_y}")


       
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

Cam1.release()
Cam2.release()
cv.destroyAllWindows()