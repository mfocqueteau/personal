""" Fórmulas relacionadas a la esfericidad de la Tierra """
from collections import namedtuple
from numpy import cos, pi, arccos


def angle(height, degrees=True):
    """ Retorna ángulo de caída del horizonte """
    theta = arccos(R / (R + height))
    if degrees:
        return theta * RADTODEG
    return theta


def horizon(height, miles=True):
    """ Retorna distancia hasta el horizonte del observador """
    if miles:
        return R * angle(height, False) / 5280
    return R * angle(height, False)


def visible(eye_height, object_height, distance):
    """ Qué porcentaje del objeto es visible """
    distance *= 5280
    dist_horizon = horizon(eye_height, False)
    hidden = R * (1 / cos((distance - dist_horizon) / R) - 1)
    obj_visible = object_height - hidden
    percentage = 1 if distance <= dist_horizon else 0
    if hidden < object_height:
        percentage = obj_visible / object_height
        # print(f"Target hidden height: {hidden} ft\n"
        #       f"Target visible height: {obj_visible} ft ({percentage} %)")
    return Visible(obj_visible, 100 * percentage, hidden)


def centrifugal(latitude):
    """ La fuerza centrífuga debido a la rotación de la Tierra a cierta latitud """
    latitude /= RADTODEG
    speed = 2 * pi * R * cos(latitude) / (24 * 3600)
    acceleration = speed**2 / (R * cos(latitude))
    return Motion(speed, acceleration)


def refraction(eye_height, object_height, distance, percentage=97):
    """ El ángulo (grados) de refracción necesario para ver X% de cierto objeto """
    distance *= 5280
    adjusted_height = object_height * (1 - percentage / 100)
    dist_horizon = horizon(eye_height, False)
    alpha = (distance - dist_horizon) / R - arccos(R / (R + adjusted_height))
    return alpha * RADTODEG


def gravitational_force(mass1, mass2, distance):
    """ 'Fuerza' gravitacional """
    return G * mass1 * mass2 / distance**2


Visible = namedtuple('Visible', 'visible percentage hidden')
Motion = namedtuple('Motion', 'speed acceleration')

RADTODEG = 180 / pi  # 1 radián en grados
R = 20902230.97  # Radio d la Tierra en [ft]
G = 6.67408 * 10**(-11)  # Constante gravitacional
