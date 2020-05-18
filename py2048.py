import os
import numpy as np
import keyboard
import random
import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument('-n','--board',type=int,help='Size of board')
parser.add_argument('-w','--winscore',type=int,help='Winning score')
args = parser.parse_args()
arr = np.zeros((args.board,args.board))
list = []
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if arr[j][i] == 0:
            list.append([j, i]);
[[j,i],[y,x]] = random.choices(list,weights = None,cum_weights = None,k=2)
arr[j,i] = 2
arr[y,x] = 2
os.system('cls')
print(arr)
length = len(arr)
temparr = np.zeros((args.board,args.board))
def win(arr,wscore):
    flag = 0
    for i in range(0,len(arr)) :
        for j in range(0,len(arr)) :
            if arr[j][i] == wscore :
                flag = 1
    return(flag)
def assign_two(arr) :
    list = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[j][i] == 0:
                list.append([j, i]);
    [j, i] = random.choice(list)
    arr[j][i] = 2
    return(arr)
def move_add(arr):
    for i in range(0,len(arr)):
        flag = 1
        for j in range(0, len(arr)):
            if arr[j][i] == 0 and (i != (len(arr)-1) or j != (len(arr)-1)):
                while (arr[j][i] == 0) and (flag != 0):
                    if j == (len(arr)-1) :
                        break
                    else :
                        k = j
                        list = []
                        while k < (len(arr)-1) and arr[k][i] == 0:
                            arr[k][i] = arr[k + 1][i]
                            list.append(arr[k + 1][i])
                            arr[k + 1][i] = 0
                            flag = max(list)
                            k = k + 1
        for j in range(0,(len(arr)-1)):
            if arr[j][i] == arr[j+1][i] :
                arr[j][i] = 2*arr[j][i]
                arr[j+1][i] = 0
                k = j+1
                while k<(len(arr) - 1) :
                    arr[k][i] = arr[k+1][i]
                    arr[k+1][i] = 0
                    k = k+1
    return(arr)
def check(arr) :
    flag = 0
    for i in range(0, len(arr)):
        for j in range(0, (len(arr) - 1)):
            if arr[j][i] == arr[j + 1][i]:
                flag = 1
            arrtranspose = np.transpose(arr)
            if arrtranspose[j][i] == arrtranspose[j + 1][i]:
                flag = 1
    return(flag)
while True :
    keyinp = keyboard.read_key()
    if keyinp == "w":
        temparr = np.copy(arr)
        arr = move_add(arr)
        if (np.array_equal(arr,temparr) == False) :
            arr = assign_two(arr)
        os.system('cls')
        print(arr)
        time.sleep(0.5)
        flag = win(arr,args.winscore)
        if flag == 1:
            print("YOU WIN")
            break
        flg = check(arr)
        if flg == 0 :
            print("YOU LOSE")
            break
    if keyinp == "a":
        temparr = np.copy(arr)
        arr = np.transpose(arr)
        arr = move_add(arr)
        arr = np.transpose(arr)
        if (np.array_equal(arr,temparr) == False) :
            arr = assign_two(arr)
        os.system('cls')
        print(arr)
        time.sleep(0.5)
        flag = win(arr, args.winscore)
        if flag == 1:
            print("YOU WIN")
            break
        flg = check(arr)
        if flg == 0 :
            print("YOU LOSE")
            break
    if keyinp == "d" :
        temparr = np.copy(arr)
        arr = np.flipud(np.transpose(arr))
        arr = move_add(arr)
        arr = (np.transpose(np.flipud(arr)))
        if (np.array_equal(arr,temparr) == False) :
            arr = assign_two(arr)
        os.system('cls')
        print(arr)
        time.sleep(0.5)
        flag = win(arr, args.winscore)
        if flag == 1:
            print("YOU WIN")
            break
        flg = check(arr)
        if flg == 0 :
            print("YOU LOSE")
            break
    if keyinp == "s" :
        temparr = np.copy(arr)
        arr = np.flipud(arr)
        arr = move_add(arr)
        arr = np.flipud(arr)
        if (np.array_equal(arr,temparr) == False) :
            arr = assign_two(arr)
        os.system('cls')
        print(arr)
        time.sleep(0.5)
        flag = win(arr, args.winscore)
        if flag == 1:
            print("YOU WIN")
            break
        flg = check(arr)
        if flg == 0 :
            print("YOU LOSE")
            break




