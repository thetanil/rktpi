import random


class C:
    w = 1920
    h = 1080


def svg_head(
    vbxmin: int = 0,
    vbymin: int = 0,
    vbw: int = C.w,
    vbh: int = C.h,
    width: str = C.w,
    height: str = "",
):
    return f"""
        <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="{vbxmin} {vbymin} {vbw} {vbh}"
        stroke="black" stroke-width="4">
        <filter id='shadow' color-interpolation-filters="sRGB">
            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.4"/>
        </filter>
        <filter id='shadow2' color-interpolation-filters="sRGB">
            <feDropShadow dx="0" dy="0" stdDeviation="5.5" flood-opacity=".8"/>
        </filter>
        <filter id='shadow3' color-interpolation-filters="sRGB">
        <feDropShadow dx="10" dy="10" stdDeviation="0"
          flood-color="teal" flood-opacity="0.5"/>
        </filter>
        <g >
        <rect x="0" y="0" width="100%" height="100%" fill="#ccc"
                stroke-width="8" stroke="none" />
        </g>
    """


def svg_foot():
    return """</svg>"""


def line(
    x1: int = 0, y1: int = 80, x2: int = 100, y2: int = 120, suffix=""
) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {suffix}/>'


# transform in place
# https://stackoverflow.com/questions/23899718/scale-and-mirror-svg-object/23902773


# def line():
#     return (
#         f'<polygon points="100,0,100,100,0,100" '
#         f'transform="translate(200,200) scale(-1,2)"/>'
#     )


# def lines():
#     return f"{line()}"


def get_color():
    _colors = """
        #cb997e
        #ddbea9
        #ffe8d6
        #b7b7a4
        #a5a58d
        #6b705c
        """
    colors = [x.strip() for x in _colors.splitlines()]
    # colors = _colors.splitlines().trim()
    return colors[random.randrange(0, len(colors))]


def get_color02():
    colors = [
        "001219",
        "005f73",
        "0a9396",
        "94d2bd",
        "e9d8a6",
        "ee9b00",
        "ca6702",
        "bb3e03",
        "ae2012",
        "9b2226",
    ]

    # colors = ["264653", "2a9d8f", "e9c46a", "f4a261", "e76f51"]
    return f"#{colors[random.randrange(0, len(colors))]}"


def purple():
    return f'stroke="{get_color()}" stroke-width="{random.randint(1,30)}"'


def style():
    return (
        f" "
        # f'fill="{get_color()}" '
        # f'fill-opacity="0.8" '
        # f'stroke="none" '
        f'stroke="{get_color()}" '
        f'stroke-width="{random.randint(8,32)}" '
        f'stroke-dasharray="32 64 128" '
        # f'stroke-width="2" '
        f'filter="url(#shadow3)" '
    )


def lines():
    _lines = []
    for i in range(10):
        _lines.append(
            line(
                random.randint(0, C.w),
                random.randint(0, C.h),
                random.randint(0, C.w),
                random.randint(0, C.h),
                style(),
            )
        )
    return _lines


def test_artboard_lines01():
    with open("docs/content/svg/lines01.svg", "w") as the_file:
        the_file.write((f"{svg_head()}" f"{lines()}" f"{svg_foot()}"))


def style02():
    return (
        f" "
        # f'fill="{get_color()}" '
        # f'fill-opacity="0.8" '
        # f'stroke="none" '
        f'stroke="{get_color02()}" '
        f'stroke-width="{random.randint(8,64)}" '
        f'stroke-linecap="round" '
        # f'stroke-dasharray="8 16 32" '
        # f'stroke-width="2" '
        f'filter="url(#shadow2)" '
    )


def wrap_in_transform(line: str, trans: str = "") -> str:
    return f'<g transform="{trans}" > {line} </g>'


def line02(
    x1: int = 0, y1: int = 80, x2: int = 100, y2: int = 120, suffix=""
) -> str:
    return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {suffix}>
            <animateTransform attributeName="transform"
                          attributeType="XML"
                          type="rotate"
                          from="0 60 70"
                          to="360 60 70"
                          dur="10s"
                          repeatCount="indefinite"/></line>"""


def lines02() -> str:
    _lines = []
    for i in range(16):
        next_line = line02(
            random.randint(-C.w, C.w),
            random.randint(-C.h, C.h),
            random.randint(-C.w, C.w),
            random.randint(-C.h, C.h),
            style02(),
        )
        next_line += wrap_in_transform(
            next_line,
            (
                f"translate({C.w/2}, 0) "
                # f"translate(200,0) "
                f"scale(-1, 1) "
                f"translate(-{C.w/2}, 0) "
                # f"scale(2, 2) scale(1, 1) "
                f"rotate(180, {C.w/2}, {C.h/2})"
            ),
        )
        next_line += wrap_in_transform(
            next_line,
            (
                f"translate({C.w/2}, 0) "
                # f"translate(200,0) "
                f"scale(-1, 1) "
                f"translate(-{C.w/2}, 0) "
                # f"scale(2, 2) scale(1, 1) "
                # f"rotate(0, {C.w/2}, {C.h/2})"
            ),
        )

        _lines.append(next_line)
    # return "\n".join(_lines)
    joined = "\n".join(_lines)
    return (
        f"{joined}"
        # f'<g transform="scale(-1, 1) translate(-{C.w},0)">{joined}</g>'
        # f'<g transform="scale(1, -1) translate(0,-{C.h})">{joined}</g>'
        # f'<g transform="scale(-1, -1) translate(-{C.w},-{C.h})">{joined}</g>'
    )


def test_artboard_lines02():
    with open("docs/content/svg/lines02.svg", "w") as the_file:
        the_file.write((f"{svg_head()}" f"{lines02()}" f"{svg_foot()}"))
