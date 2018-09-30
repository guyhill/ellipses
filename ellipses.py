import math
import matplotlib.pyplot as plt
import sys

x=0
y=1

dt = 0.0001 # small time interval

# mode selection
if len(sys.argv) < 2:
    mode = "3d"
else:
    mode = sys.argv[1]

if mode == "3d":
    pow = 3
    max_orbits = 1
    vmin = 5
    vmax = 13
elif mode == "2d":
    pow = 2
    max_orbits = 5
    vmin = 5
    vmax = 5
elif mode == "1d":
    pow = 1
    max_orbits = 5
    vmin = 5
    vmax = 5
elif mode == "constant":
    pow = 0
    max_orbits = 1
    vmin = 5
    vmax = 13
else:
    print("unknown mode {}. Valid modes are '1d', '2d', '3d' and 'constant'".format(mode))
    quit(1)


# loop over different orbits
for vy in range(vmin, vmax + 1):
    # Note that r, v and a are 2 dimensional. We ignore the z coordinate here because
    # planetary orbits lie inside a plane
    r = [1, 0] # initial position of planet
    v = [0, float(vy) / 10.0] # initial velocity of planet
    a = [0, 0] # acceleration of planet (placeholder only)

    result = [r[:]] # resulting list of positions of the planet over time
    status = 0 # Used to detect when we have calculated the required number of orbits

    # loop over successive time intervals of length dt
    while True:
        # calculate acceleration
        lenr = math.sqrt(r[x] ** 2 + r[y] ** 2) # Calculate length of vector r using Pythagoras
        a[x] = -r[x] / lenr ** pow # Acceleration from 2nd law of motion and Newton's law of gravitation
        a[y] = -r[y] / lenr ** pow

        # Update position
        # From the definition of velocity as the rate of change of position
        r[x] += v[x] * dt
        r[y] += v[y] * dt

        # Update velocity
        # From the definition of acceleration as the rate of change of velocity
        v[x] += a[x] * dt
        v[y] += a[y] * dt

        # Store position for later
        result.append(r[:])

        # increase status whenever the orbit crosses the x axis. Two x axis crossings constitute 1 orbit
        # Even status means that the planet is above the x axis, odd status means below.
        if status % 2 == 0 and r[y] < 0: 
            status += 1
        elif status % 2 == 1 and r[y] > 0:
            status += 1
        elif status == max_orbits * 2:
            break

    plt.plot(
        [ r[x] for r in result ],
        [ r[y] for r in result ]
    )

plt.plot(0, 0, 'ko') # Plot sun in the center
axes = plt.gca()
axes.set_aspect('equal', 'box') # Make axes square, so that a circle is recognizable as such
axes.axhline(y=0, color='k') # Plot the axes themselves
axes.axvline(x=0, color='k')
plt.show()
