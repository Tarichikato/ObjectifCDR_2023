from skimage.io import imread
from matplotlib import pyplot as plt
from matplotlib.patches import Circle,Rectangle
import get_config as config


def show(table):
    img = imread('data/fondTable21.jpg')
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Show the image
    ax.imshow(img)

    e1 = table.scale(img.shape, table.bd['enemy_1'])
    e2 = table.scale(img.shape, table.bd['enemy_2'])
    f1 = table.scale(img.shape, table.bd['friend_1'])
    f2 = table.scale(img.shape, table.bd['friend_2'])

    circ = Circle(e1, 50, color='r')
    ax.add_patch(circ)
    circ = Circle(e2, 50, color='r')
    ax.add_patch(circ)
    circ = Circle(f1, 50, color='g')
    ax.add_patch(circ)
    circ = Circle(f2, 50, color='g')
    ax.add_patch(circ)

    if (table.cam['girouette'] is not None):
        team = config.get_couleur()
        x = 0
        if (team == 'yellow'):
            x = img.shape[1] - 100
        if (table.cam['girouette'] == 'N'):
            y = 0
        if (table.cam['girouette'] == 'S'):
            y = 280

        rect = Rectangle((x, y), 100, 125, color='g', alpha=0.5)
        ax.add_patch(rect)

    plt.show()