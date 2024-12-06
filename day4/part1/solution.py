def solution(data: list) -> int:
  occurance = 0
  for row_index, line in enumerate(data):
    for col_index, letter in enumerate(line):
      if letter == 'X':
        # Look Right
        clipped_index = col_index + 4 if (len(line) - col_index) > 4 else len(line)
        if "XMAS" in line[col_index:clipped_index]:
          occurance += 1
          # print("({},{}) right:{}".format(col_index, row_index, occurance))

        # Look Left
        clipped_index = col_index - 3 if col_index - 3 > 0 else 0
        if "SAMX" in line[clipped_index:col_index + 1]:
          occurance += 1
          # print("({},{}) left:{}".format(col_index, row_index, occurance))

        # Look up + to diagonals up
        if row_index >= 3:
          if data[row_index - 1][col_index] == 'M' and \
             data[row_index - 2][col_index] == 'A' and \
             data[row_index - 3][col_index] == 'S':
              occurance += 1
              # print("({},{}) up:{}".format(col_index, row_index, occurance))
          if col_index >= 3:
            if data[row_index - 1][col_index - 1] == 'M' and \
               data[row_index - 2][col_index - 2] == 'A' and \
               data[row_index - 3][col_index - 3] == 'S':
                occurance += 1
                # print("({},{}) up/left:{}".format(col_index, row_index, occurance))
          if (len(line) - col_index) > 3:
            if data[row_index - 1][col_index + 1] == 'M' and \
               data[row_index - 2][col_index + 2] == 'A' and \
               data[row_index - 3][col_index + 3] == 'S':
                occurance += 1
                # print("({},{}) up/right:{}".format(col_index, row_index, occurance))

        # Look Down Diagonals down
        if (len(data) - row_index) > 3:
          if data[row_index + 1][col_index] == 'M' and \
             data[row_index + 2][col_index] == 'A' and \
             data[row_index + 3][col_index] == 'S':
              occurance += 1
              # print("({},{}) down:{}".format(col_index, row_index, occurance))
          if col_index >= 3:
            if data[row_index + 1][col_index - 1] == 'M' and \
               data[row_index + 2][col_index - 2] == 'A' and \
               data[row_index + 3][col_index - 3] == 'S':
                occurance += 1
                # print("({},{}) down/left:{}".format(col_index, row_index, occurance))
          if (len(line) - col_index) > 3:
            if data[row_index + 1][col_index + 1] == 'M' and \
               data[row_index + 2][col_index + 2] == 'A' and \
               data[row_index + 3][col_index + 3] == 'S':
                occurance += 1
                # print("({},{}) down/right:{}".format(col_index, row_index, occurance))
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
