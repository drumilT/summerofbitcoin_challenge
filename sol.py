
mem = dict({})
with open('mempool.csv') as f:
    for line in f.readlines()[1:]:
        id,f,w,p = line.strip().split(",")
        ps = [] if len(p) ==0 else p.split(";")
        mem[id]={"f":int(f),"w":int(w),"p":ps}


anc = dict({})

def get_anc(id):
    if id in anc.keys():
        return anc[id]
    ret =[]
    for p in mem[id]["p"]:
        ret+=get_anc(p)
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
#print(order)
Wmax = 4000000


f = [ mem[i]['f']+sum([mem[j]['f'] for j in anc[i]]) for i in order]

w = [ mem[i]['w']+sum([mem[j]['w'] for j in anc[i]]) for i in order]
#chosen = dict({k:False for k in mem.keys()})
pos_map = {b:a for a,b in enumerate(order)}

print(len(f),len(order),len(w))
def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)] 
    chosen = [{} for _ in range(W+1)]
    for i in range(1, n+1):
        if i%100==0:
            print(i)
        for w in range(W, 0, -1):  
            if wt[i-1] <= w and (i-1) not in chosen[w-wt[i-1]]:
                val2 = max(dp[w], dp[w-wt[i-1]]+val[i-1])
                if dp[w] != val2:
                    dp[w] = val2
                    chosen[w] = chosen[w-wt[i-1]]
                    for j in anc[order[i-1]]:
                        chosen[w].add(pos_map[j])

    return dp[W],chosen[W]

best_val, chosen = knapSack(Wmax,w,f,len(f))
print(best_val)
print(sum([mem[order[i]]['f'] for i in chosen if i==1]))
print(sum([mem[order[i]]['w'] for i in chosen if i==1]))
#print([order[i] if i ])
with open("block.txt","w") as f:
    for i in chosen:
        if i == 1:
            f.write(order[i]+"\n")