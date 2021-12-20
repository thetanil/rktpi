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
    """


def svg_foot():
    return """</svg>"""


def qcircle():
    return """
    <path fill="none" stroke="green" stroke-opacity="0.3" stroke-width="8" d="M20,0 a20,20 0 0,1 20,20" />
    """


def circle(cx: int, cy: int, r: float, style: str):
    return f"<circle " f'cx="{cx}" ' f'cy="{cy}" ' f'r="{r}"' f"{style}" f"/>"


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


def style():
    return (
        f'fill="{get_color()}" '
        f'stroke="black"'
        f'fill-opacity="0.5"'
        f'filter="url(#shadow)"'
        f'stroke-width="2"'
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
            style()
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


def is_valid(c, list):
    pass


def packed_circles(
    xmin: int = 0,
    xmax: int = 100,
    ymin: int = 0,
    ymax: int = 100,
    rmin: int = 0,
    rmax: int = 100,
) -> str:
    ret = ""
    max_count = 100
    circles = []
    for i in range(max_count):
        possible = (
            random.randrange(xmin, xmax, 1),
            random.randrange(ymin, ymax, 1),
            random.randrange(rmin, rmax, 1),
        )
        if is_valid(possible, circles):
            circles.append(possible)

    for i in range(max_count):
        possible = circle(
            random.randrange(xmin, xmax, 1),
            random.randrange(ymin, ymax, 1),
            random.randrange(rmin, rmax, 1),
            style(),
        )

    return ret


def lines():
    # TODO: add symmetry and repetition
    # q1 = {"fill": "red"}
    return (
        f"{svg_head(width=800)}"
        # f'{qcircle()}'
        # f'{circle_quart(q1)}'
        # f'{circle(10, 10, 10, style())}'
        # f'{more_circles(100)}'
        f"{packed_circles()}"
        f"{svg_foot()}"
    )


def test_artboard_test():
    with open("docs/content/svg/quarter_circles.svg", "w") as the_file:
        # values = make_tiles(10, 10, 1000, sw=2)
        # the_file.write(tmpl.render(groups = groups))
        the_file.write(lines())
