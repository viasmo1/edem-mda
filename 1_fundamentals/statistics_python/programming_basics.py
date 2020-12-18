import matplotlib.pyplot as plt
import time
import math


##########
ax = plt.subplots(figsize=(9, 9))  # Define plot size
ax = plt.gca()  # Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

c1 = plt.Circle((5, 5), 1, color="r")  # Define  circle
ax.add_artist(c1)  # Draw circle


##########
fig2 = plt.figure(figsize=(9, 9))
ax2 = fig2.add_subplot(111)
# change default range so that new circles will work
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))

for i in range(0, 11, 1):
    c = plt.Circle((i, i), 0.5, color="r")
    ax2.add_artist(c)


##########
fig3 = plt.figure(figsize=(9, 9))
ax3 = fig3.add_subplot(111)
# change default range so that new circles will work
ax3.set_ylim((0, 10))
ax3.set_xlim((0, 10))
for i in range(0, 11, 1):
    c1 = plt.Circle((i, i), 0.5, color="r")
    c2 = plt.Circle((i - 1, i - 1), 0.4, color="w")
    ax3.add_artist(c1)
    ax3.add_artist(c2)


##########
for i in range(0, 11, 1):
    fig3 = plt.figure(figsize=(9, 9))
    ax3 = fig3.add_subplot(111)
    # change default range so that new circles will work
    ax3.set_ylim((0, 10))
    ax3.set_xlim((0, 10))
    c1 = plt.Circle((i, i), 0.5, color="r")
    c2 = plt.Circle((i - 1, i - 1), 0.4, color="w")
    ax3.add_artist(c1)
    ax3.add_artist(c2)


##########
fig2 = plt.figure(figsize=(9, 9))
ax2 = fig2.add_subplot(111)
# change default range so that new circles will work
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))

for i in range(0, 11, 1):
    c = plt.Circle((i, i), 0.5, color="r")
    c2 = plt.Circle((10 - i, i), 0.5, color="b")
    ax2.add_artist(c)
    ax2.add_artist(c2)


##########
fig2 = plt.figure(figsize=(9, 9))
ax2 = fig2.add_subplot(111)
# change default range so that new circles will work
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))

for i in range(0, 11, 1):
    c = plt.Circle((i, i), 0.5, color="r")
    c2 = plt.Circle((10 - i, i), 0.5, color="b")
    ax2.add_artist(c)
    ax2.add_artist(c2)


##########
colors = [
    "r",
    "b",
    "orange",
    "g",
    "c",
    "m",
    "y",
    "maroon",
    "darkgreen",
    "aquamarine",
    "k",
]

fig2 = plt.figure(figsize=(9, 9))
ax2 = fig2.add_subplot(111)
# change default range so that new circles will work
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))

for i in range(0, 11, 1):
    c = plt.Circle((i, i), 0.1 * i, color=colors[i])
    ax2.add_artist(c)


############
fig2 = plt.figure(figsize=(9, 9))
ax2 = fig2.add_subplot(111)
# change default range so that new circles will work
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))

for i in range(0, 11, 1):
    c = plt.Circle((i, i), 0.2 * i, color=colors[i], alpha=0.05 * i)
    ax2.add_artist(c)


###############
for i in range(0, 11, 1):
    if i < 5:
        print("My grade is: ", i, " -> FAILED!")
    elif 5 <= i <= 8:
        print("My grade is: ", i, " -> PASSED!")
    else:
        print("My grade is: ", i, " -> CONGRATS!")
