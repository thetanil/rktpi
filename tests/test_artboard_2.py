# import pytest
# import os
import random


def draw_line(
    x,
    y,
    length,
    pos,
    size,
    sections,
    top_left_x,
    top_left_y,
    sw,
    sym=False,
    color="blue",
):
    """returns the svg xml for the line
    Params:
    x - starting x value
    y - starting y value
    length - number of squares across and down
    pos - whether the gradient is positive or negative
    size - the size of each square in the grid
    topleftX - the starting point for the tile x value
    topleftY - the starting point for the tile y value
    sw - strokewidth
    sym - whether this is the symmtrical duplicate of another line
    color of the stroke
    """
    if sym:
        length = -length
    x2 = x + length
    if pos:
        y2 = y - length
    else:

        y2 = y + length

    if x2 < 0:
        y2 = y2 + x2
        x2 = 0
    if y2 < 0:
        x2 = x2 + y2
        y2 = 0
    # don't actually know why I need this -- dumb computers
    if sym and pos:
        temp = x2
        x2 = y2
        y2 = temp

    # depending on all the above conditions output the format for the line
    return f'<line x1="{top_left_x + x * size}" y1="{top_left_y + y * size}" x2="{top_left_x + x2 * size}" y2="{top_left_y + y2 * size}" stroke-linecap="square" stroke-width="{sw}" stroke="{color}" />'
    # return f'<line x1="{x * size + top_left_x}" y1="{y * size + top_left_y}" x2="{x2 * size + top_left_x}" y2="{y2 * size + top_left_y}" stroke-linecap="square" stroke-width="{sw}" stroke="{color}" />'


def create_lines(sections):
    # Make lines (not actually unique) in the bottom right diagonal half
    # of the bottom quadrant and then repeats in all the places
    num_lines = random.randint(sections // 2, int(sections * 1.5))
    point_set = set()
    lines = []
    neg = True
    # repeats ignoring duplicate points
    while len(lines) < num_lines:
        # get a random even number for x adn y
        x = random.randint(0, sections // 2 - 1) * 2
        y = random.randint(0, x // 2) * 2

        # calculate the maximum length
        top = sections - x - y if x == y and x == 2 else sections - x
        # pick a random length between 1 and the maximum
        length = random.randint(1, top)
        # alternate the positivity of the gradient depending on starting point
        pos = x in (2, 4) and y in (2, 4)

        if (x, y) not in point_set:
            lines.append((x, y, length, pos))
            point_set.add((x, y))
    return lines


def make_tiles(size, tiles, image_size, sw=1):
    # takes number of sections in each quadrant (indicates intricacy)
    # tiles is the number of repetitions across and down
    # imagesize is number of pixels across and down but it also affects
    # the relative stroke width --> sw is stroke width
    image_pad = 50
    header = f'<svg viewBox="-{image_pad} -{image_pad} {image_size + 2 * image_pad} {image_size + 2 * image_pad}" xmlns="http://www.w3.org/2000/svg">\n'
    output = []
    output.append(header)

    tile_size = image_size / tiles
    padding = image_size / tiles / 2
    padding = 0
    sections = size
    for row in range(tiles):
        for column in range(tiles):
            # cutting off at the border is not working

            # make a tile quadrant group (without <g> wrapping just yet)
            group = ""
            top_left_x = column * tile_size + padding / 2
            top_left_y = row * tile_size + padding / 2
            # print(top_left_x, top_left_y)
            square_size = ((tile_size - padding) / size) / 2
            lines = create_lines(sections)
            for line in lines:
                # do the same thing (ish) in the four different quadrants
                x, y, length, pos = line
                x1 = x
                y1 = y

                # print(x1,y1,length,pos,a,b)
                l = draw_line(
                    x1,
                    y1,
                    length,
                    pos,
                    square_size,
                    sections,
                    top_left_x,
                    top_left_y,
                    sw,
                )
                group += l + "\n"
                # x, y, length, pos, size, sections, top_left_x, top_left_y, sw, sym=False, color='black'
                if x != y or pos:
                    x1 = y
                    y1 = x
                    l2 = draw_line(
                        x1,
                        y1,
                        -length,
                        pos,
                        square_size,
                        sections,
                        top_left_x,
                        top_left_y,
                        sw,
                        sym=True,
                    )
                    # x, y, length, pos, size, sections, top_left_x, top_left_y, sw, sym=False, color='black'
                    group += l2 + "\n"

            # repeat this quadrant 3 more times
            for quad in range(4):
                rotation = quad * 90
                rotationX = top_left_x + (tile_size - padding) / 2
                rotationY = top_left_y + (tile_size - padding) / 2
                output.append(
                    f'<g transform="rotate({rotation} {rotationX} {rotationY})">{group}</g>'
                )

    footer = f"</svg>"
    output.append(footer)
    return output


svg_wrapper = """\
<svg
xmlns="http://www.w3.org/2000/svg" 
xml:lang="en" 
xmlns:xlink="http://www.w3.org/1999/xlink"
viewBox="0 0 1000 1000" 
width="1000">
<rect 
    id="background" 
    x="0" 
    y="0" 
    width="50" 
    height="50" 
    fill="{{ layout.color.background if layout else 'lightblue'}}" 
    />

<circle cx="50" cy="50" r="40" stroke="lightblue" stroke-width="4" fill="lightyellow" />
<circle cx="100" cy="100" r="60" stroke="purple" stroke-width="8" fill="orange" fill-opacity="0.4" stroke-opacity="0.4"/>

<path fill="none" stroke="red" stroke-opacity="0.3" stroke-width="4" d="M20,0 a20,20 0 0,1 20,20" />

{{groups}}
</svg>
"""

# https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md
""" 20b - high sat
393b79 #393b79
5254a3 #5254a3
6b6ecf #6b6ecf
9c9ede #9c9ede
637939 #637939
8ca252 #8ca252
b5cf6b #b5cf6b
cedb9c #cedb9c
8c6d31 #8c6d31
bd9e39 #bd9e39
e7ba52 #e7ba52
e7cb94 #e7cb94
843c39 #843c39
ad494a #ad494a
d6616b #d6616b
e7969c #e7969c
7b4173 #7b4173
a55194 #a55194
ce6dbd #ce6dbd
de9ed6 #de9ed6
"""

# https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md
""" category20c - lower sat
3182bd #3182bd
6baed6 #6baed6
9ecae1 #9ecae1
c6dbef #c6dbef
e6550d #e6550d
fd8d3c #fd8d3c
fdae6b #fdae6b
fdd0a2 #fdd0a2
31a354 #31a354
74c476 #74c476
a1d99b #a1d99b
c7e9c0 #c7e9c0
756bb1 #756bb1
9e9ac8 #9e9ac8
bcbddc #bcbddc
dadaeb #dadaeb
636363 #636363
969696 #969696
bdbdbd #bdbdbd
d9d9d9 #d9d9d9
"""

# https://colorbrewer2.org/#type=diverging&scheme=RdYlBu&n=6
""" cat6 
#d73027
#fc8d59
#fee090
#e0f3f8
#91bfdb
#4575b4
"""


def test_artboard_2():
    import jinja2

    tmpl = jinja2.Template(svg_wrapper)

    with open("docs/static/svg/artboard_2.svg", "w") as the_file:
        # values = make_tiles(10, 10, 1000, sw=2)
        the_file.write(tmpl.render())


def test_artboard_test():
    import jinja2

    tmpl = jinja2.Template(svg_wrapper)

    with open("docs/content/svg/test.svg", "w") as the_file:
        # values = make_tiles(10, 10, 1000, sw=2)
        the_file.write(tmpl.render())
