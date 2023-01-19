from converter import dectohex
from user import hexv,ra,ga,ba,a

def tohex(rgb):
    global hexv,ra,ga,ba
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    hr = dectohex(r)
    hg = dectohex(g)
    hb = dectohex(b)
    return hr+hg+hb

def torgba(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return rgb
