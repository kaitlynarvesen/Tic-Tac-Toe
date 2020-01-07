# Tic-Tac-Toe

Command line tic-tac-toe game  
  
- One-player mode  
  - player vs computer  
  - three skill levels  
    -level 1: computer goes in a random open spot each turn  
    -level 2: if computer or player can win on the next turn, the computer goes in that spot, otherwise it goes in a random open spot  
    -level 3: uses minimax algorithm to determine best possible place to go after considering all possible outcomes  
- Two-player mode  
  - player 1 vs player 2  
- Choosing who goes first  
  - at the beginning of each game, a random number from 1-100 (inclusive) will be chosen by the computer  
  - for one-player mode, the computer will choose another random number in this range as the computer "player's" guess, and the    player will be prompted to choose a number in this range  
  - for two-player mode, each player will be prompted to choose a number in this range  
  - the player who is closest to the correct number (the one originally chosen by the computer) gets to go first  
