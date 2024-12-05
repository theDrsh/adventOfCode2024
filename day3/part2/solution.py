import re
def solution(data: list) -> int:
  multiplications = list()
  regex = "do\\(\\)|don't\\(\\)|mul\\(-?\d+,-?\d+\\)"
  do_mult = True
  for instruction in data:
    results = re.findall(regex, instruction)
    for match in results:
      if match == "do()":
        do_mult = True
      elif match == "don't()":
        do_mult = False
      else:
        if do_mult:
          left, right = list(map(int, match.split("mul(")[1].split(")")[0].split(",")))
          multiplications.append(left * right)
  return sum(multiplications)


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
