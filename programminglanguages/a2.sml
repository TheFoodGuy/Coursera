(* this is for the second assignment on PL Part A. I have to learn how to use datatype (or class
type in a way) over the usual specificiation of objects ex. obj : int*) 

(* this compares two strings and return true if they are the same string *)
fun same_string(s1 : string, s2: string) = 
    s1 = s2
(* #1 - must use pattern matching here. No null, hd, tl, isSome, valOf or any #
    This problem involves using first-name substitutions to come up with alternate names.
    ex. Fredrick William Smith -> Fred William Smith or Freddie William Smith *)
(* #a 
    return NONE if string not in list, or return SOME lst if identical
    val test1 = all_except_option ("string", ["string"]) = SOME []
*) 
fun all_except_option(str1 : string, str_list : string list) = 
    let 
        fun find_all(remaining_list : string list) = 
            case remaining_list of
                [] => []
                | x::xs' => if same_string(str1, x) then xs'
                         else x::find_all(xs')
        val check_list = find_all(str_list)
    in
        if check_list = str_list then NONE else SOME check_list
    end
(* val test1 = all_except_option("string", ["string"]) ; 
val test2 = all_except_option("string", ["one", "string", "billy"]);
val test3 = all_except_option("string", ["string", "one"]); *)
(* #b
    takes a string list list (aka the substitutions for the first name) and a string s
    and returns a string list. This result has all the strings that are in some list 
    in substitutions that also has s, but s itseld should not be the result. *)
fun get_substitutions1(name_list : (string list) list, name: string) =
    (* this checks if the name remotely matches the "name" to make sure it's a nickname *)
    (* no helper function for this case *)
    case name_list of
        [] => []
        | x::xs' => case all_except_option(name, x) of
                        NONE => get_substitutions1(xs', name)
                        | SOME y => y @ get_substitutions1(xs', name)
 (* #c - tail recursive style of get_substitutions
 *)
(* I want to recursively call and get the tail into acc *)
(* fun get_sub (name_list: string list list, name : string) : string list = 
    let 
        fun looping (acc: string list , str_list : string list list) = 
            case str_list of
                [] => acc
                | x::xs => 
                    case all_except_option(name, x) of
                        NONE => looping(acc, xs)
                        | SOME y => looping(y @ acc, xs)
    in
        looping([], name_list)
    end *)

(* you may assume that Num is always used with values 2, 3, ..., 10
    through it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades 
datatype rank = Jack | Queen | King | Ace | Num of int
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw

exception IllegalMove
(* #2 down here with the following helper codes up there *)
(* val test5 = card_color (Clubs, Num 2) = Black *)
fun card_color(suit, rank) =
    case suit of
         Spades => Black 
        |Clubs => Black
        |Diamonds => Red
        |Hearts => Red

(* val test6 = card_value (Clubs, Num 2) = 2 *)
fun card_value(suit, rank) = 
    case rank of
        Ace => 11
        |Jack => 10
        |Queen => 10
        |King => 10
        |Num x => x

(* remove only once from the list and keep on adding *)
fun remove_card(cs : card list, c : card, e ) = 
    let
        fun remove(cs) = 
            case cs of
                [] => [] (* this is the new list everything but that one copy*)
                | x::xs => 
                    if x = c then xs else x::remove(xs)
        val acc_list = remove(cs)
    in
        if acc_list = cs then raise e else acc_list
    end
(* val test7 = remove_card ([(Hearts, Ace)], (Hearts, Ace), IllegalMove) *)

fun all_same_color(cs) = 
    case cs of
        [] => true
        | x::[] => true
        | head::(neck::rest) => (head = neck andalso all_same_color(neck::rest))


(* val test8 = all_same_color [(Hearts, Ace), (Hearts, Ace), (Clubs, Ace)] = true *)
fun sum_cards(cs) = 
    let
        fun sum_up(cs, acc) = 
            case cs of 
                [] => acc
                | x::xs => sum_up(xs, card_value(x) + acc)
        val x = sum_up(cs, 0)
    in
        x
    end

(* val test9 = sum_cards [(Clubs, Num 2),(Clubs, Num 2)] = 4  *)
(* read the rules here before coding
    This computes the score as described *)
fun score(cs, value) = 
    let 
        val x = sum_cards(cs) - value
    in
        if x < 0 then abs(x) else abs(x)*3
    end

(* val test10 = score ([(Hearts, Num 2),(Clubs, Num 4)],10) = 4 *)
(* val test11 = officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6 *)
(* val test12 = officiate ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)], *)
                        (* [Draw,Draw,Draw,Draw,Draw], *)
                        (* 42) *)
             (* = 3 *)
(* val test13 = ((officiate([(Clubs,Jack),(Spades,Num(8))], *)
                         (* [Draw,Discard(Hearts,Jack)], *)
                         (* 42); *)
               (* false)  *)
              (* handle IllegalMove => true) *)
(*last question: 
    this runs a game and takes a card list, cs, a move list, ms, and 
    an int, goal. returns the score at the end of the game=*)
fun officiate(cs, ms, goal) = 

