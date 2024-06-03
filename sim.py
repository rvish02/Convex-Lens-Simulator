from turtle import *
from math import *

width(1.5)
mode("standard")
lens_size = 40


def find(eq1, eq2):
    _1x1, _1y1, _1x2, _1y2 = eq1[0][0], eq1[0][1], eq1[1][0], eq1[1][1]
    _2x1, _2y1, _2x2, _2y2 = eq2[0][0], eq2[0][1], eq2[1][0], eq2[1][1]
    m1 = (_1y2 - _1y1) / (_1x2 - _1x1)
    m2 = (_2y2 - _2y1) / (_2x2 - _2x1)
    x = ((m1 * _1x1) - (m2 * _2x1) - _1y1 + _2y1) / (m1 - m2)
    y = (m1 * (x - _1x1)) + _1y1
    return x, y


def convex_lens_simulater(f, h1, u):
    reset()
    lens_apeture = 150
    if h1 > lens_apeture:
        lens_apeture = h1 + 30
    try:
        "principal axis"
        pu()
        bk(f * 2)
        dot(7)
        pd()
        fd(f)
        color("blue")
        dot(7)
        width(3)
        fd(f)
        dot(7)
        fd(f)
        dot(7)
        color("black")
        width(1.3)
        fd(f)
        dot(7)

        "lens"
        co, x, a, = (
            [],
            0,
            lens_apeture,
        )
        pu()
        p = lens_size
        for run in range(p):
            try:
                y = sqrt(4 * a * x)
                co.append((x - p, y))
                goto(x - p, y)
                pd()
                x = x + 1
            except:
                break
        pu()
        for e in co[::-1]:
            goto(e[0], -e[1])
            pd()
        pu()
        for e in co:
            goto(-e[0], -e[1])
            pd()
        pu()
        for e in co:
            goto(-e[0], e[1])
            pd()
        "dotted line of the lens"
        dis = distance(pos()[0], -pos()[0])
        space = 15
        right(90)
        pu()
        for x in range(space * 2):
            if x % 2 == 0:
                pd()
                fd(dis / space)
                pu()
            else:
                fd(dis / space)
        "object"
        pu()
        home()
        bk(u)
        pd()
        color("red")
        width(3)
        left(90), fd(h1)
        stamp()
        color("black")
        width(1.3)
        right(90)
        fd(u / 2)
        stamp(), fd(u / 2)
        stamp()
        goto(f, 0)
        for i in range(1, 5):
            goto(f * (i + 1), -h1 * i)
        pu()
        home()
        pu()
        goto(-u, h1)
        pd()
        goto(0, 0)
        stamp()
        goto(u * 4, -h1 * 4)
        pu()
        e1 = [(f, 0), (0, h1)]
        e2 = [(-u, h1), (0, 0)]
        common_pt = find(e1, e2)
        goto(common_pt[0], 0)
        right(90)
        pd()
        color("yellow")
        width(3)
        goto(common_pt[0], common_pt[1])
        stamp()
        color("black")
        width(1.3)
        if common_pt[0] < 0:
            color("yellow"), left(180)
            stamp()
            color("black")
            goto(0, h1)
            pu()
            goto(common_pt[0], common_pt[1])
            pd()
            goto(-u, h1)
        # extend principal axis
        pu()
        color("black")
        if common_pt[0] < 0:
            goto(common_pt[0], 0)
            pd()
            goto(-f, 0)
        else:
            goto(common_pt[0], 0)
            pd()
            goto(f, 0)
        return h1, common_pt[1], u, common_pt[0], common_pt[1] / h1
    except:
        return None


if __name__ == "__main__":
    convex_lens_simulater(f=100, h1=90, u=70)
