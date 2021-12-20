import random


def svg_head():
    return """
<svg
xmlns="http://www.w3.org/2000/svg" 
xml:lang="en" 
xmlns:xlink="http://www.w3.org/1999/xlink"
viewBox="100 100 600 800"
width="800">
  <filter id='shadow' color-interpolation-filters="sRGB">
    <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.4"/>
  </filter>
    """

def svg_foot():
    return """</svg>"""

def qcircle():
    return """
    <path fill="none" stroke="green" stroke-opacity="0.3" stroke-width="8" d="M20,0 a20,20 0 0,1 20,20" />
    """

def circle(cx: int, cy: int, r: float, style: str):
    return (
        f'<circle '
        f'cx="{cx}" '
        f'cy="{cy}" '
        f'r="{r}"'
        f'{style}'
        f'/>'
    )

def get_color():
    # 20b - high sat
    _colors = """
        #393b79
        #5254a3
        #6b6ecf
        #9c9ede
        #637939
        #8ca252
        #b5cf6b
        #cedb9c
        #8c6d31
        #bd9e39
        #e7ba52
        #e7cb94
        #843c39
        #ad494a
        #d6616b
        #e7969c
        #7b4173
        #a55194
        #ce6dbd
        #de9ed6
    """
    colors = [x.strip() for x in _colors.splitlines()]
    # colors = _colors.splitlines().trim()
    return colors[random.randrange(0,len(colors))]

def style():
    return (
        f'fill="{get_color()}" '
        f'stroke="black"'
        f'fill-opacity="0.5"'
        f'filter="url(#shadow)"'
        f'stroke-width="2"'
    )

def more_circles(count: int):
    min_r = 20
    max_r = 80
    w = 1000
    h = 1000
    ret =''
    for i in range(count):
        ret = f"""
        {ret}
        {circle(
            random.randrange(max_r,w-max_r, 1),
            random.randrange(max_r,h-max_r, 1),
            random.randrange(min_r,max_r, 1),
            style()
            )}
        """
    return ret

def circle_quart(d: dict):
    return """
    <path 
    fill="none" 
    stroke="green" 
    stroke-opacity="0.3" 
    stroke-width="8" 
    d="M20,0 a20,20 0 0,1 20,20" 
    />
    """.format(**d)

def lines():
    # TODO: add symmetry and repetition
    q1 = { 'fill': 'red'}
    return (
        f'{svg_head()}'
        # f'{qcircle()}'
        # f'{circle_quart(q1)}'
        # f'{circle(10, 10, 10, style())}'
        f'{more_circles(250)}'
        f'{svg_foot()}'
    )

def test_artboard_test():
    with open("docs/content/svg/quarter_circles.svg", "w") as the_file:
        # values = make_tiles(10, 10, 1000, sw=2)
        # the_file.write(tmpl.render(groups = groups))
        the_file.write(lines())