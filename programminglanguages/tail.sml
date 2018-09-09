(* having fun with tail recurison here*)
fun sum' (acc:int) (l:int list):int = 
    case l of 
        [] => acc
        | x::xs => sum' (acc+x) xs

fun get_substitutions1(name_list : (string list) list, name: string) =
    (* this checks if the name remotely matches the "name" to make sure it's a nickname *)
    (* no helper function for this case *)
    case name_list of
        [] => []
        | x::xs' => case all_except_option(name, x) of
                        NONE => get_substitutions1(xs', name)
                        | SOME y => y @ get_substitutions1(xs', name)

(* I want to recursively call and get the tail into acc *)
fun get_sub (name_list: string list list, name : string) : string list = 
    let 
        fun looping (acc: string list) (str_list : string list list) = 
            case str_list of
                [] => acc
                | x::xs => 
                    case all_except_option(name, x) of