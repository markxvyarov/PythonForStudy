import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


if __name__ == '__main__':
    features = pd.read_csv('textures_data.csv', sep=',')
    a = 3

    data = np.array(features)
    X = (data[:, :-1]).astype('float64')
    Y = data[:, -1]

    x_transform = PCA(n_components=3)

    Xt = x_transform.fit_transform(X)

    red = Y == 'linoleum'
    green = Y == 'plaster'
    blue = Y == 'table'
    yellow = Y == 'wood'

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(Xt[red, 0], Xt[red, 1], Xt[red, 2], c="r")
    ax.scatter(Xt[green, 0], Xt[green, 1], Xt[green, 2], c="g")
    ax.scatter(Xt[blue, 0], Xt[blue, 1], Xt[blue, 2], c="b")
    ax.scatter(Xt[yellow, 0], Xt[yellow, 1], Xt[yellow, 2], c="y")

    classifier = svm.SVC(gamma='auto')

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33)

    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    print(acc)
    cm = confusion_matrix(y_test, y_pred, normalize='true')
    print(cm)
    disp = plot_confusion_matrix(classifier, x_test, y_test, display_labels=['Linoleum','Plaster','Table','Wood'], cmap=plt.cm.Blues)

    a = 0
