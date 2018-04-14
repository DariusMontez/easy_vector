===========
Quick-start
===========

Some common things to do with vectors::

    >>> from easy_vector import Vector as V
    >>> vec = V(3, 4)
    >>> print(vec)
    Vector[3.000,4.000]
    >>> vec.length
    5.0
    >>> vec[1] = 3
    >>> print(vec)
    Vector[3.000,3.000]
    >>> vec.normal
    Vector[0.707,0.707]
    >>> vec.normal.angle
    45.0
