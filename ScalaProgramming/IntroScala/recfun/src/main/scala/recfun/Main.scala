package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if (c == 0 | c == r) 1
      else pascal(c-1, r-1) + pascal(c, r-1)
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def recBalance(chars: List[Char], counter: Int, balanced: Boolean): Boolean = {
        if (chars.isEmpty) !balanced && counter == 0
        else
          chars.head match {
            case '(' => recBalance(chars.tail, counter + 1, true)
            case ')' => recBalance(chars.tail, counter - 1, false)
            case _ => recBalance(chars.tail, counter, balanced)
          }
      }
      recBalance(chars, 0, false)
    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      money match {
        case _ if money < 0 => 0
        case _ if money == 0 => 1
        case _ if coins.isEmpty => 0
        case _ => countChange(money - coins.head, coins) + countChange(money, coins.tail)
      }
    }
  }
