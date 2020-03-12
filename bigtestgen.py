import random

f = open("input.txt", "a")
f.write('\n')

for i in range(10):
    n = random.randint(30000, 100000)
    f.write(str(n))
    f.write('\n')
    f.write(str(256))
    f.write('\n')
    v = [str(random.randint(1, 100000)) for j in range(n)]
    s = " ".join(v)
    f.write(s)
    f.write('\n')

# in fisierul input trebuie introdus numarul de teste manual