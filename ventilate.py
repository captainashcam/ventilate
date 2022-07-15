# --------------------------
# TODO
# - update isFanRunning() to check GPIO
# - update startFan() and stopFan() to use GPIO
# 
# WHEN LIVE
# - remove fanRunning variable
#
# https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python
# --------------------------


from datetime import date

# --------------------------
# ----- fan management -----
# --------------------------

# this variable can be deleted when using files
fanRunning = False

def isFanRunning():
  if (fanRunning):
    return True
  else:
    return False


# check fan is not running, then start fan
def startFan():
  global fanRunning

  if (not isFanRunning()):
    print("run fan")
    fanRunning = True


# check fan is running, then stop fan
def stopFan():
  global fanRunning

  if (isFanRunning()):
    print ("stop fan");
    fanRunning = False


# -------------------------------------------------
# ----- config - put these into separate file -----
# -------------------------------------------------

# override = 10

# target temps
target = {
  "Dec": 22, "Jan": 22, "Feb": 22,
  "Mar": 20, "Apr": 19, "May": 18,
  "Jun": 16, "Jul": 16, "Aug": 16,
  "Sep": 18, "Oct": 19, "Nov": 20
}

# ---------------------
# ----- main body -----
# ---------------------

iterations = 1
while iterations <= 2:

  # check if override is set
  if ('override' in locals()):
    targetTemp = override
  else:
    # get current date
    today = date.today()

    # get target temp
    targetTemp = target[today.strftime("%b")]

    # read loft temp
    loftTemp = 4

    # read house temp
    houseTemp = 22
  # endelse

  print ("house = " + str(houseTemp))
  print ("loft = " + str(loftTemp))
  print ("target = " + str(targetTemp))

  if ((houseTemp < targetTemp) and (loftTemp > houseTemp)):
    # heat house
    print ("heating")
    startFan()
  elif ((houseTemp > targetTemp) and (loftTemp < houseTemp)):
    # cool house
    print ("cooling")
    startFan()
  else:
    # no action
    stopFan()

  iterations += 1
  print ("-----")
