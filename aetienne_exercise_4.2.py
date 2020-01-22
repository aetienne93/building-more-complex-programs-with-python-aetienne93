#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:57:48 2020
exercise 4.2 creating flowers 
@author: aetienne
"""

from __future__ import print_function, division

import math
import turtle
"""Import necessary packages"""

"""Define a square with x number of sides and given length, t for turtle."""
"""Will return turtle to start.  """
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
      

"""Will draw ls line segments.

    t is turtle
    ls is # line segments
    length is the length of each segment
    ang is the anlgle in degrees between segments
    """
def polyline(t, ls, length, ang):
    for i in range(ls):
        t.fd(length)
        t.lt(ang)


def polygon(t, ls, length):
    """Draws a polygon with ls sides.

    t: Turtle
    ls: number of sides (line segments)
    length: length of each side.
    """
    ang = 360.0/ls
    polyline(t, ls, length, ang)


def arc(t, r, ang):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle linked by arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(ang) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(ang) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """This draws the circle of a specified radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


def petal(t, r, ang):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    ang: angle that links each arc in degrees 
    """
    for i in range(2):
        arc(t, r, ang)
        t.lt(180-ang)


def flower(t, ls, r, ang):
    """Draws a flower with ls petals.

    t: Turtle
    ls: number of line segments- petals
    r: radius of the arcs
    ang: angle that links each arc in degrees
    """
    for i in range(ls):
        petal(t, r, ang)
        t.lt(360.0/ls)


def move(t, length):
    """Moves turtle forward a specified length unit
    will not leave trail behind
    Pen ends up in down direction.
    """
    t.pu()
    t.fd(length)
    t.pd()


keith = turtle.Turtle()

"""where the magic happens- draws 3 seperate flowers as specified in ch. 4)"""
move(keith, -100)
flower(keith, 7, 60.0, 60.0)

move(keith, 100)
flower(keith, 10, 40.0, 80.0)

move(keith, 100)
flower(keith, 20, 140.0, 20.0)

keith.hideturtle()
turtle.mainloop()

