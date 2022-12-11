# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_txt = "фарвпы ффа абв вабввд лылыщд вавабв"
txt_list = list(filter(lambda i: "а" not in i and "б" not in i and "в" not in i, my_txt.split()))
print(txt_list)



# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
   for i in range(3):
      print(board[0+i*3], board[1+i*3], board[2+i*3])

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Такой ячейки нет!")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Ячейки - числа от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def press(file, result):
    with open(file, "r", encoding="utf-8") as text:
        with open(result, "w", encoding="utf-8") as res:
            inp_str = text.readline()
            ind = 0
            out_str = ""
            count = 1
            while ind < len(inp_str) - 1:
                if inp_str[ind] == inp_str[ind + 1]:
                    count += 1
                else:
                    if count == 1:
                        res.write(inp_str[ind])
                    else:
                        res.write(str(count) + inp_str[ind])
                    count = 1
                ind += 1
            
press("file.txt", "result.txt")

def depress(file, result):
    with open(file, "r", encoding="utf-8") as text:
        with open(result, "w", encoding="utf-8") as res:
            inp_str = text.readline()
            count = ""
            for letter in inp_str:
                if letter.isdigit():
                    count += letter
                else:
                    if count != "":
                        res.write(int(count) * letter)
                    else:
                        res.write(letter)
                    count = ""
depress("result.txt", "result2.txt")