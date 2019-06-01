# CSC 310 Assignment 1 - Conway's Game of Life
# Micheal Martel
# Aaron Schneidereit 
# Ian Pascoe
# Feb 1, 2019

import sys
import os
import time
import random

def main():#creates board and generations

    board_size = 40
    num_generation = 100

    game_life(board_size, num_generation)



def game_life(board_size, num_generation):

    life = [' ', '*']#alive and empty  cells 
    array = [] #game board
 
    for i in range (0, board_size): # fills initial array
        row = []
        for j in range (0, board_size):
            x = random.randint(0, 1)
            row.append(life[x])
        
        array.append(row)
    

    for i in range (0, num_generation): # runs the game
        display_array(array)
        rules(array, board_size)



def rules(array, board_size): #decides whether a cell lives or dies 
    for i in range (0,board_size):
        for j in range (0,board_size):
            element = array[i][j]
            if element == '*': #checking for a live cell
                if i == 0: #Checking if cell is in first row
                    if j == 0:#checks if cell is the top left corner 
                        count = cor_cell(array, board_size, i, j)
                    elif j == board_size-1:#checks if cell is in top right corner 
                        count = cor_cell(array, board_size, i, j)
                    elif j != 0:#checks if cell is in the top row
                        count = top_cell(array, board_size, i, j)

                elif i == board_size-1: # Checking if cell is in last row
                    if j == 0:#checks if cell is in the bottom left corner
                        count = cor_cell(array, board_size, i, j)
                    elif j == board_size -1:#checks if cell is in the bottom right 
                        count = cor_cell(array, board_size, i, j)
                    elif j != 0:#checks if cell is on the bottom row
                        count = bot_cell(array, board_size, i, j)

                elif i != 0:#checking if cell is between top and bot
                    if j == 0:#checks if cell on the left edge
                        count = left_cell(array, board_size, i, j)
                    elif j == board_size-1:#checks if cell is on the right edge 
                        count = right_cell(array, board_size, i, j)
                    elif j != 0:#checks if cell is in the middle of the board
                        count = safe_cell(array, board_size, i, j)

                if count < 2:
                    #dies
                    array[i][j] = ' '
                elif count == 2 or count == 3:
                    #lives
                    array[i][j] = '*'
                elif count > 3:
                    #dies
                    array[i][j] = ' '
            else: # checking for a dead cell
                if i == 0: #Checking if cell is in first row
                    if j == 0: #checks if cell is the top left corner 
                        count = cor_cell(array, board_size, i, j)
                    elif j == board_size-1: #checks if cell is in top right corner
                        count = cor_cell(array, board_size, i, j) 
                    elif j != 0: #checks if cell is in the top row
                        count = top_cell(array, board_size, i, j)

                elif i == board_size-1: # Checking if cell is in last row
                    if j == 0: #checks if cell is in the bottom left corner
                        count = cor_cell(array, board_size, i, j)
                    elif j == board_size -1: #checks if cell is in the bottom right 
                        count = cor_cell(array, board_size, i, j)
                    elif j != 0: #checks if cell is on the bottom row
                        count = bot_cell(array, board_size, i, j)

                elif i != 0: #checking if cell is between top and bot
                    if j == 0: #checks if cell on the left edge
                        count = left_cell(array, board_size, i, j)
                    elif j == board_size-1: #checks if cell is on the right edge 
                        count = right_cell(array, board_size, i, j)
                    elif j != 0: #checks if cell is in the middle of the board
                        count = safe_cell(array, board_size, i, j)

                if count == 3:
                    #live
                    array[i][j] = '*'
                    
def safe_cell(array, board_size, i, j): #checks cells that are not on the edge

    count = 0

    if array[i-1][j-1] == '*':
        count+=1
    if array[i-1][j] == '*':
        count+=1
    if array[i-1][j+1] == '*':
        count+=1
    if array[1][j-1] == '*':
        count+=1
    if array[i][j+1]== '*':
        count+=1
    if array[i+1][j-1] == '*':
        count+=1
    if array[i+1][j] == '*':
        count+=1
    if array[i+1][j+1] == '*':
        count+= 1
    return count    

def top_cell(array, board_size, i, j): #check cells that are on the top row

    count = 0

    if array[i][j-1] == '*':
        count+=1
    if array[i][j+1] == '*':
        count+=1
    if array[i+1][j-1] == '*':
        count+=1
    if array[i+1][j] == '*':
        count+=1
    if array[i+1][j+1] == '*':
        count+=1
    
    return count                                                                    


def bot_cell(array, board_size, i, j): #check cells that are on the bottom row

    count = 0
    
    if array[i][j-1] == '*':
        count +=1
    if array[i][j+1] == '*':
        count+=1
    if array[i-1][j-1] == '*':
        count+=1
    if array[i-1][j] == '*':
        count+=1
    if array[i-1][j+1] == '*':
        count+=1

    return count                        


def left_cell(array, board_size, i, j): #check cells that are on the left side

    count = 0

    if array[i-1][j] == '*':
        count+=1
    if array[i-1][j+1] == '*':
        count+=1
    if array[i][j+1] == '*':
        count+=1
    if array[i+1][j+1] == '*':
        count+=1
    if array[i+1][j] == '*':
        count+=1
    
    return count            

def right_cell(array, board_size, i, j): #check cells that are on the right side

    count = 0

    if array[i-1][j] == '*':
        count+=1
    if array[i-1][j-1] == '*':
        count+=1
    if array[i][j-1] == '*':
        count+=1
    if array[i+1][j-1] == '*':
        count+=1
    if array[i+1][j] == '*':
        count+=1

    return count

def cor_cell(array, board_size, i , j): #checks cells in the corners
    count = 0
    if i == 0:
        if j == 0:
            #top left
            if array[i][j+1] == '*':
                count+=1
            if array[i+1][j+1] == '*':
                count+=1
            if array[i+1][j] == '*':
                count+=1
        elif j == board_size - 1:
            #top right
            if array[i][j-1] == '*':
                count+=1
            if array[i+1][j-1] == '*':
                count+=1
            if array[i+1][j] == '*':
                count+=1
    elif i == board_size - 1:
        if j == 0:
            #bot left
            if array[i-1][j] == '*':
                count+=1
            if array[i-1][j+1] == '*':
                count+=1
            if array[i][j+1] == '*':
                count+=1
        elif j == board_size-1:
            #bot right
            if array[i-1][j-1] == '*':
                count+=1
            if array[i-1][j] == '*':
                count+=1
            if array[i][j-1] == '*':
                count+=1
    return count


def display_array(array): #displays array 

    os.system('clear')

    rows = len(array)
    cols = len(array[0])

    if rows == 0:
        raise ValueError("Array contains no data")


    for i in range(rows):
        for j in range (cols):
            print (array[i][j],end=' ')
        print()
    time.sleep(.25)

main()