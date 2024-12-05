def solution(data: list) -> int:
  safe_reports = list()
  for report in data:
    levels = list(map(int, report.split(" ")))
    safe_reports.append(is_safe(levels))
  return sum(safe_reports)

def is_safe(levels: list) -> bool:
  report_is_safe = False
  levels_difference = list()
  sorted_levels_increasing = list(levels)
  sorted_levels_increasing.sort()
  sorted_levels_decreasing = list(levels)
  sorted_levels_decreasing.sort(reverse=True)
  if (sorted_levels_increasing == levels) or (sorted_levels_decreasing == levels):
    for level_index in range(len(levels) - 1):
      levels_difference.append(abs(levels[level_index] - levels[level_index + 1]))
    if (max(levels_difference) <= 3) and (min(levels_difference) > 0):
      report_is_safe = True
  return report_is_safe

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
