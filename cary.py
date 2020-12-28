class Car:
    """
    This class represents a car objects class. It is the smallest unit in
    the game and will be placed over the board of the game.
    It has 4 attributes which are represented by name, length,
    location and orientation.
    Examples for some cars will be:
    Car(Y, 4, (1,4),0) = YYYY - name is Y, length is 4, the location will
    be given and placed in the board on the point (1,4) and the orientation
    is 0, vertical
    Down here will be the implementation of the class car
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

        
        this is some real shit
    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = [self.location]
        if self.orientation == 0:
            # in case the car is vertical
            for index in range(1, self.length):
                lst.append(
                    tuple([self.location[0] + index, self.location[1]+1]))
            return lst
        if self.orientation == 1:
            # in case the car is horizontal
            for index in range(1, self.length):
                lst.append(
                    tuple([self.location[0]+1, self.location[1] + index]))
            return lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        if self.orientation == 0:
            # in case the car is vertical
            return {'u': "causes the car to drive upwards",
                    'd': "causes the car to drive downwards"}
        if self.orientation == 1:
            # in case the car is horizontal
            return {'r': "causes the car to drive to the right",
                    'l': "causes the car to drive to the left"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
         this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        last = self.car_coordinates()[self.length - 1]
        if self.orientation == 0:
            # in case the car is vertical
            if movekey == "u":
                return [tuple([self.location[0] - 1, self.location[1]])]
            if movekey == "d":
                return [tuple([last[0] + 1, self.location[1]])]
        if self.orientation == 1:
            # in case the car is horizontal
            if movekey == "r":
                return [tuple([self.location[0], last[1] + 1])]
            if movekey == "l":
                return [tuple([self.location[0], self.location[1] - 1])]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.orientation == 1:
            # HORIZONTAL
            if movekey == 'r':
                self.location = (self.location[0], self.location[1] + 1)
                return True
            if movekey == 'l':
                self.location = (self.location[0], self.location[1] - 1)
                return True
        if self.orientation == 0:
            # VERTICAL
            if movekey == 'u':
                self.location = (self.location[0] - 1, self.location[1])
                return True
            if movekey == 'd':
                self.location = (self.location[0] + 1, self.location[1])
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
c1=Car("Z",3,(-1,-1),1)
print(c1.car_coordinates())
