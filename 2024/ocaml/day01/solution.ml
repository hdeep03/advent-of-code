open Base
open Stdio

let text = In_channel.read_all "input.in"
let lines = String.split_lines text
let head lst = match lst with [] -> "" | x :: _ -> x
let tail list : string = match List.last list with None -> "" | Some x -> x

let left =
  List.map lines ~f:(fun x -> String.split ~on:' ' x |> head |> Int.of_string)

let right =
  List.map lines ~f:(fun x -> String.split ~on:' ' x |> tail |> Int.of_string)

let l_sorted = List.sort left ~compare:Int.compare
let r_sorted = List.sort right ~compare:Int.compare
let diff = List.map2_exn l_sorted r_sorted ~f:(fun a b -> abs (b - a))
let pt1 = List.fold diff ~init:0 ~f:( + )
let () = printf "%d\n" pt1

(* type t = (int, int, Int.comparator_witness) Map.t *)
let empty = Map.empty (module Int)
let inc m k = Map.update m k ~f:(function None -> 1 | Some x -> x + 1)
let right_freq = List.fold right ~init:empty ~f:inc

let pt2 =
  List.fold left ~init:0 ~f:(fun acc x ->
      match Map.find right_freq x with None -> acc | Some ct -> acc + (x * ct))

let () = printf "%d\n" pt2
