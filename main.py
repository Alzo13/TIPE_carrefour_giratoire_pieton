import traceback
from generate_peoples import *



run = True

# Dictionnaire contenant les ellipses tkinter
dotarray = {}
for p in peoples :
    dotarray[p] = p.get_forme(window.canvas)

# Liste des temps passés dans le rond-point
times = [0]


try :
    while len(peoples) > 0:
        #time.sleep(0.001)
        for p in peoples :
            p.update_acceleration(peoples,rplist,murs,coins,(width/2,height/2))
        for p in peoples :
            window.canvas.delete(dotarray[p])
            dotarray[p] = p.get_forme(window.canvas)
            p.update()
            if p.arrive():
                window.canvas.delete(dotarray[p])
                peoples.pop(peoples.index(p))
                if p.t > 30 :
                    #print((p.t*Tau))
                    times.append((p.t*Tau))

        window.update()
    window.destroy()
except :
    window.destroy()
    traceback.print_exc()
finally :
    print("\n Nombre de points : ",len(times)-1)
    print("moyenne : ",sum(times)/(len(times)-1))
    print("min : ",times[0] if len(times) == 1 else times[1])
    print("médiane : ",times[(len(times))//2])
    print("max : ",times[-1])
    print()