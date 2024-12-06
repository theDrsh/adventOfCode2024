def solution(data: list) -> int:
  occurance = 0
  for row_index, line in enumerate(data):
    for col_index, letter in enumerate(line):
      if letter == 'A':
        if col_index >= 1 and (len(line) - col_index) > 1:
          if row_index >= 1 and (len(data) - row_index) > 1:
            if data[row_index - 1][col_index - 1] == "M" and \
              data[row_index - 1][col_index + 1] == "S" and \
              data[row_index + 1][col_index - 1] == "M" and \
              data[row_index + 1][col_index + 1] == "S":
              occurance += 1
            if data[row_index - 1][col_index - 1] == "M" and \
              data[row_index - 1][col_index + 1] == "M" and \
              data[row_index + 1][col_index - 1] == "S" and \
              data[row_index + 1][col_index + 1] == "S":
              occurance += 1
            if data[row_index - 1][col_index - 1] == "S" and \
              data[row_index - 1][col_index + 1] == "M" and \
              data[row_index + 1][col_index - 1] == "S" and \
              data[row_index + 1][col_index + 1] == "M":
              occurance += 1
            if data[row_index - 1][col_index - 1] == "S" and \
              data[row_index - 1][col_index + 1] == "S" and \
              data[row_index + 1][col_index - 1] == "M" and \
              data[row_index + 1][col_index + 1] == "M":
              occurance += 1
  return occurance



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
