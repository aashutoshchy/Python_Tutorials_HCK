"""
Develop a simulation of Elevator. If the floor is higher than 13
floor than the actual floor will be floor – 1. The output should
contain, Floor pressed by users and the actual floor.
"""

pressed_floor = int(input("Press the floor: "))
if pressed_floor>13:
    actual_florr = pressed_floor-1
else:
    actual_florr = pressed_floor

print("Pressed Floor: ", pressed_floor)
print("Actual Floor: ", actual_florr)

