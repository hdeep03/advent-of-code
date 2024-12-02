open Base
open Stdio

let string_to_char_list s = List.init (String.length s) ~f:(String.get s)

let digits char_list =
  char_list
  |> List.map ~f:(fun x -> String.make 1 x)
  |> List.filter_map ~f:Int.of_string_opt

let get_first_of_list list =
  (list |> fun x -> List.take x 1) |> fun x ->
  match x with [] -> 0 | a :: _ -> a

let get_first_digit char_list = char_list |> digits |> get_first_of_list

let soln () =
  In_channel.fold_lines In_channel.stdin
    ~f:(fun acc line ->
      let char_list = string_to_char_list line in
      let first = get_first_digit char_list in
      let last = char_list |> List.rev |> get_first_digit in
      acc + (first * 10) + last)
    ~init:0

let () = soln () |> Int.to_string |> print_endline
