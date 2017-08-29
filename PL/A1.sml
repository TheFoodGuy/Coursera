(* this file is a compiled list of all the problems in the first assignment *)

(*#1
   takes two dates and evaluates to true if the first one is less than the second one*)
fun is_older( d1 : (int * int * int), d2 : (int * int * int)) = 
    if #1 d1 < #1 d2
    then true 
    else if #2 d1 < #2 d2 andalso #1 d1 = #1 d2
    then true 
    else if #3 d1 < #3 d2 andalso #2 d1 = #2 d2 andalso #1 d1 = #1 d2
    then true 
    else false
    
(*#2
   Going by american date standard m/d/y *)
fun number_in_month(d1 : (int * int * int) list, month) = 
    if null d1
    then 0
    else if #1 (hd d1) = month
    then 1 + number_in_month(tl d1, month)
    else number_in_month(tl d1, month)
(* #3
    This uses #2 and recursively call the tail of months for the results
    of all the dates that match the months.*)
fun number_in_months(d1: (int * int * int) list, months: int list) =
    if null d1
    then 0 
    else if null months
    then 0
    else (*somehow recursively call month with each function call *)
        number_in_month(d1, hd months) + number_in_months(d1, tl months)
(* #4
    This returns a list that has all of the dates that match a single month *)
fun dates_in_month(d1: (int * int * int) list, month : int) = 
    if null d1
    then []
    else if month=0
    then []
    else
        if #1 (hd d1) = month
        then (hd d1)::dates_in_month(tl d1, month)
        else dates_in_month(tl d1, month)

(* #5
    takes two lists of dates and months and returns a list 
    holding the dates from the argument list of dates that are in any of the months*)
fun dates_in_months(d1 : (int * int * int) list, m1 : int list) = 
    if null d1 orelse null m1
    then []
    else 
        dates_in_month(d1, hd m1)::dates_in_months(d1, tl m1)

(* #6
    takes a list of strings and an int, n, and returns the nth element of the list *)
fun get_nth(s1 : string list, nth : int) =
    if nth = 1
    then hd s1
    else if null s1
    then ""
    (* continously calling tl on string list and subtracting nth until 0*)
    else get_nth(tl s1, nth - 1)

(* #7 
    takes a date and retuns a string of the form January 20, 2013 
    basically convert dates to its full date name *)
fun date_to_string(date : (int * int * int)) =
    let
        val months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul."
                      ,"Aug.", "Sept.", "Oct.", "Nov.", "Dec"] ;
    in
        let val x = get_nth(months, #1 date) in print(x ^ " " ^ (Int.toString(#2 date)) ^ ", " ^
        (Int.toString(#3 date)) ^ ("\n")) 
        end
    end

(* #8 
    takes a pos. int called sum and an int list containing all pos. numbers and return an int.
    returns an int n such that the first nelements of the list add to less than sum, but 
    the first n + 1 elemnts of the list add to sum or more.
    *) 
    (* no idea what it's really asking so im skipping it *)

(* #9
    takes a day of year from 1 - 365 and returns what month that day is in *) 
fun what_month(day_int : int) = 
    let
        val months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov",
        "Dec" ] ;
        (* days of each month *) 
        val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] ;
        fun find_month(days: int, d1 : int list , m1 : string list) =
            let 
                val cur_day = hd d1
                val cur_mon = hd m1
            in
                if days <= cur_day
                then cur_mon
                else find_month(days-cur_day, tl d1, tl m1)
           end 
    in
        (* I want to keep on calling days to subtract the number until it is greater giving me the
        location of the day in what month *)
        let val month = find_month(day_int, days, months) 
        in print(month ^ "\n") 
        end
    end

(* #10
    takes two days of the year day1 and day2 and returns an int list of ms. 
    basically, if day1 = Feb and day2 = April, then the list should be 
    2, 3, 4. Can't make it go reverse for some reasons *)
fun month_range(day1 : int, day2 : int) = 
    let
        val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] ; 
        val months =[1,2,3,4,5,6,7,8,9,10,11,12] ;
        fun find_month(days: int, d1 : int list, m1 : int list) =
            let 
                val cur_day = hd d1
                val cur_mon = hd m1
            in 
                if days <= cur_day
                then cur_mon
                else find_month(days-cur_day, tl d1, tl m1)
            end
        fun countdown(start: int, stop: int) = 
            if start <= stop
            then stop::countdown(start, stop-1)
            (* once start == stop *)
            else []
    in
        if day1 > day2
        then []
        else 
            (* find the months of day1 and day2 in comparison to the month list *)
            let 
                val month1 = find_month(day1, days, months) 
                val month2 = find_month(day2, days, months)
            in
                countdown(month1, month2) 
            end
    end
(*
(* #11 
    takes a list of dates and evaluates an (int * int * int) option of the oldest date *)
fun count(ya: int list) = 
    if null ya
    then 0 
    else 1 + count(tl ya)
fun oldest(dates : (int * int * int) list) = 
    if null dates
    then NONE
    else 
        (* finding the oldest date here *)
        let
            (* dates are #1 - month, #2 - day, #3 - year *)
            fun is_oldest(d1: int * int * int, d2: int * int * int) =
                let
                    val day1 = ((#1 d1) * 12) + ((#2) * 365) + (#3 d1)
                    val day2 = ((#1 d2) * 12) + ((#2) * 365) + (#3 d1)
                in
                    (* this is testing if the second day is bigger than the first day or the target
                    *)
                    if day1 < day2
                    then true
                    else false 
                end
            fun find_oldest(target: int, dates: (int * int * int) list) =
                let
                    val current = target 
                    val next = hd dates
                    val result = is_oldest(current, next)
                in
                    if result = true
                    then current = result
                    else current = current ;
                    
                    if count((tl dates)) > 0
                    then find_oldest(current, tl dates)
                    else current
                      
               end
        in 
            print(Int.toString(find_oldest(hd dates, tl dates)) ^ "\n")
        end *)
