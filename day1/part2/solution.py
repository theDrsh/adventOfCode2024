def solution(data: list) -> int:
  left_list = list()
  right_list = list()
  similarity_list = list()
  for line in data:
    split_line = line.split("   ")
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[1]))
  left_list.sort()
  right_list.sort()
  for item in left_list:
    occurances = 0
    for compare_item in right_list:
      if item < compare_item:
        break
      elif item == compare_item:
        occurances += 1
    similarity_list.append(item * occurances)
  return sum(similarity_list)

if __name__ == "__main__":
  solution_value = {"example_solution": None,
                    "puzzle_solution": None}
  with open("example.txt") as example_file:
    example_data = example_file.read()
    example_data = example_data.split("\n")[0:-1]
    solution_value["example_solution"] = solution(example_data)
  with open("data.txt") as data_file:
    data = data_file.read()
    data = data.split("\n")[0:-1]
    solution_value["puzzle_solution"] = solution(data)
  print(solution_value)
