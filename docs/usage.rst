=====
Usage
=====

To use Easy Vector in a project::

    from easy_vector import Vector

Or, abbreviate for easier usage::

    from easy_vector import Vector as V

Create vectors from components::

    >>> V(4, 9)  # create a 2D vector
    Vector[4.000,9.000]
    >>> V(2, 4, 9)  # create a 3D vector
    Vector[2.000,4.000,9.000]
    >>> V([4, 9])  # from a list
    Vector[4.000,9.000]
    >>> V((4, 9))  # or a tuple
    Vector[4.000,9.000]

Or from a length and direction::

    >>> V.polar(10, 45) # from length and angle, in degrees
    Vector[7.071,7.071]

Working with vector components::

    >>> vector = V(3, 5, 7)
    >>> vector[2]  # access componentswith subscript
    7
    >>> vector[1] = 8
    >>> print(vector)
    Vector[3.000,8.000,7.000]

Vector math::

    >>> V(4, 9) + V(6, 1)  # add
    Vector[10.000,10.000]
    >>> V(4, 9) - V(2, 4)  # subtract
    Vector[2.000,5.000]
    >>> V(3, 7) * 2.5  # multiply by scalar
    Vector[7.500,17.500]
    >>> V(3, 7) / 2.5  # divide by scalar
    Vector[1.200,2.800]
    >>> -V(15, 2)  # negate (flip 180)
    Vector[-15.000,-2.000]

Length (magnitude) and angle::

    >>> V(1, 1).length # length or magnitude
    1.4142135623730951
    >>> V(1, 1).angle # angle in degrees
    45.0

Normalizing a vector::

    >>> V(1, 1).normal # normalization (divide by length)
    Vector[0.707,0.707]

Comparing vectors::

    >>> V(6, 12) == V(6, 12)  # identity
    True
    >>> V(6, 12) == V(6.0, 12.0)  # int vs. float
    True
    >>> V(1,2) == V(1,3)
    False

Vectors are iterable::

    >>> for component in V(1.2, 5.6):
    ...     print(component)
    ... 
    1.2
    5.6

Operand type conversion::

    >>> V(5, 5) + [2, 2]
    Vector[7.000,7.000]
    >>> V(4, 6) + (1, 4)
    Vector[5.000,10.000]
    
