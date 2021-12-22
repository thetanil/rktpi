import random


def svg_head(
    vbxmin: int = 0,
    vbymin: int = 0,
    vbw: int = 1000,
    vbh: int = 1000,
    width: str = "50vw",
    height: str = "",
):
    return f"""
        <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="{vbxmin} {vbymin} {vbw} {vbh}"
        width="{width}">
        <filter id='shadow' color-interpolation-filters="sRGB">
            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.4"/>
        </filter>
        <filter id='shadow2' color-interpolation-filters="sRGB">
            <feDropShadow dx="0" dy="0" stdDeviation="5.5" flood-opacity=".8"/>
        </filter>
    """


def svg_foot():
    return """</svg>"""


def qcircle():
    return """
    <path fill="none" stroke="green" stroke-opacity="0.3"
    stroke-width="8" d="M20,0 a20,20 0 0,1 20,20" />
    """


def circle(cx: int, cy: int, r: float, style: str):
    return f"<circle " f'cx="{cx}" ' f'cy="{cy}" ' f'r="{r}"' f"{style}" f"/>"


def get_color2():
    _colors = """
        #d73027
        #f46d43
        #fdae61
        #fee090
        #ffffbf
        #e0f3f8
        #abd9e9
        #74add1
        #4575b4
        """
    colors = [x.strip() for x in _colors.splitlines()]
    # colors = _colors.splitlines().trim()
    return colors[random.randrange(0, len(colors))]


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
    return colors[random.randrange(0, len(colors))]


def style3():
    return (
        f'fill="{get_color()}" '
        f'stroke="none"'
        f'fill-opacity="0.8"'
        f'filter="url(#shadow)"'
    )


def style2():
    return (
        f'fill="{get_color()}" '
        f'stroke="black"'
        f'fill-opacity="0.4"'
        f'filter="url(#shadow)"'
        f'stroke-width="2"'
    )


def style1():
    return (
        f'fill="{get_color2()}" '
        f'stroke="none"'
        f'fill-opacity=".6"'
        f'filter="url(#shadow2)"'
    )


def style():
    return (
        f'fill="{get_color()}" '
        f'stroke="none"'
        f'fill-opacity="0.8"'
        f'filter="url(#shadow)"'
        # f'stroke-width="2"'
    )


def more_circles(count: int) -> str:
    min_r = 50
    max_r = 120
    w = 1000
    h = 1000
    ret = ""
    for i in range(count):
        ret = f"""
        {ret}
        {circle(
            random.randrange(max_r,w-max_r, 1),
            random.randrange(max_r,h-max_r, 1),
            random.randrange(min_r,max_r, 1),
            style2()
            )}
        """
    return ret


def more_circles2(count: int) -> str:
    min_r = 50
    max_r = 120
    w = 1000
    h = 1000
    ret = ""
    for i in range(count):
        ret = f"""
        {ret}
        {circle(
            random.randrange(max_r,w-max_r, 1),
            random.randrange(max_r,h-max_r, 1),
            random.randrange(min_r,max_r, 1),
            style3()
            )}
        """
    return ret


# def circle_quart(d: dict) -> str:
#     return """
#     <path
#     fill="none"
#     stroke="green"
#     stroke-opacity="0.3"
#     stroke-width="8"
#     d="M20,0 a20,20 0 0,1 20,20"
#     />
#     """.format(**d)

# import typing.List
# import typing.Tuple


def is_valid(possible, circles):
    import math

    x1, y1, r1 = possible
    for c in circles:
        x2, y2, r2 = c
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if d < r1 + r2:
            return False
    return True


def packed_circles(
    xmin: int = 1,
    xmax: int = 1000,
    ymin: int = 1,
    ymax: int = 1000,
    rmin: int = 8,
    rmax: int = 96,
) -> str:
    ret = ""
    max_count = 1000
    circles = []
    for i in range(max_count):
        possible = (
            random.randrange(xmin, xmax),
            random.randrange(ymin, ymax),
            random.randrange(rmin, rmax),
        )
        if is_valid(possible, circles):
            circles.append(possible)

    assert len(circles) >= 10

    for c in circles:
        ret += circle(*c, style())

    return ret


def packed_circles2(
    xmin: int = 0,
    xmax: int = 1100,
    ymin: int = 0,
    ymax: int = 900,
    rmin: int = 60,
    rmax: int = 160,
) -> str:
    ret = ""
    max_count = 1000000
    circles = []
    for i in range(max_count):
        possible = (
            random.randrange(xmin, xmax),
            random.randrange(ymin, ymax),
            random.randrange(rmin, rmax),
        )
        if is_valid(possible, circles):
            circles.append(possible)

        if len(circles) >= 20:
            break

    assert len(circles) >= 20

    for c in circles:
        ret += circle(*c, style1())

    return ret


def symmetry():
    tile = packed_circles()

    tile = (
        f'<g transform="scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(180, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(90, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(270, 500,500)scale(.5,.5)">{tile}</g>'
        # f'<g transform="rotate(45,500,500), scale(2,2)">{tile}</g>'
    )

    return (
        f'<g transform="scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(180, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(90, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(270, 500,500)scale(.5,.5)">{tile}</g>'
        # f'<g transform="rotate(45,500,500), scale(2,2)">{tile}</g>'
    )


def symmetry2():
    tile = packed_circles2()

    tile = (
        f'<g transform="scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(180, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(90, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(270, 500,500)scale(.5,.5)">{tile}</g>'
        # f'<g transform="rotate(45,500,500), scale(2,2)">{tile}</g>'
    )

    tile = (
        f'<g transform="scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(180, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(90, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(270, 500,500)scale(.5,.5)">{tile}</g>'
        # f'<g transform="rotate(45,500,500), scale(2,2)">{tile}</g>'
    )

    return (
        f'<g transform="scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(180, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(90, 500,500)scale(.5,.5)">{tile}</g>'
        f'<g transform="rotate(270, 500,500)scale(.5,.5)">{tile}</g>'
        # f'<g transform="rotate(45,500,500), scale(2,2)">{tile}</g>'
    )


def test_artboard_circles01():
    with open("docs/content/svg/circles01.svg", "w") as the_file:
        the_file.write(
            (f"{svg_head(width=800)}" f"{more_circles(50)}" f"{svg_foot()}")
        )


def test_artboard_circles02():
    with open("docs/content/svg/circles02.svg", "w") as the_file:
        the_file.write(
            (f"{svg_head(width=800)}" f"{more_circles2(100)}" f"{svg_foot()}")
        )


def test_artboard_circles03():
    with open("docs/content/svg/circles03.svg", "w") as the_file:
        the_file.write(
            (f"{svg_head(width=800)}" f"{packed_circles()}" f"{svg_foot()}")
        )


def test_artboard_circles04():
    with open("docs/content/svg/circles04.svg", "w") as the_file:
        the_file.write(
            (f"{svg_head(width=800)}" f"{symmetry()}" f"{svg_foot()}")
        )


def test_artboard_circles05():
    uhg = svg_head(vbxmin=0, vbymin=0, vbw=1000, vbh=1000, width=800)
    with open("docs/content/svg/circles05.svg", "w") as the_file:
        the_file.write((f"{uhg}" f"{symmetry2()}" f"{svg_foot()}"))
