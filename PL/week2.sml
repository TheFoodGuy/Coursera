(* this is a random example from what I gathered in the lecture slides *)
fun pow(x : int, y : int) = 
    if y = 0
    then 1 
    else x * pow(x, y-1)

val a = [(1,2,3), (4,5,6)];
