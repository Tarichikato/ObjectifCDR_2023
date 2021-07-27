
import talkToLL as ll
import balise as b
import camera as c
import get_config as config
import lidar
import graph as g
import _thread
import time
from scipy.spatial import distance


class Table():
    def __init__(self):
        self.graph = self.build_graph()
        self.bd = self.get_balise_data()
        self.cam = self.get_camera_data()
        self.codeuses = (0, 0, 0)
        self.codeuses = self.get_codeuses_data()

        _thread.start_new_thread(self.keep_table_updated, (0.01,))

    def keep_table_updated(self,delay):
        while True:
            self.update_table()
            time.sleep(delay)

    def update_table(self):
        self.bd = self.get_balise_data()
        self.lidar = lidar.get_map()
        self.cam = self.get_camera_data()
        self.graph = self.update_graph()
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

    def build_graph(self):
        graph = g.init_graph()
        return (graph)

    def get_elements(self):
        #Todo lister les élémnts présents et leur position

        return None

    def get_config(self):
        #Todo récuperer un dictionaire avec la config des éléménts (ex: girouette ou eceuil en 2020
        # on peut meme imaginer mache à air relevèes ou phare déployé ou non)
        return None

    def update_graph(self):
        graph = self.build_graph()
        to_pop = []
        for _edge in graph:
            edge = _edge.split(',')
            p = (int(edge[0]), int(edge[1]))
            if(distance.euclidean(p, self.bd['enemy_1']) < 150*2):
                to_pop.append(_edge)
        for e in to_pop:
            graph.pop(e)
        for _edge in graph:
            tp= []
            for k in range (len(graph[_edge])):
                if(graph[_edge][k] in to_pop):
                    tp+=[graph[_edge][k]]
            for k in tp:
                graph[_edge].remove(k)
        return (graph)

