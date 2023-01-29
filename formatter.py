from converter import dectohex, hextodec

class Rgb:
    def __init__(self, rgb, target):
        self.rgb = rgb
        self.target = target

    def rgba(self):
        rgba_ra = self.rgb[0]
        rgba_ga = self.rgb[1]
        rgba_ba = self.rgb[2]
        rgba_a = 1
        return [rgba_ra, rgba_ga, rgba_ba, rgba_a]

    def hex(self):
        hex_r = dectohex(self.rgb[0])
        hex_g = dectohex(self.rgb[1])
        hex_b = dectohex(self.rgb[2])
        return hex_r+hex_g+hex_b

    def convert(self):
        if self.target == 'rgba':
            return self.rgba()
        if self.target == 'hex':
            return self.hex()

class Rgba(Rgb):
    def __init__(self, rgba, target):
        self.rgba = rgba
        self.target = target

    def rgb(self):
        return [self.rgba[0], self.rgba[1], self.rgba[2]]

    def convert(self):
        result = self.rgb()
        if self.target == 'hex':
            return Rgb.hex(result)
        else:
            return result

class Hex(Rgb):
    def __init__(self, hexv, target):
        self.hexv = hexv
        self.target = target

    def rgb():
        hex_r = self.hexv[0] + self.hexv[1]
        hex_g = self.hexv[2] + self.hexv[3]
        hex_b = self.hexv[4] + self.hexv[5]
        rgb_r = hextodec(hex_r)
        rgb_g = hextodec(hex_g)
        rgb_b = hextodec(hex_b)
        return [rgb_r, rgb_g, rgb_b]

    def convert(self):
        result = self.rgb()
        if self.target == 'rgba':
            return Rgb.rgba(result)
        else:
            return result
