import numpy as np
import sys
import cv2


print( sys.argv[1]) # get value
sys.stdout.flush()
# print(dataToSendBack) send back to node
# sys.stdout.flush()
cap = cv2.VideoCapture(0)

    
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frameqq
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ('ok')
        sys.stdout.flush()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
