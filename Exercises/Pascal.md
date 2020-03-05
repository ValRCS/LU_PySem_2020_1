# Pascal's Triangle

* Test/Submit here: https://www.codewars.com/kata/56e7d40129035aed6c000632

* [Wiki on Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)

![Pascal's Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

In the drawing below we have a part of the Pascal's triangle, lines are numbered from zero (top).

We want to calculate the sum of the squares of the binomial coefficients on a given line with a function called easyline (or easyLine or easy-line).

Can you write a program which calculate easyline(n) where n is the line number?

The function will take n (with: n>= 0) as parameter and will return the sum of the squares of the binomial coefficients on line n.

## Examples:

easyline(0) => 1
easyline(1) => 2
easyline(4) => 70
easyline(50) => 100891344545564193334812497256


## Submission For Participation until next Friday's Lecture

Write a class Pascal which is initialized with number of lines(count starts at 0)

This means writing a constructor and holding all the lines in memory(data structure up to you).

Class should have the method easyline(linenum) (same thing as above)

Class should also have a prettyprint(numlines) which displays Pascal's triangle up to and including numlines in some sort of graphical format, ASCII art is okay, but graphics would be nicer
