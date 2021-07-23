import json

dir = ""

def get_couleur():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
        couleur = data['Common']['color']
    return(couleur)

def get_num_robots():
    with open(dir+"config.json") as json_data_file:
        data = json.load(json_data_file)
        num = data['Common']['num_robots']
    return (num)

def get_name():
    if(get_num_robots() == 2):
        with open(dir+"config.json") as json_data_file:
            data = json.load(json_data_file)
            name = data['Myself']['name']
    else:
        name = 'robot_1'
    return (name)


def is_homologation():
    with open(dir+"config.json") as json_data_file:
        data = json.load(json_data_file)
        homologation = data['Match']['homologation']
    if (homologation == 'True'):
        return True
    return False

def is_ll_simulated():
    with open(dir+"config.json") as json_data_file:
        data = json.load(json_data_file)
        simulation = data['Common']['simulate_LL']
    if (simulation == 'True'):
        return True
    return(False)


