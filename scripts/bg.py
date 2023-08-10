# python module for greetings.
# when called it returns a formal greeting (for email/etc) with the correct time of day formula.

# Defining Strings, feel free to translate/adapt to your taste.
m1 = "Buongiorno"
m2 = "Buon pomeriggio"
m3 = "Buonasera"

import datetime
currentTime = datetime.datetime.now()
currentTime.hour

if currentTime.hour < 12:
	print(m1)
elif 12 <= currentTime.hour < 18:
	print(m2)
else:
	print(m3)
