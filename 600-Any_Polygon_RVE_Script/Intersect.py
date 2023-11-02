# coding=utf-8
# code from ：
# https://segmentfault.com/a/1190000004457595

# 点
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


# 向量
class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


ZERO = 1e-9


def negative(vector):
    """取反"""
    return Vector(vector.end, vector.start)


def vector_product(vectorA, vectorB):
    '''计算 x_1 * y_2 - x_2 * y_1'''
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y


def is_intersected(A, B, C, D):
    '''A, B, C, D 为 Point 类型'''
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)

    return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
        and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)


def detect_Polygon_Intersect(Polygon1, Polygon2):
    """Polygon ==> [(x1,y1),(x2,y2)...]"""

    for i in range(0, len(Polygon1)):
        p1 = Polygon1(i % (len(Polygon1)))
        p2 = Polygon1((i + 1) % (len(Polygon1)))
        A = Point(p1[0], p1[1])
        B = Point(p2[0], p2[1])
        for j in range(0,len(Polygon2)):
            p3 = Polygon2(i % (len(Polygon2)))
            p4 = Polygon2((i + 1) % (len(Polygon2)))
            C = Point(p3[0], p3[1])
            D = Point(p4[0], p4[1])

            if is_intersected(A, B, C, D):
                return 1
    return 0
