import time
import random

# functia de testat validitatea sortarii


def sortedtest(nume_sortare):

    global vaux

    daux = {}  # dictionar pentru retinerea frecventelor in vectorul sortat de nume_sortare

    if len(vaux) != n:
        print(nume_sortare + " nu a reusit sa sorteze; lungimea vectorului sortat difera de lungimea initiala")
        return False

    for k in range(n - 1):

        if vaux[k] > vaux[k + 1]:
            print(nume_sortare + " nu a reusit sa sorteze; elementele nu sunt in ordine crescatoare")
            return False

        if vaux[k] in daux.keys():
            daux[vaux[k]] += 1
        else:
            daux.update({vaux[k]: 1})

    if vaux[n - 1] in daux.keys():
        daux[vaux[n - 1]] += 1
    else:
        daux.update({vaux[n - 1]: 1})

    for elem in daux.keys():
        if (elem not in dver.keys()) or (elem in dver.keys() and dver[elem] != daux[elem]):
            print(nume_sortare + " nu a reusit sa sorteze; frecventa elementelor din vectorul sortat difera de cea din vectorul initial")
            return False

    return True
    '''vaux2 = [vaux[i] for i in range(n)] 
    vaux2.sort()
    for i in range(n):
        if vaux[i] == vaux2[i]:
            return True
    return False'''

# quicksort si functiile aferente


def pchoice(a, b, c):

    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (a <= c <= b) or (b <= c <= a):
        return c
    elif (b <= a <= c) or (c <= a <= b):
        return a


def partition(st, dr):

    p = pchoice(random.choice(vaux[st:dr + 1]), random.choice(vaux[st:dr + 1]), random.choice(vaux[st:dr + 1]))

    i = st - 1
    j = dr + 1

    while 1:
        i += 1
        while vaux[i] < p:
            i += 1

        j -= 1
        while vaux[j] > p:
            j -= 1

        if i < j:
            vaux[i], vaux[j] = vaux[j], vaux[i]
        else:
            return j


def quicksort(st, dr):

    if st < dr:
        ip = partition(st, dr)
        quicksort(st, ip)
        quicksort(ip + 1, dr)


# radixsort (in baza b) si functiile aferente

def dim(x):

    global b

    if x == 0:
        return 0

    count = 0
    while x > 0:
        x //= b
        count += 1

    return count


