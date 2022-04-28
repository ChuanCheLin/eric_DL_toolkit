from sklearn import manifold
import matplotlib.pyplot as plt
import numpy as np
import joblib

path = "/home/eric/few-shot-object-detection/features.npy"
label_path = "/home/eric/few-shot-object-detection/labels.npy"
features = np.load(path)
labels = np.load(label_path)

table = ['brownblight', 'algal', 'blister', 'sunburn', 'fungi_early', 'roller', 'moth', 
'tortrix', 'flushworm', 'caloptilia', 'mosquito_early', 'mosquito_late', 
'miner', 'thrips', 'tetrany', 'formosa', 'other']

# list for selection
chosen = [5, 6, 7, 8, 9] # roller to caloptilia

# tsne
X_tsne = manifold.TSNE(n_components=2, init='random', random_state=5, verbose=1).fit_transform(features)

joblib.dump(X_tsne, 'tsne.pkl')

x_min, x_max = X_tsne.min(0), X_tsne.max(0)
X_norm = (X_tsne - x_min) / (x_max - x_min)  #Normalize
plt.figure(figsize=(10, 10))

#for i in range(len(table)):
for i in chosen:
    x = []
    y = []
    # set color
    if i in range(0, 11):
            color = plt.cm.Set3(i)
    elif i in range(11, 17):
            color = plt.cm.Set1(i-10)

    for j in range(X_norm.shape[0]):
        if labels[j] == i:
            x.append(X_norm[j, 0])
            y.append(X_norm[j, 1])

    plt.scatter(x, y, color = color, label = table[i])

'''
for i in range(X_norm.shape[0]):
    #set color
    if labels[i] in range(0, 11):
        color = plt.cm.Set3(labels[i])
    elif labels[i] in range(11, 17):
        color = plt.cm.Set1(labels[i]-10)
    plt.scatter(X_norm[i, 0], X_norm[i, 1], color = color, label = table[labels[i]])
'''

plt.xticks([])
plt.yticks([])
plt.legend()
plt.savefig('t_sne.png')
plt.show()


    # plt.text(X_norm[i, 0], X_norm[i, 1], '.', color = color, #str(labels[i])
    #         fontdict={'weight': 'bold', 'size': 9})