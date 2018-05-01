x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# x = [4, 6, 1, 3, 5, 7, 25]


def draw_stars(x):
    
    for i in x:
        if type(i) is int:
            for s in range(0,i):
                print "*",
            print("")
        else:
            for s in range(0,len(i)):
                
               print i[0].lower(),
            print("")




draw_stars(x)
