from skimage.io import imread
from matplotlib import pyplot as plt
from matplotlib.patches import Circle,Rectangle
import get_config as config
import time
import cv2
import math




def stream_table(table):
    while True:


        img = imread('data/fondTable21.jpg')

        if(table.bd['enemy_1'] is not None):
            e1 = table.scale(img.shape, table.bd['enemy_1'])
            cv2.circle(img, e1, 50, (255, 0, 0), -1)
        if (table.bd['enemy_2'] is not None):
            e2 = table.scale(img.shape, table.bd['enemy_2'])
            cv2.circle(img, e2, 50, (255, 0, 0), -1)
        if (table.bd['friend_1'] is not None):
            f1 = table.scale(img.shape, (table.codeuses[0],table.codeuses[1]))
            cv2.circle(img, f1, 50, (0, 0, 255), -1)
        if (table.bd['friend_2'] is not None):
            f2 = table.scale(img.shape, table.bd['friend_2'])
            cv2.circle(img, f2, 50, (0, 0, 255), -1)







        #Trait pour orientation
        o = table.codeuses[2]
        pt2 = (int(f1[0] + math.cos(o) * 150), int(f1[1] + math.sin(o) * 150))
        lineThickness = 2
        cv2.line(img, f1,pt2, (0, 0, 0), lineThickness)

        if (table.cam['girouette'] is not None):
            team = config.get_couleur()
            x = 0
            if (team == 'yellow'):
                x = img.shape[1] - 100
            if (table.cam['girouette'] == 'N'):
                y = 0
            if (table.cam['girouette'] == 'S'):
                y = 280
            #Todo à revoir
            cv2.rectangle(img, (x,y), (x-100,y-125), 'g', 0.5)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Image",img)
        key = cv2.waitKey(1)



        # Press esc or 'q' to close the image window
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break



