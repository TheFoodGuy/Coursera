(* Coursera Programming Languages, Homework 3, Provided Code

Remember you might have to restart this class again when you get back just
saying man. *)
exception NoAnswer
datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** you can put all your code here ****)
(** return a string list that has only the strings in the arguments that start
	with an uppercase letter - at least one character**)
fun only_capitals string_list =
	List.filter (fn x => Char.isUpper(String.sub(x, 0))) string_list ; 

(** takes a string list and returns the longest string in the list, else return none**)
fun longest_string1 string_list = 
	List.foldl (fn (x, acc) => if String.size x > String.size acc then x else acc ) "" string_list ;
(* val test2 = longest_string1 ["A","bc","C"] = "bc" *)
fun longest_string2 string_list = 
	List.foldl (fn (x, acc) => if String.size x >= String.size acc then x else acc ) "" string_list ; 

(*longest_string3 = 1 and longest_string4 = 2*)
fun longest_string_helper f str_list str = 
	List.foldl( f(str_list, str) )	