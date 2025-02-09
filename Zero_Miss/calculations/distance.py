from .calculator import missedCalculator

# gives standard battle distance: 100m, 200m, 300m
def battleDistance(angle):
    for distance in range(100,400,100):
      metersOffAtDistance, inchesOffAtDistance = missedCalculator(angle, distance)

      print(f"At {distance} meters,you would be {float(metersOffAtDistance)} meters,")
      print(f"or {float(inchesOffAtDistance)} inches off.")
