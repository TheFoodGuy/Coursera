import scala.collection.immutable.Stream.cons

var s = List('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd')


val list = List(1, 2, 4, 2, 4, 7, 3, 2, 4)
// Using the provided count method this would yield the occurrences of each value in the list:
list.map(x => list.count(_ == x))

"haskell scala".groupBy(identity).mapValues(_.size).toList

val pairs = s.groupBy(identity).mapValues(_.size).toList

