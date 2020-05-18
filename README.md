# 2048 Game
## Please run this code on windows only as os.system('cls') is used in code which runs in windows
## Please make moves after 0.5s each move,because without it game was running very fast as it was taking input twice on a single press of key
### To run this game in command line 
![github1](https://user-images.githubusercontent.com/64823050/82174010-e3d03b80-98ec-11ea-9121-2946b13195fe.JPG)
* -n refers to board size.
* -w refers to win score.
### Modules imported
![github2](https://user-images.githubusercontent.com/64823050/82174203-82f53300-98ed-11ea-99b0-919e82086e48.JPG)
* os
* numpy
* keyboard
* random
* argparse
* time
### Initializing the board
* To initialize the board i used random.choices().
* This function returns random numbers from a list.
* We can also specify the number of numbers to be returned.
* I took four numbers randomly and then made two indices using them.
* After that i did arr[j][i] = 2 , arr[y][x] = 2 , where i,j,x,y are the random numbers returned. 
### Functions made by me in the code
#### def win(arr,wscore)
* This function checks that whether any number on the board is equal to the winning score.
* If it finds that a number on board is equal to win score then it return 1,which is later used to stop the game and declare win.
#### def assign_two(arr) 
* This function assign 2 two the position where there is 0 .
* Each time this function is called it assign to only one index at which there was zero . 
* In this function i used random.choice to select from indices where there is zero .
#### def move_add(arr)
* This function moves all the elements which can be moved upward as in a 2048 game and adds if possible to add .
* For the feasible elements to move up i have used two loops(i and j), to access each element , after the for loop(j) i have used i!= ... and j != ... in the if statement because it was running in an infinte loop without it,also not considering the last element of last column will not affect our result as it will be considered in the second last element.
* If the element is found to be 0 then i again run a while loop for arr[j][i] == 0 this loop breaks if the element is last .
* But if the element is not last then it moves all the elements after it in that column upwards.
* In my innermost while loop i checked all elements below our element and stored them in a list named list,then i checked its maximum element, if it comes out to be 0 it means all elements after that element in that column are zero, so i stopped the loop there which made it more effecient and also stopped it from getting into an infinite loop.
* After moving the elements up i ran a for loop(j) and if two elements(j and k=j+1) in a column are found to be similar then i added those and shifted all elements upwards .
#### def check(arr)
* This function checks whether any further move can be made on the board or not
* I checked neighouring element of an element in column and row, if found to be similar the function returns 1,if not then 0 .
* To check neighbouring element in row i transposed the matrix and run the same condition as for checking neighbouring elements in column .
### Implementation
* I have used keyboard module to check which key is pressed on keyboard, i stored the key pressed in a variable called keyinp.
* I ran a while loop which will break only after a win or loss, each input is taken by this while loop . 
* If "w" is pressed then feasible elements move up and add as array is passed through move_add() function
* If "a" is pressed then i did transpose of my matrix and then move all feasible elements up using move_add() function, and then finally again taking transpose of returned array, this will move feasible elements to the left and add if possible . 
* If "s" is pressed then i flipped the matrix updown and then used move_add() function and then again flipped the returned array , this will move all feasible elements down and add if possible .
* If "d" is pressed then first i transposed my array and then flipped updown and then send this array through move_add() funtion, then i first flipped updown and then took transpose of the returned array, this will move all the feasible elemnts to the right and add if possible .
* I stored my array before movement in temparr and compared it with the array after movement if they are found to be similar then i did not assign two to a random position and the board will remain as it is, but if they are found to be different then it means that our move has worked so i randomly assign two to a position by calling assign_two() function .
* After that i cleared the screen and print the array.
* I have to stop the function for 0.5s using time.sleep() as it was running very fast and was taking input twice in a single input of key.
* Then i passed my array through win() function which checks whether win score has been obtained and if it is obtained then it breaks the loop.
* Then i passed the function through check() function which tells if a move can be made if can't be made then it breaks the loop .
### Some Screenshots
![github3](https://user-images.githubusercontent.com/64823050/82177433-14b56e00-98f7-11ea-811c-1933de259faf.JPG)
![github 4](https://user-images.githubusercontent.com/64823050/82177450-2565e400-98f7-11ea-88ec-3258486310cf.JPG)
![github5](https://user-images.githubusercontent.com/64823050/82177460-2f87e280-98f7-11ea-8eec-c6bd94835220.JPG)
![github6](https://user-images.githubusercontent.com/64823050/82177483-3b73a480-98f7-11ea-9d89-a8138cae34fc.JPG)
