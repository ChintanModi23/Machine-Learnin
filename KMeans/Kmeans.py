import sys

##################################
###Reading Data from file
##################################
datafile = sys.argv[1]
f = open(datafile)
data = []
line = f.readline()
while(line !=''):
	row = line.split( )
	rowf = []
	for i in range(0,len(row),1):
		rowf.append(float(row[i]))
	data.append(rowf)
	line = f.readline()
rows = len(data)
cols = len(data[0])
f.close()

m = []
distance = []
cluster = []
last = []
lust = 999999999999

##################################
###No of Clusters
##################################
no_clusters = int(sys.argv[2])
for i in range(0, no_clusters, 1):
	cluster.append([])
	last.append([])
	m.append([])
	distance.append(0)

##################################
###Initialize: assign xi to C1 or C2 with equal probability
##################################
for i in range(0,rows,1):
	cluster[i%no_clusters].append(data[i])
	last[i%no_clusters].append(data[i])
	
	
for i in range(0,no_clusters,1):
	for j in range(0,cols,1):
		m[i].append(0)
		
		
for i in range(0,no_clusters,1):
	for j in range(0,len(cluster[i]),1):
		for k in range(0,cols,1):
			m[i][k]=m[i][k] + cluster[i][j][k]
	for j in range(0,cols,1):
		if len(cluster[i])!=0:
			m[i][j]=m[i][j]/len(cluster[i])
		else:
			m[i][j]=0
cont=1
while(cont==1):
	
	obj=0
	clus_pop=[]
	clus_app=[]
	for i in range(0,no_clusters,1):
			last[i]=cluster[i][:]
			clus_pop.append([])
			clus_app.append([])
	
##################################
###Recompute no_clusters: assign xi to C1 if ||xi-m1||<||xi-m2||, otherwise assign to C2
##################################
	for i in range(0,no_clusters,1):
		for j in range(0,len(cluster[i]),1):
			min=999999999999
			for e in range(0,no_clusters,1):
				distance[e]=0
			for l in range(0,no_clusters,1):
				for k in range(0,cols,1):
					distance[l]=distance[l] + ((cluster[i][j][k]-m[l][k])**2)
			for e in range(0,no_clusters,1):
				if distance[e]<min:
					min=distance[e]
					rem=e
			if i!=rem:
				clus_pop[i].append(cluster[i][j])
				clus_app[rem].append(cluster[i][j])
	
	
	for j in range(0,no_clusters,1):
		for k in range(0,len(clus_pop[j]),1):
			cluster[j].remove(clus_pop[j][k])
	for j in range(0,no_clusters,1):
		for k in range(0,len(clus_app[j]),1):
			cluster[j].append(clus_app[j][k])
			
##################################
###Recompute means m1 and m2		
##################################			
	for j in range(0,no_clusters,1):
		for k in range(0,cols,1):
			m[j][k]=0
	for i in range(0,no_clusters,1):
		for j in range(0,len(cluster[i]),1):
			for k in range(0,cols,1):
				m[i][k]=m[i][k] + cluster[i][j][k]
		for j in range(0,cols,1):
			if len(cluster[i])!=0:
				m[i][j]=m[i][j]/len(cluster[i])
			else:
				m[i][j]=0

##################################				
###Compute objective
##################################

	for i in range(0,no_clusters,1):
		for j in range(0,len(cluster[i]),1):
			for k in range(0,cols,1):
				obj=obj + ((cluster[i][j][k]-m[i][k])**2)

##################################	
####Compute objective of new clustering. If difference is smaller than     then stop, otherwise go to step 2.
##################################
	if abs(obj-lust)==0:
		cont=0
	lust=obj



for i in range(0,rows,1):
	for j in range(0,no_clusters,1):
		for k in range(0,len(cluster[j]),1):
			if cluster[j][k]==data[i]:
				print(j,i)