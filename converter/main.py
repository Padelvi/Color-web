import torgb, fromrgb

colorlist = ['rgb', 'hex']
result = []

# if colorlist[0] == 'rgb':
    # result=(r,g,b)
    # print(result)
    # rgb = result
    # print(rgb)
# elif colorlist[0] == 'rgba':
    # result=(ra,ga,ba,a)
    # bck = (br,bg,bb)
    # print(result)
    # rgb = torgb.fromrgba(result, bck)
    # print(rgb)
# else:
    # result=hexv
    # print('#'+result)
    # rgb = torgb.fromhex(result)
    # print(rgb)

# output = {
    # 'rgb': rgb,
    # 'rgba': fromrgb.torgba(rgb),
    # 'hex': fromrgb.tohex(rgb)
# }

source = {
    'rgb': result
    'rgba': fromrgb.torgba(result)
    'hex': fromrgb.tohex(result)
}

rgb = source[colorlist[0]]
