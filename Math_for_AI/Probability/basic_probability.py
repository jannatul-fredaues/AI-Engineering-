import math

white_ball = int(input("Enter the white ball number: "))
red_ball = int(input("Enter the red ball number: "))
black_ball = int(input("Enter the black ball number: "))
yellow_ball = int(input("Enter the yellow ball number: "))

total_balls = white_ball + red_ball + black_ball + yellow_ball

# Probability of drawing a white ball
prob_white = white_ball / total_balls
print("Probability of drawing a white ball:", prob_white)

# Probability of drawing a red ball
prob_red = red_ball / total_balls
print("Probability of drawing a red ball:", prob_red)

# Probability of drawing a black ball
prob_black = black_ball / total_balls
print("Probability of drawing a black ball:", prob_black)

# Probability of drawing a yellow ball
prob_yellow = yellow_ball / total_balls
print("Probability of drawing a yellow ball:", prob_yellow)

# Probability of drawing a white or red ball
prob_white_red = prob_white + prob_red  
print("Probability of drawing a white or red ball:", prob_white_red)

# Probability of drawing a white and red ball (assuming independent events)
prob_white_and_red = prob_white * prob_red  
print("Probability of drawing a white and red ball:", prob_white_and_red)

# Probability of drawing a white or red ball but not both
prob_white_or_red_but_not_both = prob_white_red - prob_white_and_red
print("Probability of drawing a white or red ball but not both:", prob_white_or_red_but_not_both)

# probability of drawing a white ball given that a red ball is drawn (conditional probability)
prob_white_given_red = prob_white_and_red / prob_red if prob_red > 0 else 0
print("Probability of drawing a white ball given that a red ball is drawn:", prob_white_given_red)
# Probability of whithe ball when red ball is given is drawn (conditional probability)
prob_red_given_white = prob_white_and_red / prob_white if prob_white > 0 else 0
print("Probability of drawing a red ball given that a white ball is drawn:", prob_red_given_white)




