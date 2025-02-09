from sympy import tan, atan

in_PerMeter = 1/.0254

def metersOff(inchesOff):
    return inchesOff / in_PerMeter

def angle(metersOff,zeroDistance):
    return atan(metersOff/zeroDistance)

def missedCalculator(angle, distance):# predicts miss distance
    metersOffAtDistance = distance*tan(angle) # oppostie = adjacent * tangent
    inchesOffAtDistance = metersOffAtDistance * in_PerMeter
    return metersOffAtDistance, inchesOffAtDistance
