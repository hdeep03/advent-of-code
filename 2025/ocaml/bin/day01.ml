open Core

let inputPath = "inputs/day01.txt"

module Operation = struct 
  let parse input = 
    let input = input |> String.strip |> String.uppercase in
    let factor = match String.slice input 0 1 with
      | "L" -> -1
      | "R" -> 1
      | _ -> raise (Failure "Failed to parse first character of Operation")
      in
    let rotation = String.slice input 1 0 |> Int.of_string_opt |> Option.value_exn ~message:"Failed to parse numerical part of Operation" in
    rotation * factor
end

module StateA = struct
  type t = {
    lockPosition: int;
    zeroCount: int
  }

  let init () = {lockPosition=50; zeroCount=0}

  let update state operation =
    let (+%) dividend divisor = ((dividend % divisor) + divisor) % divisor in
    let newLockPosition = (state.lockPosition + operation) +% 100 in
    let newZeroCount = match newLockPosition with
    | 0 -> state.zeroCount + 1
    | _ -> state.zeroCount 
    in
    {lockPosition=newLockPosition;zeroCount=newZeroCount}
end

module StateB = struct
  type t = {
    lockPosition: int;
    zeroCount: int
  }

  let init () = {lockPosition=50; zeroCount=0}

  let update state operation =
    let (+%) dividend divisor = ((dividend % divisor) + divisor) % divisor in
    let increment = if operation > 0 then (state.lockPosition + operation) / 100 else ((100 - state.lockPosition)%100 + abs(operation)) / 100 in
    let newLockPosition = (state.lockPosition + operation) +% 100 in
    let newZeroCount = state.zeroCount + increment in
    {lockPosition=newLockPosition;zeroCount=newZeroCount}
end

let partA input =
  let operations = List.map input ~f:Operation.parse in
  let state = List.fold operations ~init:(StateA.init ()) ~f:StateA.update in
  Int.to_string state.zeroCount

let partB input =
  let operations = List.map input ~f:Operation.parse in
  let state = List.fold operations ~init:(StateB.init ()) ~f:StateB.update in
  Int.to_string state.zeroCount

let () = 
  let input = In_channel.read_lines inputPath in
  let resA = partA input in
  let resB = partB input in
  print_endline ("Part A: " ^ resA);
  print_endline ("Part B: " ^ resB)