def fileWrite(filename):
    fopen = open(filename, "w+")
    for i in range(10):
        fopen.write("My name is %s. This is line %d\n"%("Oscar Lopez", i))
    fopen.close()

def csvWrite(filename, names, ages):
    f = open(filename, "w+")
    f.write("id, name, age")

    for i in range(len(names)):
        f.write("%d, %s, %d\n"%(i, names[i], ages[i]))
    f.close()

fileWrite("SaturdayClass.txt")
names = ["al", "bob", "oscar", "charlie", "Dave", "Ian", "Marcos"]
ages = [20, 19, 30, 45, 90, 22, 15]

csvWrite("myCSV.csv", names, ages)
