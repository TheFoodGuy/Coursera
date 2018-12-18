package patmat

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

import patmat.Huffman._

@RunWith(classOf[JUnitRunner])
class HuffmanSuite extends FunSuite {
	trait TestTrees {
		val t1 = Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5)
		val t2 = Fork(Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5), Leaf('d',4), List('a','b','d'), 9)
	}


  test("weight of a larger tree") {
    new TestTrees {
      assert(weight(t1) == 5)
      println(weight(t1))
    }

  }




  test("chars of a larger tree") {
    new TestTrees {
      assert(chars(t2) === List('a','b','d'))
    }
  }


  test("string2chars(\"hello, world\")") {
    assert(string2Chars("hello, world") === List('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd'))
  }


  test("makeOrderedLeafList for some frequency table") {
    assert(makeOrderedLeafList(List(('t', 2), ('e', 1), ('x', 3))) === List(Leaf('e',1), Leaf('t',2), Leaf('x',3)))
  }


  test("combine of some leaf list") {
    val leaflist = List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 4))
    val leaflist1 = List(Leaf('e', 2), Leaf('t',3), Leaf('x', 4))
    assert(combine(leaflist) === List(Fork(Leaf('e',1),Leaf('t',2),List('e', 't'),3), Leaf('x',4)) )
    assert(combine(leaflist1) === List(Leaf('x', 4), Fork(Leaf('e', 2), Leaf('t', 3), List('e', 't'), 5)))
  }


  test("createCodeTree") {
    val res = createCodeTree("HGFEDCBBBAAAAAAAA".toList)
    assert(res === Fork(Leaf('A', 8), Fork(Fork(Leaf('B', 3), Fork(Leaf('C', 1), Leaf('D', 1), List('C', 'D'), 2), List('B', 'C', 'D'), 5), Fork(Fork(Leaf('E', 1), Leaf('F', 1), List('E', 'F'), 2), Fork(Leaf('G', 1), Leaf('H', 1), List('G', 'H'), 2), List('E', 'F', 'G', 'H'), 4), List('B', 'C', 'D', 'E', 'F', 'G', 'H'), 9), List('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'), 17))
  }

//  test("decode and encode a very short text should be identity") {
//    new TestTrees {
//      assert(decode(t1, encode(t1)("ab".toList)) === "ab".toList)
//    }
//  }

}
