"""
Build a Travel Weather Planner
------------------------------
Dtermine whether commuting is
 possible based on the weather, 
 the distance to travel, and the 
 availability of a vehicle.

 
1. Create a variable named distance_mi that stores a number representing the distance to travel in miles.

2. Create a variable named is_raining that stores a boolean (True or False) representing whether the user is currently experiencing rainy weather.

3. Create a variable named has_bike that stores a boolean representing if the user has a bicycle.

4. Create a variable named has_car that stores a boolean representing if the user has a car.

5. Create a variable named has_ride_share_app that stores a boolean representing if the user has an app that allows them to request a ride.

6. Use conditional statements to determine whether commuting is possible based on the values of these variables.

7. Use if, elif, and else statements to evaluate the distance categories in ascending order.

8. If distance_mi is a falsy value:
   Print False.

9. If the distance is less than or equal to 1 mile:
   Print True only if it is not raining.
   Otherwise, print False.

10. If the distance is greater than 1 mile and less than or equal to 6 miles:
    Print True only if the person has a bike and it is not raining.
    Otherwise, print False.

11. If the distance is greater than 6 miles:
    Print True if the person has a car or has a ride-share app.
    Otherwise, print False.
 

"""

distance_mi = 3 #distance in miles
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True


if not distance_mi:
    print(False)



elif distance_mi <= 1:
    print(not is_raining)

elif distance_mi >1 and distance_mi <=6:
    print( has_bike and is_raining )

elif distance_mi > 6:
    print(has_car or has_ride_share_app)
else:
    print(False)