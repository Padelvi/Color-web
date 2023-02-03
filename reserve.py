def rgba2rgb(rgba, bck):
    return (
        ((1 - rgba[3]) * background[0]) + (rgba[3] * rgba[0]),
        ((1 - rgba[3]) * background[1]) + (rgba[3] * rgba[1]),
        ((1 - rgba[3]) * background[2]) + (rgba[3] * rgba[2]),
    )
