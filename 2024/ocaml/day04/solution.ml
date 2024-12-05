open Base
open Stdio

let match_str = "XMAS"

let text = In_channel.read_all "input.in"
let lines = String.split ~on:'\n' text
let get_char_at row col = 
  try
    let line = List.nth_exn lines row in String.get line col
  with _ -> ' '


let rec check_match row col dr dc idx =
  if idx = 0 then (match get_char_at row col with 'S' -> true |  _ -> false)
  else if idx > 3 then failwith "invalid idx"
  else
    let res = (get_char_at row col) in
    if Char.equal res (String.get match_str (3-idx)) then (check_match (row + dr) (col + dc) dr dc (idx - 1))
    else false

let count_matches_at row col =
  let dirs = [(0, 1); (1, 0); (1, 1); (1, -1); (0, -1); (-1, 0); (-1, -1); (-1, 1)] in
  List.map dirs ~f:(fun (dr, dc) -> check_match row col dr dc 3) 
  |> List.filter ~f:(fun x -> x)
  |> List.length

let pt1 =
  let rows = List.length lines in
  let cols = String.length (List.hd_exn lines) in
  let rec loop row col acc =
    if row = rows then acc
    else if col = cols then loop (row + 1) 0 acc
    else loop row (col + 1) (acc + (count_matches_at row col))
  in loop 0 0 0


let get_crosses row col =
  let offsets = [(-1, -1, 1, 1); (-1, 1, 1, -1); (1, -1, -1, 1); (1, 1, -1, -1)] in
  List.map offsets ~f:(fun (dr, dc, drr, dcc) -> check_match (row + dr) (col + dc) drr dcc 2)
  |> List.filter ~f:(fun x -> x)
  |> fun x -> match List.length x = 2 with true -> 1 | _ -> 0

let pt2 =
  let rows = List.length lines in
  let cols = String.length (List.hd_exn lines) in
  let rec loop row col acc =
    if row = rows - 1 then acc
    else if col = cols - 1 then loop (row + 1) 0 acc
    else loop row (col + 1) (acc + (get_crosses row col))
  in loop 1 1 0

let () = printf "Part 1: %d\n" pt1
let () = printf "Part 2: %d\n" pt2