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

## Bonus (hard problem)

### Project Euler #148
* https://projecteuler.net/problem=148

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

 	 	 	 	 	 	 1
 	 	 	 	 	 1	 	 1
 	 	 	 	 1	 	 2	 	 1
 	 	 	 1	 	 3	 	 3	 	 1
 	 	 1	 	 4	 	 6	 	 4	 	 1
 	 1	 	 5	 	10	 	10	 	 5	 	 1
    1	 	 6	 	15	 	20	 	15	 	 6	 	 1
  
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.

For our class one million will be enough.
