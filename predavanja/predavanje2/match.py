tocka = (5, 3)
match tocka:
    case (0, 0):
        print("izhodišče")
    case (0,t) if t > 0:
        print("Na osi y, za ", t, " višje od izhodišča")
    case(0, t) if t < 0:
        print("Na osi y, za ", t, " nižje od izhodišča")
    case (t,0):
        print("Na osi x in sicer na dožini ",t)
    case (x, y):
        print("Ni na osi, temveč je", x, y)
    case(x,y,z):
        print("V prostoru")