# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.9:
from ps2_verify_movement39 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.9

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.w = width
        self.h = height
        self.numTiles = width * height
        self.dirtyTiles = []
        # make a list of the dirty tiles
        for tw in range(width):
            for th in range(height):
                tile = [tw,th]
                self.dirtyTiles.append(tile)
        # wrote dirty tiles first, all tiles next
        self.allTiles = self.dirtyTiles.copy()
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        tile = [int(pos.getX()), int(pos.getY())]
        if tile in self.dirtyTiles:
            self.dirtyTiles.remove(tile)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        tile = [m,n]
        if tile not in self.dirtyTiles:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.numTiles

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return self.numTiles - len(self.dirtyTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        randX, randY = random.randrange(self.w), random.randrange(self.h)
        randPos = Position(randX, randY)
        return randPos

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.getX() < self.w and 0 <= pos.getY() < self.h:
            return True
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        Note: The Robot class is an abstract class, which means that we will
        never make an instance of it.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        # random start values for position and direction
        self.pos = room.getRandomPosition()
        self.dir = random.randrange(360)
        # clean the starting tile
        self.room.cleanTileAtPosition(self.pos)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.dir

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.dir = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newPos = Position.getNewPosition(self.pos, self.dir, self.speed)
        if self.room.isPositionInRoom(newPos):
            self.pos = newPos
        else:
            self.dir = random.randrange(360) # change direction
        # now clean new position
        RectangularRoom.cleanTileAtPosition(self.room, self.pos)

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    results  = []
    for trial in range(num_trials):
        # clear list and create new instance(s) for each trial
        myRobots = []
        room = RectangularRoom(width, height)
        for r in range(num_robots):
            myRobots.append(robot_type(room, speed))
        # start timer and clean
        time_passed = 0
        while room.getNumCleanedTiles() / room.getNumTiles() < min_coverage:
            # time to clean!
            for bot in range(len(myRobots)): # move each robot
                myRobots[bot].updatePositionAndClean()
                #room.cleanTileAtPosition(myRobots[bot].getRobotPosition())
            time_passed += 1
        results.append(time_passed)
    return sum(results) / len(results)

# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(8, 1.0, 10, 30, 0.8, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newPos = Position.getNewPosition(self.pos, self.dir, self.speed)
        if self.room.isPositionInRoom(newPos):
            self.pos = newPos
        self.dir = random.randrange(360) # change direction
        # now clean new position
        RectangularRoom.cleanTileAtPosition(self.room, self.pos)


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    
    This function runs through different number of robots (x axis) and shows
    the time-steps (y axis) it takes to clean a 20 x 20 room. It plots two
    lines - one for the StandardRobot approach, the other for RandomWalkRobot
    approach.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    
    This function runs through differently-rectangular rooms (x axis) and shows
    the time-steps (y axis) it takes to clean each of these rooms. It plots two
    lines - one for the StandardRobot approach, the other for RandomWalkRobot
    approach.
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.
def showPlots():
    showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room', \
              'Numer of Robots', 'Time-Steps to Clean')
    showPlot2('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms',\
              'Aspect Ratio', 'Time-Steps to Clean')

# =============================================================================
'''
The problem set is done, but I am curious if I can show the effects between
different numbers of trials.
'''
import statistics
import time
# === Self curiosities about number of trials.
def numTrials(title, x_label, y_label):
    """
    Shows a visualization of how the number of trials run can effect the
    spread of averaged Time-Steps to clean a 20*20 room to 80%. Additionally,
    prints the standard deviation of each 
    """
    num_trial_range = range(5, 51, 5)
    times1 = []
    times2 = []
    for num_trials in num_trial_range:
        print("Plotting", num_trials, '/', max(num_trial_range))
        times1.append(runSimulation(1, 1.0, 20, 20, 0.8, num_trials, StandardRobot))
        times2.append(runSimulation(1, 1.0, 20, 20, 0.8, num_trials*10, StandardRobot))
    pylab.plot(num_trial_range, times1)
    pylab.plot(num_trial_range, times2)
    pylab.title(title)
    pylab.legend(('Base Trials', '10x Trials'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    print(statistics.stdev(times1), 'SD of standard trials')
    print(statistics.stdev(times2), 'SD of 10x trials')
    sd_stand.append(round(statistics.stdev(times1), 2))
    sd_10x.append(round(statistics.stdev(times2), 2))

# experiment time!
start_time = time.time()
sd_stand, sd_10x = list(), list() # the standard deviations for each trial
for i in range(10):
    numTrials('Difference in Number of Trials', 'Number of Trials', 'Time-Steps to Clean')

# display the collected data
print('----\n')
print('sd_stand results =', sd_stand)
print('the trials present an average SD and SD(SD) of', statistics.mean(sd_stand),\
      round(statistics.stdev(sd_stand), 3), '\n')
print('sd_10x =', sd_10x)
print('the trials present an average SD and SD(SD) of', statistics.mean(sd_10x),\
      round(statistics.stdev(sd_10x), 3), '\n')

# report the time it took to run this experiment
end_time = time.time()
time_elapsed = round(end_time - start_time, 2)
print('this experiment took', time_elapsed, 'seconds')
