import cv2
import pygame
#from gtts import gTTS
import pyttsx3
import os
def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 4096  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
thres=0.5 #threshold to detect object



#importing names of the ojects
classNames=[]
#importing the files
classFile='coco.names'
with open(classFile,'rt') as f: #read file classFile as f
    classNames =f.read().rstrip('\n').split('\n') #striping the images in the new line and stores inthe classNames

#importing the path of the configuration and weight
configPath='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath='frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img,draw=True,objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=0.2)
    print(classIds,bbox)
    if len(objects)==0: objects=classNames
    objectInfo = []
    if len(classIds) !=0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,className.upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)), (box[0] + 300, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 2)
                    pyttsx3.speak(str(className))
                   #myobj = gTTS(text=className, lang='en', slow=False)
                    #myobj.save("1.mp3")
                    #initMixer()
                    #file = '/home/ip/Desktop/blind_Asst/1.mp3'
                    #pmusic(file)
    return img,objectInfo



if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 488)

    while True:
        success, img = cap.read()
        if img is None :
            break
        result,objectInfo = getObjects(img)
        #print(objectInfo)
        cv2.imshow("output", img)
        cv2.waitKey(27)


