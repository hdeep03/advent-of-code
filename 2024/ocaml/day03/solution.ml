open Stdio

let text = In_channel.read_all("input.in")
let regex = Str.regexp {|mul(\([0-9][0-9]?[0-9]?\),\([0-9][0-9]?[0-9]?\))\|do()\|don't()|}

let rec scan start acc flag pt= 
  try
  let _ = Str.search_forward regex text start in
  match Str.matched_string text with 
  "do()" -> scan (Str.match_end()) acc 1 pt
  | "don't()" -> scan (Str.match_end()) acc (2-pt) pt
  | _ ->
        let left = Str.matched_group 1 text |> int_of_string in
        let right = Str.matched_group 2 text |> int_of_string in
        let prod = (left * right) * flag + acc in
        scan (Str.match_end()) prod flag pt
  with Not_found -> 
    acc

let () = printf("Part 1: %d\nPart 2: %d\n") (scan 0 0 1 1) (scan 0 0 1 2)
