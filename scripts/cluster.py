###################################
#
#
###################################


import numpy as np
import numpy.linalg as LA 
from sklearn.cluster import DBSCAN


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
	if(len(locations) > xmin): #len(locations) = numero de filas en locations
		db = DBSCAN(eps = epsilon, min_samples = neigh_samples, random_state = random_state).fit(locations)
		labels = db.labels_
		n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

		clusters = [locations[labels == i] for i in xrange(n_clusters)]

		return clusters
	else:
		return None 

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

def minCluster(clusters):
	""" Deuvelve el cluster mas chico para un usuario
		INPT:
			clusters: cluster obtenido para key
	"""
	try:
		return clusters[np.argmin(map(len, clusters))]
	except:
		raise None

def distance(x, y):
	p1 = np.array(x)
	p2 = np.array(y)
	return LA.norm(p1 - p2)