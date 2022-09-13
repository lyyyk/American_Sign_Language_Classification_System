#operating system
import os
#openCV(computer vision)
import cv2
import random
import string

convert_dict = {}

def asl_classifier(frame):
    # TO DO: implement
    result = random.randint(0,25)
    char = convert_dict[result]
    message = 'Result: {}'.format(char)
    #Insert result message on output window (controlling different features of text)
    frame = cv2.putText(frame, message, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
    return frame
def main():
    
    alphabets = list(string.ascii_uppercase)
    for i in range(len(alphabets)):
        convert_dict[i] = alphabets[i]
    
    #webcam object
    webcam = cv2.VideoCapture(0)
    
    #window size control
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while True:
        #read object to retrieve frame
        flag, frame = webcam.read()
        
        #infinite loop(identify letter in each frame being retrieved)
        frame = asl_classifier(frame)
        
        #show frame with identified letter in window
        cv2.imshow('window', frame)
        
        #wait 250ms until moving on to next frame
    
        key = cv2.waitKey(250)
        
        if key == ord('q'):
            print("Program exit")
            break
        elif key == ord('s'):
            file_path = 'test.png'
            cv2.imwrite(file_path, frame)
    

if __name__ == '__main__':
    
    
    
    
    
    main()