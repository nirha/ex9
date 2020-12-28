from car import Car


class Board:
    """
    this class creates a Board for the game.
    the board consists of cars, which are elements of the class Car
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        l, c = 8, 8
        self.board = [["_" for x in range(l)] for y in range(c)]
        self.board[3].append("_")
        self.car_list = []
        self.car_names = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        str = ""
        for row in self.board:
            str = str + (' '.join(row)) + "\n"
        return str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        final_lst = []
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board)):
                final_lst.append((row, col))
        final_lst.append((3, 7))
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        return final_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        final_lst = []
        for car in self.car_list:
            if car.orientation == 0:
                if 0 <= car.movement_requirements('u')[0][0] <= 6 and \
                        0 <= car.movement_requirements('u')[0][1] <= 6 \
                        and self.cell_content(car.movement_requirements('u')[0])==None:
                    final_lst.append((car.get_name(), 'u', 'can go up'))
                if 0 <= car.movement_requirements('d')[0][0] <= 6 and \
                        0 <= car.movement_requirements('d')[0][1] <= 6\
                        and self.cell_content(car.movement_requirements('d')[0])==None:
                    final_lst.append((car.get_name(), 'd', 'can go down'))
            if car.orientation == 1:
                if 0 <= car.movement_requirements('r')[0][0] <= 6 and \
                        0 <= car.movement_requirements('r')[0][1] <= 7 \
                        and self.cell_content(car.movement_requirements('r')[0])==None:
                    final_lst.append((car.get_name(), 'r', 'can go right'))
                if 0 <= car.movement_requirements('l')[0][0] <= 6 and \
                        0 <= car.movement_requirements('l')[0][1] <= 6\
                        and self.cell_content(car.movement_requirements('l')[0])==None:
                    final_lst.append((car.get_name(), 'l', 'can go left'))
        return final_lst
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        pass

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (int((len(self.board) - 1) / 2), len(self.board[0]))

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        if self.board[coordinate[0]][coordinate[1]] != "_":
            return self.board[coordinate[0]][coordinate[1]]
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if car.name in self.car_names:
            return False
        for cor in car.car_coordinates():
            if cor[0] < 0 or cor[1] < 0 or cor[0] > 6:
                return False
            if cor[0] != 3 and cor[1] > 6:
                return False
            if cor[0] == 3 and cor[1] > 7:
                return False
            if self.cell_content(cor) is not None:
                return False
        self.car_list.append(car)
        self.car_names.append(car.get_name())
        for point in car.car_coordinates():
            # updating the board
            self.board[point[0]][point[1]] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass" [('o',u'....)('j','n'....)]
        for opt in self.possible_moves():
            if name == opt[0] and movekey == opt[1]:
                for car in self.car_list:
                    if car.get_name() == name:
                        if self.cell_content(
                                car.movement_requirements(movekey)[
                                    0]) is None:
                            self.remove_car(car)
                            car.move(movekey)
                            self.add_car(car)
                            return True
        return False

    def remove_car(self, car):
        """
        this function gets a car and removes it from the board
        """
        for point in car.car_coordinates():
            # updating the board
            self.board[point[0]][point[1]] = "_"
        for name in self.car_names:
            if name == car.get_name():
                self.car_names.remove(name)

    def check_victory(self):
        """
        this function checks victory
        :return: True or Fasle
        """
        if self.cell_content((3,7)) != None:
            return True
        return False
