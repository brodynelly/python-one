#accepts user input for variables
pos = input("Input initial position: ")
pos_float = float(pos)

vel = input("Input initial velocity: ")
vel_float = float(vel)

acc = input("Input acceloration: ")
acc_float = float(acc)

t = input("Input time: ")
t_float = float(t)

#calculate input 
def calculate(pos_float, vel_float, acc_float, t_float): 
    result = float()
    result = pos_float + vel_float*(t_float) + 1/2*(acc_float)*(t_float)*(t_float)
    return result

#print result
print("the final position is: " + calculate(pos_float, vel_float, acc_float, t_float))