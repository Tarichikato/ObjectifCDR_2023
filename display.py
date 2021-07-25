from skimage.io import imread
from matplotlib import pyplot as plt
from matplotlib.patches import Circle,Rectangle
import get_config as config
import time
import cv2




def stream_table(table):
    while True:
        img = imread('data/fondTable21.jpg')


        e1 = table.scale(img.shape, table.bd['enemy_1'])
        e2 = table.scale(img.shape, table.bd['enemy_2'])
        #f1 =
        f1 = table.scale(img.shape, (table.codeuses[0],table.codeuses[1]))
        f2 = table.scale(img.shape, table.bd['friend_2'])


        cv2.circle(img, e1, 50, (255, 0, 0), -1)
        cv2.circle(img, e2, 50, (255, 0, 0), -1)
        cv2.circle(img, f1, 50, (0, 0, 255), -1)
        cv2.circle(img, f2, 50, (0, 0, 255), -1)

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



