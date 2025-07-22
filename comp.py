a=[]
for x in range(5):
    a.append(x**2)
print(a)


a=[x**2 for x in range(5)]
print(a)


b=[x for x in range(10)if x%2==0]
print(b)


ages={"john":10,"jeo":20,"jivin":30}
print(ages)