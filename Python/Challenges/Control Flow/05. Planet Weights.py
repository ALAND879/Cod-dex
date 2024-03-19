"""
The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

Asks the user what their Earth weight is (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14
If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
"""

Earth_Weight = float(input())
Planet_Number = int(input())

if Planet_Number == 1:
    Destination_Weight = Earth_Weight * 0.38

elif Planet_Number == 2:
    Destination_Weight = Earth_Weight * 0.91

elif Planet_Number == 3:
    Destination_Weight = Earth_Weight * 0.38

elif Planet_Number == 4:
    Destination_Weight = Earth_Weight * 2.53

elif Planet_Number == 5:
    Destination_Weight = Earth_Weight * 1.07

elif Planet_Number == 6:
    Destination_Weight = Earth_Weight * 0.89

elif Planet_Number == 7:
    Destination_Weight = Earth_Weight * 1.14

else:
    print("Invalid planet number")
