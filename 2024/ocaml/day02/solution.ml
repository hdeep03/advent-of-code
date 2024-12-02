open Base
open Stdio


let text = In_channel.read_all("input.in")
let lines = String.split_lines text

let get_trailing lst = match lst with | [] -> [] | _::tl -> tl

let take_start lst = List.rev lst |> get_trailing |> List.rev

let is_seq_valid line = 
  let left_side = take_start line in
  let right_side = get_trailing line in
  List.map2 left_side right_side ~f:(fun a b -> b-a > 0 && b - a < 4) 
  |> (fun x -> match x with | Base.List.Or_unequal_lengths.Ok x -> x | Base.List.Or_unequal_lengths.Unequal_lengths -> failwith "Unequal lengths") 
  |> List.fold ~init:true ~f:(&&)

let records = List.map ~f:(fun x -> String.split ~on:' ' x |> List.map ~f:Int.of_string) lines
let pt1 = records |> List.filter ~f:(fun lst -> is_seq_valid lst || is_seq_valid (List.rev lst)) |> List.length

let () = printf "Part 1: %d\n" pt1

let generate_combos lst = 
  let rng = List.range 1 (List.length lst) in
    List.map rng ~f:(fun x -> List.take lst (x-1) @ List.drop lst x)

let combo_valid lst = let combos = generate_combos lst in
  List.map ~f:(fun x -> is_seq_valid x || is_seq_valid (List.rev x)) combos
  |> List.fold ~init:false ~f:(||)

let seq_fuzzy_valid lst = combo_valid lst || is_seq_valid lst || is_seq_valid (List.rev lst) || combo_valid (List.rev lst)

let () = let ct = List.filter records ~f:seq_fuzzy_valid in printf "Part 2: %d\n" (List.length ct)
