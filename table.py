
import talkToLL as ll
import balise as b
import camera as c
import get_config as config
import lidar
import graph as g
import _thread
import time
import math
from scipy.spatial import distance
import graph2 as g2


class Table():
    def __init__(self):
        self.fixed_obstacles = self.init_fixed_obstacles()
        self.graph, self.nodes = self.build_graph()
        print("Graph créé")
        self.bd = self.get_balise_data()
        self.cam = self.get_camera_data()
        self.codeuses = (0, 0, 0)
        self.codeuses = self.get_codeuses_data()

        _thread.start_new_thread(self.keep_table_updated, (0.01,))
        _thread.start_new_thread(self.simulate_mouv, (0.5,))

    def simulate_mouv(self,delay):
        while True:
            #self.bd = self.get_balise_data()
            e = (self.bd['enemy_1'][0],(self.bd['enemy_1'][1]-100)%2000)
            self.bd['enemy_1'] = e
            time.sleep(delay)

    def keep_table_updated(self,delay):
        while True:
            self.update_table()
            time.sleep(delay)

    def update_table(self):
        #self.bd = self.get_balise_data()
        self.lidar = lidar.get_map()
        self.cam = self.get_camera_data()
        self.graph,self.nodes = self.update_graph()
        self.codeuses = self.get_codeuses_data()


    def get_balise_data(self):
        rc = b.get_robots_center()
        team = config.get_couleur()
        if (team == 'yellow'):
            return (
                {'enemy_1': rc['blue_1'], 'enemy_2': rc['blue_2'], 'friend_1': rc['yellow_1'],'friend_2': rc['yellow_2']})
        if (team == 'blue'):
            return (
                {'enemy_1': rc['yellow_1'], 'enemy_2': rc['yellow_2'], 'friend_1': rc['blue_1'],'friend_2': rc['blue_2']})
        else:
            # TODO Error
            print("couleur ni bleu ni jaune (cause la plus probable : Faute d'orthographe sale dislexique)")

    def get_camera_data(self):
        cam = c.get_data()
        return(cam)

    def get_codeuses_data(self):
        data = ll.get_position_odometrie()
        if(len(data)!=6):
            return(self.codeuses)
        return(int(data[1]),int(data[3]),float(data[5]))

    def scale(self,shape, position):
        return (int(position[0] / 3000 * shape[1]), int(position[1] / 2000 * shape[0]))

    def create_map(self):
        map = self.build_map(self)
        return map

    def build_map(self):
        graph = self.build_graph(self)
        elements = self.get_elements(self)
        config = self.get_config(self)
        map = {'graph': graph,'elements':elements,'config':config}
        return (map)

    def init_fixed_obstacles(self):
        robot_ray = 150
        fixed_obstacles = []
        fixed_obstacles.append({'type': 'rectangle','info':[(0,0),(3000,robot_ray)]})
        fixed_obstacles.append({'type': 'rectangle','info':[(0,0),(robot_ray,2000)]})
        fixed_obstacles.append({'type': 'rectangle','info':[(0,2000),(3000,2000-robot_ray)]})
        fixed_obstacles.append({'type': 'rectangle','info':[(3000,2000),(3000-robot_ray,0)]})
        return(fixed_obstacles)

    def build_graph(self):
        adj,nodes = g2.init_graph()
        for k in range(len(nodes)) :
            #TODO gerer le problème où c'est juste une arrète qui traverse
            if(self.is_in(nodes[k],self.fixed_obstacles)):
                for j in range (len(adj[k])):
                    if(adj[k][j] != 0):
                        adj[k][j] = 0
                        adj[j][k] = 0


        return (adj,nodes)

    def is_in(self,pt,obstacles):
        for obstacle in obstacles:
            if (obstacle['type'] == 'rectangle'):
                a = obstacle['info'][0]
                b = obstacle['info'][1]
                if(pt[0]>= a[0] and pt[0]<= b[0] or pt[0] <= a[0] and pt[0] >= b[0]):
                    if(pt[1]>= a[1] and pt[1]<= b[1] or pt[1] <= a[1] and pt[1] >= b[1]):
                        return (True)
        return(False)


    def get_elements(self):
        #Todo lister les élémnts présents et leur position

        return None

    def get_config(self):
        #Todo récuperer un dictionaire avec la config des éléménts (ex: girouette ou eceuil en 2020
        # on peut meme imaginer mache à air relevèes ou phare déployé ou non)
        return None

    def update_graph(self):
        adj,nodes = self.build_graph()
        p = self.bd['enemy_1']
        #print(p)
        for k in range (len(adj)):
            for i in range (len(adj[k])):
                if(adj[k][i]!= 0):
                    if(self.intercect(p,nodes[k],nodes[i],2*150)):
                        adj[k][i] = 0
        return (adj,nodes)

    def intercect(self,p,d1,d2,l):
        '''if(int((d1[0]-d2[0])) != 0):
            if (int((d1[1] - d2[1])) != 0):
                a = (d1[1]-d2[1])/(d1[0]-d2[0])
                b = d1[1] - a*d1[0]
                d = abs(a*p[0]+b-p[1])/math.sqrt(a*a+1)
            else: d = abs(d1[1]-p[1])
        else:
            d = abs(d1[0]-p[0])'''

        d = self.minDistance(d1, d2, p)

        if(d<= l):
            #print(d,d1,d2,p)
            return(True)
        else:
            return(False)

    def minDistance(self,A, B, E):

        # vector AB
        AB = [None, None];
        AB[0] = B[0] - A[0];
        AB[1] = B[1] - A[1];

        # vector BP
        BE = [None, None];
        BE[0] = E[0] - B[0];
        BE[1] = E[1] - B[1];

        # vector AP
        AE = [None, None];
        AE[0] = E[0] - A[0];
        AE[1] = E[1] - A[1];

        # Variables to store dot product

        # Calculating the dot product
        AB_BE = AB[0] * BE[0] + AB[1] * BE[1];
        AB_AE = AB[0] * AE[0] + AB[1] * AE[1];

        # Minimum distance from
        # point E to the line segment
        reqAns = 0;

        # Case 1
        if (AB_BE > 0):

            # Finding the magnitude
            y = E[1] - B[1];
            x = E[0] - B[0];
            reqAns = math.sqrt(x * x + y * y);

        # Case 2
        elif (AB_AE < 0):
            y = E[1] - A[1];
            x = E[0] - A[0];
            reqAns = math.sqrt(x * x + y * y);

        # Case 3
        else:

            # Finding the perpendicular distance
            x1 = AB[0];
            y1 = AB[1];
            x2 = AE[0];
            y2 = AE[1];
            mod = math.sqrt(x1 * x1 + y1 * y1);
            reqAns = abs(x1 * y2 - y1 * x2) / mod;

        return reqAns;


