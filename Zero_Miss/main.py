import calculations as cal
import prompts as ppt

#main logic of program
def zeroMiss():
    inchesOff, zeroDistance = ppt.hello()

    ppt.dash()

    metersOff = cal.metersOff(inchesOff)
    angle = cal.angle(metersOff,zeroDistance)
    print(f"At {zeroDistance} meters, you were {str(metersOff)} meters off "
      f"at an angle of {angle:.6f} radians(rounded to the sixth decimal place).")

    ppt.dash()

    cal.battleDistance(angle)

    ppt.dash()

    while True:
      try:
        distance = float(input('At what distance would you like to know how much you will be off? '))
        break
      except ValueError:
        print('Invalid input. Enter a number.')

    metersOffAtDistance, inchesOffAtDistance = cal.missedCalculator(angle, distance)

    print(f"At {distance} meters, you would be {float(metersOffAtDistance)} meters,")
    print(f"or {float(inchesOffAtDistance)} inches off.")

    ppt.dash()
