import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1]-point1[1])**2)


while True:
    exit_choice = input ("Press 'x' button to exit. Otherwise press 'Enter': ")
    if exit_choice == "x":
        print("Exited!")
        break
    else:
        x1, y1 = map (float, input("Enter x1 and y1 values for first point: ").split())
        x2, y2 = map (float, input("Enter x2 and y2 values for second point: ").split())

        distance = euclideanDistance((x1, y1), (x2, y2))

        print("Euclidean distance between two points: ",distance)