def radixsort():

    global vaux
    global n
    global b

    u = 0
    l = [[[] for i in range(b)] for k in range(2)]

    for i in range(n):
        l[u][vaux[i] % b].append(vaux[i])

    for c in range(2, ncmax + 1):

        for z in range(b):
            for t in range(len(l[u][z])):

                if l[u][z][t] >= b**(c - 1):
                    l[1 - u][(l[u][z][t] // b**(c - 1)) % b].append(l[u][z][t])
                else:
                    l[1 - u][0].append(l[u][z][t])

        l[u] = [[] for k in range(b)]
        u = 1 - u

    vaux = []  # reintializez vectorul initial (al sortarii), pentru a fi mai usor de completat cu elementele sortate din lista

    for z in range(b):
        for t in range(len(l[u][z])):
            vaux.append(l[u][z][t])

# heapsort si functiile aferente


def buildheap(h, k):

    ok = False
    while not ok:

        if k == 1 or h[k // 2] >= h[k]:
            ok = True
        else:
            h[k // 2], h[k] = h[k], h[k // 2]
            k //= 2


def morph(h):

    global naux

    h[1], h[naux] = h[naux], h[1]
    naux -= 1

    i = 1
    ok = False

    while not ok:

        if (i * 2 > naux and i * 2 + 1 > naux) or (h[i * 2] <= h[i] and h[i * 2 + 1] <= h[i]):

            ok = True

        elif i * 2 <= naux and i * 2 + 1 <= naux:

            if h[i * 2] < h[i * 2 + 1]:
                new = i * 2 + 1
            else:
                new = i * 2

            h[new], h[i] = h[i], h[new]
            i = new

        elif i * 2 <= naux and h[i * 2] > h[i]:

            h[i * 2], h[i] = h[i], h[i * 2]
            i *= 2

        elif i * 2 + 1 <= naux and h[i * 2 + 1] > h[i]:

            h[i * 2 + 1], h[i] = h[i], h[i * 2 + 1]
            i *= 2
            i += 1

        else:
            ok = True


def heapsort():

    global naux
    global vaux

    h = ['NULL']
    for i in range(naux):
        h.append(int(l[i]))
        buildheap(h, i + 1)

    while naux > 0:
        morph(h)

    vaux = [h[i + 1] for i in range(n)]

# heapsort luat de pe net


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapsort2(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def selectionsort():

    global vaux

    for i in range(n - 1):
        for j in range(i + 1, n):
            if vaux[i] > vaux[j]:
                vaux[i], vaux[j] = vaux[j], vaux[i]


# global

selectionsortok = int(input('\033[93m' + "Introduceti cifra 1 daca doriti rularea selection sort-ului (inclusiv pe teste mari) - 0 pentru a nu rula selection sort" + '\033[0m'))
inputfile = open("input.txt")

nteste = int(inputfile.readline())

for itest in range(nteste):

    n = int(inputfile.readline())  # dimensiune sir
    b = int(inputfile.readline())  # baza la alegere pentru radixsort

    s = inputfile.readline()  # sir de elemente
    l = s.split()

    ncmax = 0  # numar maxim de cifre pentru radixsort

    dver = {}  # dictionar pentru verificarea elementelor si a frecventelor lor din vector la finalul sortarii

    v = []
    for i in range(n):
        v.append(int(l[i]))  # sir introdus in lista

        nc = dim(v[i])

        if nc > ncmax:
            ncmax = nc

        if v[i] in dver.keys():
            dver[v[i]] += 1
        else:
            dver.update({v[i]: 1})
    if n < 10:
        print("test ", itest + 1, ", input : ", *v)
    else:
        print("test ", itest + 1, " :")

    vaux = [v[i] for i in range(n)]  # copie a vectorului cu elementele in ordinea initiala
    tinit = time.time()
    quicksort(0, n - 1)
    tfin = time.time()
    if sortedtest("quicksort"):
        print("quicksort a sortat cu succes; timp de executie: ", tfin - tinit)

    vaux = [v[i] for i in range(n)] # copie a vectorului cu elementele in ordinea initiala
    tinit = time.time()
    radixsort()
    tfin = time.time()
    if sortedtest("radixsort baza " + str(b)):
        print("radixsort in baza ", b, " a sortat cu succes; timp de executie: ", tfin - tinit)

    vaux = [v[i] for i in range(n)]  # copie a vectorului cu elementele in ordinea initiala
    naux = n  # copie a lui n pentru usurinta implementarii heapsort
    tinit = time.time()
    heapsort()
    tfin = time.time()
    if sortedtest("heapsort"):
        print("heapsort a sortat cu succes; timp de executie: ", tfin - tinit)

    vaux = [v[i] for i in range(n)]
    tinit = time.time()
    heapsort2(vaux)
    tfin = time.time()
    print("heapsort de pe 'net: ", tfin - tinit)

    if selectionsortok == 1:
        print("selection sort urmeaza sa fie rulat," + '\033[93m' + " poate dura ~ zeci de secunde..." + '\033[0m', end = ' ')
        vaux = [v[i] for i in range(n)]
        tinit = time.time()
        selectionsort()
        tfin = time.time()
        if sortedtest("selectionsort"):
            print("selectionsort a sortat cu succes; timp de executie: ", tfin - tinit)

    tinit = time.time()
    v.sort()
    tfin = time.time()

    if n < 10:
        print("elemente sortate (cu ajutorul functiei native): ", end=' ')
        for i in range(n):
            print(v[i], end = ' ')

    print(" timp de executie al sortarii native: ", tfin - tinit)
    print()