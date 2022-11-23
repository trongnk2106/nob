import cv2
import numpy as np


def laser(frame,sec):
    global zeros
    if sec == 1:
        zeros[s:s+1,:] = frame[s:s+1,:]
        zeros[s+1:,:] = frame[s+1:,:]
        cv2.line(zeros,(0,s+2),(640,s+2),(255,255,0),(2))

        return zeros
    elif sec == 2:
        zeros[:,s:s+1] = frame[:,s:s+1]
        zeros[:,s+1:] = frame[:,s+1:]
        cv2.line(zeros,(s+2,0),(s+2,640+2),(100,255,50),(2))

        return zeros


if __name__ =="__main__":
    red =cv2.VideoCapture(0)
    s = 1
    array = np.array([])
    zeros = np.zeros([480,640,3],dtype=np.uint8)
    zeros.fill(255)
    try:
        sec = int(input('1: duong lazer nam ngang \n2: duong lazer thang dung\n=> '))
    except Exception as e:
        pass
    if sec == 1:
        d = True
        pass
    elif sec == 2:
        d = True
        pass
    else:
        print('end')
        d = False

    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)

    while d:
        _,frame = red.read()

        frame=cv2.flip(frame, 1)

        if sec ==1 :
            img = laser(frame,sec)
        elif sec ==2:
            img = laser(frame,sec)

        if s <= 640:
            cv2.imshow('frame',img)
        s +=1
        if s>=640:
            cv2.destroyWindow('frame')
            cv2.namedWindow('copy', cv2.WINDOW_NORMAL)
            cv2.imshow('copy',img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite('laser_images.png',img)
            break

    cam.release()
    cv2.destroyAllWindows()