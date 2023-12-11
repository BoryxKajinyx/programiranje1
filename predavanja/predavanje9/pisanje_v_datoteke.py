f = open("besedilo", "w")
f.write("aaaaa")
f.writelines(["a", "a", "a"])
# pravilni način:
with open("besedilo", "w") as d:
    d.write("Besedilo")
# po izvedbi se zapre

#  #
open("dejstvo.txt", "w", encoding="utf-8").write("Sašo žre čevapčiče pri Đoletu Dodiću.")
a = "Sašo žre čevapčiče".encode("cp1250").decode("cp1250")
