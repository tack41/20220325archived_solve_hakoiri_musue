#coding:utf-8
def print_problem(problem):
  for row in range(5):
    print(
      komas[problem[row][0][0]][problem[row][0][1]] + \
      komas[problem[row][1][0]][problem[row][1][1]] + \
      komas[problem[row][2][0]][problem[row][2][1]] + \
      komas[problem[row][3][0]][problem[row][3][1]] 
    )
def dump_problem(problem):
  retval = ""
  for row in range(5):
    retval = retval + list(problem[row][0][0])[0] + list(problem[row][1][0])[0]+ list(problem[row][2][0])[0]+ list(problem[row][3][0])[0]
  return retval

def movable_koma(problem):
  retval = {}

  for row in range(5):
    for col in range(4):
      #空きスペースを見つけたらその周囲のコマに対してチェック
      if problem[row][col][0] == "口":

        # movable from left to right 
        if col > 0 and problem[row][col-1][0] != "口":
         #コマが複数のセルで構成されている場合、その全てのセルが移動可能かチェック
          movable = True
          for in_row in range(5):
             for in_col in range(4):
               if (in_row != row or in_col != col-1) and problem[row][col-1][0] == problem[in_row][in_col][0]:
                if problem[in_row][in_col+1][0] != "口" and problem[in_row][in_col+1][0] != problem[in_row][in_col][0] :
                  movable = False
          if movable: 
            retval[problem[row][col-1][0]] = "to right"

        # movable from right to left 
        if col < 3 and problem[row][col+1][0] != "口":
         #コマが複数のセルで構成されている場合、その全てのセルが移動可能かチェック
          movable = True
          for in_row in range(5):
             for in_col in range(4):
               if (in_row != row or in_col != col+1) and problem[row][col+1][0] == problem[in_row][in_col][0]:
                if problem[in_row][in_col-1][0] != "口" and problem[in_row][in_col-1][0] != problem[in_row][in_col][0] :
                  movable = False
          if movable: 
            retval[problem[row][col+1][0]] = "to left"

        # movable from up to down 
        if row > 0 and problem[row-1][col][0] != "口":
         #コマが複数のセルで構成されている場合、その全てのセルが移動可能かチェック
          movable = True
          for in_row in range(5):
             for in_col in range(4):
               if (in_row != row-1 or in_col != col) and problem[row-1][col][0] == problem[in_row][in_col][0]:
                if problem[in_row+1][in_col][0] != "口" and problem[in_row+1][in_col][0] != problem[in_row][in_col][0] :
                  movable = False
          if movable: 
            retval[problem[row-1][col][0]] = "to down"

        # movable from down to up 
        if row < 4 and problem[row+1][col][0] != "口":
         #コマが複数のセルで構成されている場合、その全てのセルが移動可能かチェック
          movable = True
          for in_row in range(5):
             for in_col in range(4):
               if (in_row != row+1 or in_col != col) and problem[row+1][col][0] == problem[in_row][in_col][0]:
                if problem[in_row-1][in_col][0] != "口" and problem[in_row-1][in_col][0] != problem[in_row][in_col][0] :
                  movable = False
          if movable: 
            retval[problem[row+1][col][0]] = "to up"
  return retval

def move_koma(*, problem, koma_name, direction):
  import copy
  problem_moved = copy.deepcopy(problem)

  if direction == "to right":
    for row in range(5):
      for col in range(4):
        if problem_moved[row][3-col][0] == koma_name:
          problem_moved[row][3-col+1][0] = problem_moved[row][3-col][0]
          problem_moved[row][3-col+1][1] = problem_moved[row][3-col][1]
          problem_moved[row][3-col][0] = "口"
          problem_moved[row][3-col][1] = 1

  if direction == "to left":
    for row in range(5):
      for col in range(4):
        if problem_moved[row][col][0] == koma_name:
          problem_moved[row][col-1][0] = problem_moved[row][col][0]
          problem_moved[row][col-1][1] = problem_moved[row][col][1]
          problem_moved[row][col][0] = "口"
          problem_moved[row][col][1] = 1

  if direction == "to up":
    for col in range(4):
      for row in range(5):
        if problem_moved[row][col][0] == koma_name:
          problem_moved[row-1][col][0] = problem_moved[row][col][0]
          problem_moved[row-1][col][1] = problem_moved[row][col][1]
          problem_moved[row][col][0] = "口"
          problem_moved[row][col][1] = 1

  if direction == "to down":
    for col in range(4):
      for row in range(5):
        if problem_moved[4-row][col][0] == koma_name:
          problem_moved[4-row+1][col][0] = problem_moved[4-row][col][0]
          problem_moved[4-row+1][col][1] = problem_moved[4-row][col][1]
          problem_moved[4-row][col][0] = "口"
          problem_moved[4-row][col][1] = 1

  return problem_moved

def solved(*, problem):
  if problem[2][0][0] == "娘" or problem[2][1][0]=="娘" or problem[2][2][0]=="娘" or problem[2][3][0] == "娘" :
#  if problem[4][1][0] == "娘": 
    return True
  return False

koma_mother = {1:"母", 2:"母"}
koma_father = {1:"父", 2:"父"}
koma_daughter = {1:"娘", 2:"娘", 3:"娘", 4:"娘"}
koma_zyotyu = {1:"女", 2:"中"}
koma_banto = {1:"番", 2:"頭"}
koma_tedai = {1:"手"}
koma_detti = {1:"丁"}
koma_space = {1:"口"}
komas = {
  "母":koma_mother, 
  "父":koma_father, 
  "娘":koma_daughter, 
  "女中1":koma_zyotyu, 
  "女中2":koma_zyotyu, 
  "番頭":koma_banto, 
  "手代1":koma_tedai, 
  "手代2":koma_tedai, 
  "丁稚1":koma_detti, 
  "丁稚2":koma_detti, 
  "口":koma_space
}
problem_global = [
            [["母",1], ["娘",1], ["娘",2], ["父",1]],
            [["母",2], ["娘",3], ["娘",4], ["父",2]],
            [["女中1",1], ["番頭",1], ["番頭",2], ["女中2",1]],
            [["女中1",2], ["手代1",1], ["手代2",1], ["女中2",2]],
            [["丁稚1",1], ["口",1], ["口",1], ["丁稚2",1]]
          ]

dump_history_global = []
#print_problem(problem)

#print(dump_problem(problem))

def solve(*, problem, move_history):
  movable_dict = movable_koma(problem)
#  print(movable_dict)

  for koma_name,direction in movable_dict.items():
    problem_moved = move_koma(problem=problem, koma_name=koma_name, direction=direction)
    # 既に過去に展開されている場合は中止します
    already_extended = False
    for dump in dump_history_global:
      if dump_problem(problem_moved) == dump:
        already_extended = True
        break
    if already_extended:
      continue
    else:
      dump_history_global.append(dump_problem(problem_moved))
      move_history.append(str(koma_name) + "を" + str(direction) + "に動かします")
      problem_moved = move_koma(problem=problem, koma_name=koma_name, direction=direction)
#      print(str(koma_name) + "を" + str(direction) + "に動かします")
#      print_problem(problem_moved)
#      print()
      if solved(problem=problem_moved):
        print("解けました。以下の通り移動してください")
        for hist in move_history:
          print(hist)
        print_problem(problem_moved)
        print("")
        print("")
#        return True
      else:
        if solve(problem=problem_moved, move_history=move_history):
          return True          
  return False

solve(problem=problem_global, move_history=[])