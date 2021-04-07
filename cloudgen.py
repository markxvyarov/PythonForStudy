from scipy.stats import norm
import random
import math


def generate_cylinder(num_points, r, h, x_offset, y_offset, z_offset):
    xx = []
    yy = []
    zz = []
    for n in range(0, num_points):
        x = random.uniform(-r, r)
        temp = math.sqrt(r * r - x * x)
        y = random.uniform(-temp, temp)
        z = random.uniform(-1/2*h, 1/2*h)
        xx.append(x+x_offset)
        yy.append(y+y_offset)
        zz.append(z+z_offset)

    points = zip(xx, yy, zz)
    return points


def generate_plane(num_points, x_loc, x_scale, y_loc, y_scale, z_loc, z_scale):
    distribution_x = norm(loc=x_loc, scale=x_scale)
    distribution_y = norm(loc=y_loc, scale=y_scale)
    distribution_z = norm(loc=z_loc, scale=z_scale)
    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points
