def product(f: Int => Int)(a:Int, b:Int): Int =
  if (a > b) 1
  else f(a) * product(f)(a + 1, b)

product(x => x * x)(3, 4)

def factorial(n:Int) =
  product( x => x)(1, n)

factorial(5)

//def mapReduce(f: Int => Int, combine: (Int, Int), zero: Int)(a:Int, b:Int):Int =
//  if (a > b) zero
//  else combine(f(a), mapReduce(f, combine, zero)(a+1, b))

// Lecture 2.3 - Example
//Lecture 2.5 - Rationals
object rationals {
  val x = new Rational(1,2)
  x.numer
  x.denom

  val y = new Rational(2, 3)
  x.add(y)
  x.numer
  y.denom
  println(x.denom)
}
class Rational(x: Int, y: Int) {
  def numer = x
  def denom = y

  def add(that: Rational) =
    new Rational(
      numer * that.denom + that.numer * denom,
      denom * that.denom)
}