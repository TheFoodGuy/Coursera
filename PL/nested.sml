fun nondecreasing xs = 
    case xs of 
        [] => true
        | x::[] => true 
        | head::(neck::rest) => head <= neck andalso nondecreasing (neck::rest)
