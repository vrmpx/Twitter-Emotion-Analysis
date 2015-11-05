
# coding: utf-8

# In[ ]:

import re
import numpy as np
import pandas as pd

import numpy.linalg as LA 
from sklearn.cluster import DBSCAN


# In[ ]:
print "Reading data "
data = pd.read_csv('../data/users_location_time.tsv', sep='\t')
print "Done reading data"
#data.head()


# In[ ]:
print "Transforming coordinates"

lon_re = "{u'type': u'Point', u'coordinates': \[(.*),\s.*\]}"
data['longitude'] = data['coordinates'].str.extract(lon_re).apply(float)

lat_re = "{u'type': u'Point', u'coordinates': \[.*,\s(.*)\]}"
data['latitude'] = data['coordinates'].str.extract(lat_re).apply(float)
data = data.drop('coordinates', 1)

print "Done w/ coordinates"

#data.head()


# In[ ]:
print "filtering"
filtered = data[['from_user_id', 'longitude', 'latitude']].groupby('from_user_id').filter(lambda x: len(x) > 3).dropna()
#filtered.head()

print "Filtered"

# In[ ]:

def cluster(locations, xmin = 1, epsilon = 0.3, neigh_samples = 3, random_state = 42):
    """ Devuelve el cluster de los datos para un usuario
        INPT: 
        locations es una matriz de coordenadas
        epsilon, neigh_samples: datos para DBSCAN
        OUTPT:
            (cluster, labels) si el numero de filas en locations > xmin
                               cluster es una lista de n_clusters matrices de len(n_clusters) x 2
            (none, none) en otro caso
    """
    db = DBSCAN(eps = epsilon, min_samples = neigh_samples, random_state = random_state).fit(locations)
    labels = db.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

    clusters = [locations[labels == i] for i in xrange(n_clusters)]

    return clusters


# In[ ]:

def getCentroid(cluster):
    """
        Devuelve el centroide de las coordenadas del cluster
        INPT:
            cluster es el cluster obtenido para ese usuario
        OUTPT:
            centroid si cluster es distinto de None
            None en otro caso
    """
    try:
        return np.mean(cluster, axis = 0)
    except:
        return None

def maxCluster(clusters):
    """ Deuvelve el cluster mas grande para un usuario
        INPT:
            clusters: cluster obtenido para key
    """
    try:
        return clusters[np.argmax(map(len, clusters))]
    except:
        return None


# In[ ]:
print "Clustering..."

with open('../data/homeInferences_user.tsv', 'w') as outpt:
    for uid, val in filtered.groupby('from_user_id'):
        mtx = np.matrix(val[['longitude', 'latitude']].values)
        c = cluster(mtx)
        outpt.write("{}\t{}\n".format(uid, np.asarray(getCentroid(maxCluster(c))).reshape(-1)))
        # print "Done with ", uid

print "Done..."


# In[ ]:



