import cv2
import argparse
from time import sleep

ap = argparse.ArgumentParser()

ap.add_argument('-v', '--video', required=True, help='path to the input video')
args = vars(ap.parse_args())

print(args)

cap = cv2.VideoCapture(args['video'])

fno = 0
while(cap.isOpened()):
    ret, frame = cap.read()

# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.putText(frame, f'{fno}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2, cv2.LINE_AA)

    sleep(0.1)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord(' '):
        while True:
            key2 = cv2.waitKey(1) & 0xFF
            cv2.imshow('frame', frame)

            if key2 == ord(' '):
                break
        
    fno += 1


cap.release()
cv2.destroyAllWindows()