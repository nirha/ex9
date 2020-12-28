

class Boardy:
    """
    this class creates a Board for the game.
    the board consists of cars, which are elements of the class Car.
    The board has a specific size, and for this ex. it will be the size
    of 7x7. Each board has an "exiting cell" which is located in the middle
    line
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        l, c = 10,10
        self.board = [["_" for x in range(l)] for y in range(c)]
        self.board[self.target_location()[0]].append("_")
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
        final_lst = []  # this will be the returned list
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board)):
                final_lst.append((row, col))
        final_lst.append(self.target_location())  # adds the target location
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        return final_lst

    def is_empty(self, car, key):
        """this function receives a car and a movekey and checks if the cell
        it wants to move to is empty
        """
        return self.cell_content(car.movement_requirements(key)[0]) is None

    def check_bound(self, car, key):
        """
        this function receives a car and a movekey and checks if the cell
        it wants to move to is not out of range
        :return:
        """
        return self.is_cor_in_bound(car.movement_requirements(key)[0])

    def is_cor_in_bound(self, cor):
        """
        this func receives a coordinate and returns if it is in the bound
        of the board
        :param cor:
        :return:
        """
        if cor[0] < 0 or cor[1] < 0 or \
                cor[0] > len(self.board) - 1:
            return False

        if cor[0] != self.target_location()[0] and \
                cor[1] > len(self.board[0]) - 1:
            return False

        # it could be in the target location:
        if cor[0] == self.target_location()[0] and \
                cor[1] > len(self.board[self.target_location()[0]]) - 1:
            return False
        return True

    def bound_n_empty(self, car, key):
        """
        this function receives a car and movekey and check if the cell it
        wants to move is in range and is not empty
        :return:
        """
        if self.check_bound(car, key):
            if self.is_empty(car, key):
                return True
        return False

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """

        final_lst = []
        for car in self.car_list:
            keys=[]
            for key in car.possible_moves():
                keys.append(key)
            if 'u' in car.possible_moves() or 'd' in car.possible_moves():
                # VERTICAL
                if self.bound_n_empty(car, 'u'):
                    final_lst.append((car.get_name(), 'u', 'can go up'))
                if self.bound_n_empty(car, 'd'):
                    final_lst.append((car.get_name(), 'd', 'can go down'))
            if 'l' in car.possible_moves() or 'r' in car.possible_moves():
                # HORIZONTAL
                if self.bound_n_empty(car, 'r'):
                    final_lst.append((car.get_name(), 'r', 'can go right'))
                if self.bound_n_empty(car, 'l'):
                    final_lst.append((car.get_name(), 'l', 'can go left'))
        return final_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which
         is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return int((len(self.board) - 1) / 2), len(self.board[0])

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
            # In case it's been added before
            print("The name was already given!")
            return False
        lst = car.car_coordinates()
        for cor in lst:
            # check if all the cor is in bound and empty
            if not self.is_cor_in_bound(cor):
                print("The car is out of bound!")
                return False
            if self.cell_content(cor) is not None:
                print("The car is on other car!")
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
        for car in self.car_list:
            if car.get_name() == name:
                moved_car = car  # finding the car to be moved
        for opt in self.possible_moves():
            if name == opt[0] and movekey == opt[1]:
                self.remove_car(moved_car)
                moved_car.move(movekey)
                self.add_car(moved_car)
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
        if self.cell_content(self.target_location()) is not None:
            return True
        return False


