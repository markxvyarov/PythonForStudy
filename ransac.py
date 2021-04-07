import random
import numpy as np

def ransac_py(Data, max_points, treshhold, max_iterations):
    iterations = 0
    data_length = len(Data)
    actual_model_size = 0
    model_size = 0
    best_eq = []
    while iterations < max_iterations and model_size < max_points:
        rnd_a = random.randint(0,data_length-1)
        rnd_b = random.randint(0, data_length - 1)
        while rnd_a == rnd_b:
            rnd_b = random.randint(0,data_length-1)
        rnd_c = random.randint(0,data_length-1)
        while rnd_c == rnd_a or rnd_c == rnd_b:
            rnd_c = random.randint(0, data_length - 1)
        vec_A = Data[rnd_a]
        vec_B = Data[rnd_b]
        vec_C = Data[rnd_c]

        vec_BA = vec_B - vec_A
        vec_CA = vec_C - vec_A

        w = np.cross(vec_BA, vec_CA)
        w = w/np.linalg.norm(w)

        D = -np.sum(np.multiply(w, vec_C))
        distances = (w[0]*Data[:, 0]+w[1]*Data[:, 1]+w[2]*Data[:, 2]+D)/np.linalg.norm(w)
        inliers = np.where(np.abs(distances) <= treshhold)[0]
        model_size = len(inliers)
        if model_size > actual_model_size:
            best_inliers = inliers
            actual_model_size = model_size
            best_eq = [w[0], w[1], w[2], D]
        iterations += 1

    return best_eq
