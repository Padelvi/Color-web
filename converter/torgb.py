from converter import hextodec

def fromhex(hexv):
    global r,g,b,hr,hg,hb
    hr = hexv[0] + hexv[1]
    hg = hexv[2] + hexv[3]
    hb = hexv[4] + hexv[5]
    r = hextodec(hr)
    g = hextodec(hg)
    b = hextodec(hb)
    return (r,g,b)

def fromrgba(rgba):
    return rgba
