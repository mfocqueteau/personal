from numpy import cos, pi, arccos


def angle(height, degrees=True):
    theta = arccos(R / (R + height))
    if degrees:
        return theta * radtodeg
    return theta


def horizon(height, miles=True):
    if miles:
        return R * angle(height, False) / 5280
    return R * angle(height, False)


def visible(eye_height, object_height, distance):
    distance *= 5280
    D1 = horizon(eye_height, False)
    hidden = round(R * (1 / cos((distance - D1) / R) - 1), 2)
    visible = round(object_height - hidden, 2)
    if distance <= D1:
        return 'Completely visible'
    elif hidden > object_height:
        print('Completely obscured,', abs(visible), 'ft under the horizon.')
    else:
        percentage = round(100 * visible / object_height)
        print(f"Target hidden height: {hidden} ft\n"
              f"Target visible height: {visible} ft ({percentage} %)")


def centrifugal(latitude):
    latitude /= radtodeg
    speed = 2 * pi * R * cos(latitude) / (24 * 3600)
    acceleration = speed**2 / (R * cos(latitude))
    print('Speed: {} ft/s'.format(round(speed)))
    print('Acceleration: {} ft/s^2'.format(round(acceleration, 3)))


def refraction(eye_height, object_height, distance, percentage=97):
    distance *= 5280
    hp = object_height * (1 - percentage / 100)
    D1 = horizon(eye_height, False)
    alpha = (distance - D1) / R - arccos(R / (R + hp))
    return print('{}°'.format(round(alpha * radtodeg, 4)))


def gravitational_force(m1, m2, distance):
    return G * m1 * m2 / distance**2


radtodeg = 180 / pi
R = 20902230.97
G = 6.67408 * 10**(-11)
