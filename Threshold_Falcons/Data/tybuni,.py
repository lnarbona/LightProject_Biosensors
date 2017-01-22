a = sustraction('data_debut.csv', 'data_fin.csv', "None")           #to plot sustraction
b = sustraction('data_debut.csv', 'data_fin.csv', "UV")
c = sustraction('data_debut.csv', 'data_fin.csv', "Blue")
d = sustraction('data_debut.csv', 'data_fin.csv', "Green")
e = sustraction('data_debut.csv', 'data_fin.csv', "Red")
f = sustraction('data_debut.csv', 'data_fin.csv', "IR")
g = sustraction('data_debut.csv', 'data_fin.csv', "Sunlight")
amoy = (sum(a) / len(a))                                           #average of list a
bmoy = (sum(b) / len(b))                                           #average of list b
cmoy = (sum(c) / len(c))
dmoy = (sum(d) / len(d))
emoy = (sum(e) / len(e))
fmoy = (sum(f) / len(f))
gmoy = (sum(g) / len(g))
totmoy = [amoy, bmoy, cmoy, dmoy, emoy, fmoy, gmoy]
h= list()
x= list()
w = list()
k = list()
l = list()
m = list()
n = list()
for j in a:
    h.append(1)
for j in b:
    x.append(2)
for i in c:
    w.append(3)
for i in d:
    k.append(4)
for i in e:
    l.append(5)
for i in f:
    m.append(6)
for i in g:
    n.append(7)

plt.scatter(h, a, alpha=0.75, facecolor='blue', marker='x')                      #scatter plots
plt.scatter(x, b, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(w, c, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(k, d, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(l, e, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(m, f, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(n, g, alpha=0.75, facecolor='blue', marker='x')


plt.scatter(listacaca, totmoy, alpha=0.75, facecolor='black', s=500, marker='_') #ploted averages














for i in range(len(conditions)):
#    a = comp('data_debut.csv', 'data_fin.csv', conditions[i])                 #to plot comparasion
    b = sustraction('data_debut.csv', 'data_fin.csv', conditions[i])
#    amoy = (sum(a) / len(a))
    bmoy = (sum(b) / len(b))
    c = list()
    for j in b:
        c.append(listacaca[i])
#    plt.scatter(c, a, alpha=0.75, facecolor='blue', marker='x')
#    plt.scatter(c, b, alpha=0.75, facecolor='red', marker='x')
#    plt.scatter(listacaca[i], bmoy, alpha=0.75, facecolor='black', s=500, marker='_')
