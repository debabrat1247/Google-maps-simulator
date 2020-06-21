import collections
import heapq
q=collections.deque()
def shortpath(G,s,sink,speed):
	dist=[999 for i in range(len(G))]
	prev=[-1 for i in range(len(G))]
	path=["" for i in range(len(G))]
	noofpath=[0 for i in range(len(G))]

	dist[s]=0
	V=[[999,i] for i in range(len(G))]
	V[s][0]=0

	heapq.heapify(V)

	while(V):
		u=heapq.heappop(V)
		for x in G[u[1]]:
			v=x[0]
			duv=x[1]

			if(dist[v]>dist[u[1]]+duv):
				dist[v]=dist[u[1]]+duv
				path[v]=path[u[1]]+str(" ")+str(u[1])
				noofpath[v]=noofpath[u[1]]

				for i in V:
					if(i[1]==v):
						i[0]=dist[v]
				heapq.heapify(V)

			elif(dist[v]==dist[u[1]]+duv):
				print("node",u[1],v)
				noofpath[v]+=1

	
	print("Shortest path between source and sink is",path[sink],sink,"with distance",dist[sink],"km")
	print("You may take",dist[sink]/speed,"hour")

	



def bfs(G,source,sink,prev):
	n=len(G)
	color=[0 for i in range(n)]
	color[source]=1
	prev[source]=-1
	q.append(source)

	while(q):
		u=q.popleft()
		for v in G[u]:
			if color[v[0]]==0 and v[1]>0:
				q.append(v[0])
				color[v[0]]=1
				prev[v[0]]=u


	return True if color[sink]==1 else False

def max_flow(source,sink,G):

	n=len(G)
	maxflow=0
	prev=[-1 for i in range(n)]

	while(bfs(G,source,sink,prev)):
		pathflow=float("Inf")
		s=sink
		while(s!=source):
			weigth=0
			for v in G[prev[s]]:
				if v[0]==s:
					weigth=v[1]
					break

			pathflow=min(pathflow,weigth)
			s=prev[s]

		maxflow+=pathflow

		s=sink
		while(s!=source):
			x=dict(G[prev[s]])
			for v in G[prev[s]]:
				if v[0]==s:
					p=v[1]-pathflow	
					x[v[0]]=p
					break

			G[prev[s]]=x.items()
			s=prev[s]

	print("Maximum flow in the road map(graph) is ",maxflow)
	
def min_cut(source,sink,G):
	n=len(G)
	visited=[0 for i in range(n)]
	visited[source]=1
	q.append(source)

	while(q):
		u=q.popleft()
		for v in G[u]:
			if visited[v[0]]==0 and v[1]>0:
				q.append(v[0])
				visited[v[0]]=1
	print("Minimum cut on the graph:")
	for i in range(n):
		for v in G[i]:
			if visited[i]==1 and visited[v[0]]==0:
				print(i,v[0])


def main():

	file=open("input1.txt","r")
	G=[]
	G1=[]
	for line in file:
		first=True
		adj=[]
		adj1=[]
		for edge in line.split(" "):
			if(first==True):
				first=False

			else:
				v,weigth,dist=edge.split(",")
				adj.append((int(v),int(weigth)))
				adj1.append((int(v),int(dist)))

		G.append(adj)
		G1.append(adj1)

	file.close()
	source=int(input("Enter starting point(source vertex):"))
	sink=int(input("Enter Destination point(sink vertex):"))
	speed=int(input("Enter the speed(km/hr) of your vehicle:"))
	shortpath(G1,source,sink,speed)
	max_flow(source,sink,G)
	min_cut(source,sink,G)


main()
