from data import p


def nbvcxw(h):
    return "".join([chr(x) for x in h])


def poiuy(s):
    q = []
    for noooo in s:
        if noooo in p:
            q.extend(p[noooo])
        else:
            return None
    return nbvcxw(q)


dfzg = [
    "Vous dévidez vos cours",
    "Que vous pendîtes à nos trames",
    "Et ce Destin qui nous conduit",
    "Ainsi vous plaît, Etoiles",
    "Je vous salue, heureuses flammes",
    "Tandis que tous les jours",
    "Etoiles, filles de la Nuit"
]

t_cntct = poiuy(dfzg)
if t_cntct:
    print(t_cntct)
