def hello():
    print('Welcome to Zero Miss! I can tell you how much you will be off at different ranges.')
    print("All I need to know how many inches you were off and what distance, in meters, you chose to zero at.")

    #inchesOff = 1 # inches
    while True:
      try:
        inchesOff = float(input('Inches Off: '))
        break
      except ValueError:
        print('Invalid input. Enter a number.')

    #distance = 25 #meters
    while True:
      try:
        zeroDistance = float(input('Zero Distance: '))
        break
      except ValueError:
        print('Invalid input. Enter a number.')

    return inchesOff, zeroDistance