import cv2
import cv2.aruco as aruco
import time

#Renvoie le contre des robots des equipes bleues et jaunes dans un objet json

#Bon là c'est en dur
def get_robots_center():
    #TODO Appel à la camera de la balise

    robots_center = {'blue_1': (1600,1600), 'blue_2':None, 'yellow_1': (2500,400), 'yellow_2': None}
    return(robots_center)

def view():
    cap = cv2.VideoCapture(0)

    # Check whether user selected camera is opened successfully.

    if not (cap.isOpened()):

        print('Could not open video device')



    else:

        while True:

            ret, image = cap.read()
            loc_robots(image)
            time.sleep(2)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break

        cap.release()

        cv2.destroyAllWindows()



def detect_Aruco(img):  #returns the detected aruco list dictionary with id: corners
    aruco_list = {}
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)   #creating aruco_dict with 4x4 bits with max 250 ids..so ids ranges from 0-249
    parameters = aruco.DetectorParameters_create()  #refer opencv page for clarification
    #lists of ids and the corners beloning to each id
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters = parameters)

    if len(corners):    #returns no of arucos

        for k in range(len(corners)):
            temp_1 = corners[k]
            temp_1 = temp_1[0]
            temp_2 = ids[k]
            temp_2 = temp_2[0]
            aruco_list[temp_2] = temp_1
        return ids, aruco_list
    return None, None

def loc_robots(img):
    robots_center = {'blue_1': None, 'blue_2': None, 'yellow_1': None, 'yellow_2': None}
    ids, arucoDict = detect_Aruco(img)
    if(ids is not None):
        flag = 0 #Ce flag sert à savoir si on a déja détecté un robot bleu
        for k in range(1,6):
            if k in ids:
                if flag == 0:
                    robots_center['blue_1'] = recaller(arucoDict[k])
                else:
                    robots_center['blue_2'] = recaller(arucoDict[k])
                flag += 1
        flag = 0  # Ce flag sert à savoir si on a déja détecté un robot jaune
        for k in range(6,11):
            if k in ids:
                if flag == 0:
                    robots_center['yellow_1'] = recaller(arucoDict[str(k)])
                else:
                    robots_center['yellow_2'] = recaller(arucoDict[str(k)])
                flag += 1

    print(robots_center)

#passer de vue caméra à vue de dessus (tte la complexité de ce module)
#Bon ici on a juste fait comme si on avait déja la vue recalée
#TODO implementer
def recaller(corners):
    x = int((corners[0][0]+corners[1][0]+corners[2][0]+corners[3][0])/4)
    y = int((corners[0][1] + corners[1][1] + corners[2][1] + corners[3][1])/4)
    return((x,y))