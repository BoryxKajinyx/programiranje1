from primer_modula import *
# uvozi vse funkcije iz modula math
# ni dobro, ker ne veš iz katerega modula katera poklicana funkcija pride
primer_funkcije_1()

import primer_modula
# uvozi modul math
# boljše, za klicanje se navede modul in je jasno, iz kje pride poklicana funkcija
primer_modula.primer_funkcije_1()

from primer_modula import primer_funkcije_1
# uvozi samo določene funkcije
# uporabi se, ko je funkcija zelo znana (vsak ve, od kje pride) in se zelo pogosto uporablja v programu
primer_funkcije_1()

# module se uvaža na začetku programa, razen v izjemnih primerih:
#   traja dosti časa, da se uvozi
#   modul mogoče ne obstaja
#   modul se zelo redko uporablja
#   v tej datoteki

primer_funkcije_2("a")
