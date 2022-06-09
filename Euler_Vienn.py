import shapely.geometry as sg
import matplotlib.pyplot as plt
import descartes

A = {1, 4, 5, 7}
B = {2, 5, 7, 6}
C = {3, 4, 7, 6}


def euler(d, t=''):
    a = sg.Point(-0.5, 1).buffer(1.)
    b = sg.Point(0.5, 1).buffer(1.)
    c = sg.Point(0, 0.0).buffer(1.)

    part_1 = a.difference(b.union(c))
    part_2 = b.difference(a.union(c))
    part_3 = c.difference(b.union(a))
    part_4 = a.intersection(c).difference(c.intersection(b))
    part_5 = a.intersection(b).difference(b.intersection(c))
    part_6 = b.intersection(c).difference(c.intersection(a))
    part_7 = a.intersection(b.intersection(c))
    parts = [None, part_1, part_2, part_3, part_4, part_5,
             part_6, part_7]

    ax = [descartes.PolygonPatch(a, fc='b', ec='black', alpha=0.1),
          descartes.PolygonPatch(b, fc='g', ec='black', alpha=0.1),
          descartes.PolygonPatch(c, fc='r', ec='black', alpha=0.1)]
    for x in d:
        ax.append(descartes.PolygonPatch(parts[x], fc='#650055',
                                         ec='black', alpha=0.5,
                                         aa=True,
                                         hatch='/'))
    f = plt.gca(title=t)
    for i in ax:
        f.add_patch(i)
    f.set_xlim(-1.7, 1.7)
    f.set_ylim(-1.1, 2.1)
    f.set_aspect('equal')
    plt.savefig('user_img.png', dpi=135)
    plt.close()
