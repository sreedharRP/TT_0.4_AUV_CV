import cv2 as cv
import screeninfo as screen
import numpy as np
import time


start = time.time()
t_Bool = False

def timer():
    end_time = time.time()
    difference = end_time - start
    apppox_value = round(difference, 3)
    return apppox_value


#time position
Time_position = (480, 50)
Time_font = cv.FONT_HERSHEY_SIMPLEX
Time_font_scale = 1
Time_color = (0, 150, 150)
Time_thickness = 2



#port
Cam_port_0 = 0 #Right Camera
Cam_port_1 = 1 #Left Camera

Cam_0 = cv.VideoCapture(Cam_port_0)
Cam_1 = cv.VideoCapture(Cam_port_1)

Left_cam = "Left_View"
Right_cam = "Right_View"


#ROI Regions
L_T_NROI_pos = (0,0)
L_B_NROI_pos = (180, 480)
R_T_NROI_pos = (460,0)
R_B_NROI_pos = (640, 480)   
NROI_color = (0, 255, 0)
NROI_thickness = 2

while True:
    rec_time = timer()
    value , frame1 = Cam_0.read() #Left Camera
    value , frame2 = Cam_1.read()  #Right Camera

    L_gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    R_gray = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

    Left_N_ROI=cv.rectangle(frame1, L_T_NROI_pos, L_B_NROI_pos, NROI_color, NROI_thickness)
    Right_N_ROI=cv.rectangle(frame2, R_T_NROI_pos, R_B_NROI_pos, NROI_color, NROI_thickness)

    #cv.putText(L_gray, str(rec_time), Time_position, Time_font, Time_font_scale, Time_color, Time_thickness)

    stero = cv.StereoBM_create(numDisparities=176, blockSize=5)
    disparity = stero.compute(L_gray, R_gray)


    cv.imshow(Left_cam, Left_N_ROI)
    cv.moveWindow(Left_cam, 10, 10)
    
    cv.imshow(Right_cam, Right_N_ROI)
    cv.moveWindow(Right_cam, 645, 10)

    Required_disparity = disparity[0:640, 180:640]
    cv.imshow("Disparity", Required_disparity)
    #cv.moveWindow("Disparity", 10, 400)



    if cv.waitKey(1) & 0xFF == ord('x'):
        break
    
Cam_0.release()
Cam_1.release()
cv.destroyAllWindows()


