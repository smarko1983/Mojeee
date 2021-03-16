# This is my code for the Python Turtle. If the code is not mine, I will mention that.

# Starting Out With Python 4 solutions


# Page 228, repeating squares
move = 30
counter = 0
t.speed(10)

while counter < 20:
    for i in range(1,5):
        t.forward(move)
        t.left(90)
    move = move + 5
    
    
# Page 228 - 8 point star
for i in range(1,15):
    t.forward(100)
    t.right(135)  # 90 + 45

t.done()
    

    
    
# page 229 - Spiral or Hypnotic Pattern
move = 10

for i in range(1,200):
    t.forward(move)
    t.left(90)
    move = move + 10
    
  
    
   
