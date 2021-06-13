
mem = dict({})
with open('mempool.csv') as f:
    for line in f.readlines()[1:]:
        id,f,w,p = line.strip().split(",")
        ps = [] if len(p) ==0 else p.split(";")
        mem[id]={"f":f,"w":w,"p":ps}


anc = dict({})

def get_anc(id):
    if id in anc.keys():
        return anc[id]
    ret =[]
    for p in mem[id]["p"]:
        ret.append(get_anc(p))
    return ret

for id in mem.keys():
    anc[id] = get_anc(id)


def topologicalSortUtil(v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in mem[v]["p"]:
            if visited[i] == False:
                topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
def topologicalSort():
    # Mark all the vertices as not visited

    visited = dict({k:False for k in mem.keys()})
    stack = []

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in mem.keys():
        if visited[i] == False:
            topologicalSortUtil(i, visited, stack)

    # Print contents of the stack
    return stack[::-1]  # return list in reverse order
#print([len(anc[id]) for id in anc.keys()])

order = topologicalSort()
print(order)

def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)] 
 
    for i in range(1, n+1):
        for w in range(W, 0, -1):  
            if wt[i-1] <= w:
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
 
    return dp[W] 

