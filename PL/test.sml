fun sum_list xs = 
    case xs of 
        [] => 0
        | x::xs' => x + sum_list xs'

