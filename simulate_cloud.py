from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from pyransac3d import Plane
import numpy as np
from cloudgen import *
from readwritecsv import *
import random
from ransac import*



if __name__ == '__main__':
    clusters = []
    cloud_points = generate_cylinder(2000, 20, 40, 500, 500, 500)
    clusters.extend(cloud_points)
    cloud_points = generate_plane(2000, -100, 20, -100, 200, -100, 0)
    clusters.extend(cloud_points)
    cloud_points = generate_plane(2000, 100, 0, 100, 20, 100, 200)
    clusters.extend(cloud_points)

    write_to_csv(clusters,'LidarData.xyz')
    read_gen = read_xyz_from_csv('LidarData.xyz')
    clusters = list(read_gen)
    x = np.array(clusters)

#    clusterer = KMeans(n_clusters=3)
#    y_pred = clusterer.fit_predict(x)

    clusterer = DBSCAN(eps=100, min_samples=500).fit(x)
    y_pred = clusterer.labels_

    first_cluster = y_pred == 0
    second_cluster = y_pred == 1
    third_cluster = y_pred == 2

    first_cloud = x[first_cluster,:]
    second_cloud = x[second_cluster,:]
    third_cloud = x[third_cluster,:]

    write_to_csv(first_cloud,'first_cloud.xyz')
    write_to_csv(second_cloud, 'second_cloud.xyz')
    write_to_csv(third_cloud, 'third_cloud.xyz')

    best_eq = ransac_py(third_cloud,1000,0.1,10000)
    print(best_eq)

    rans_plane = Plane()
    best_eq, best_inliers = rans_plane.fit(third_cloud,0.1,1000,10000)
    print(best_eq)

