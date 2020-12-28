import helper
from car import Car
from board import Board
import sys



class Game:
    """
    this is the main class of ex9, it generates a new game and lets the user
    play it. It uses the class board and car.
    Game works like this:
    1. making an initial board using json file, if there exists
    illegal inputs it skips them
    2. every turn the user moves one car, one step, by choosing the
    car and the wanted directon, if all good it moves, if not, error will be
    printed
    3. the game will be ended upon clicking ! key, or when the car is the
    winning location
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print("Current board is")
        print(self.__board.__str__())

    def create_cars(self, car_dict):
        """
        this function creates a car from the json file
        :return:
        """
        names = ['Y', 'B', 'W', 'O', 'G', 'R']
        for key in car_dict:
            length = car_dict[key][0]
            orientation = car_dict[key][2]
            # too big :
            if length < 2 or length > 4 or (
                    # wrong orientation
                    orientation != 0 and orientation != 1) \
                    or (key not in names):  # wrong name:
                continue
            car = Car(key, length, tuple(car_dict[key][1]),
                      orientation)
            self.__board.add_car(car)

    def single_change(self, choose):
        """this function makes a single change"""
        for opt in self.__board.possible_moves():
            if opt[0] == choose[0] and opt[1] == choose[2]:
                self.__board.move_car(choose[0], choose[2])
                return True
        return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        names = ['Y', 'B', 'W', 'O', 'G', 'R']
        # implement your code here (and then delete the next line - 'pass')
        while not self.__board.check_victory():
            print("Current status:")
            print(self.__board.__str__())
            choose = input(
                "please enter the name of the car you want to move\n"
                "and the direction, in the following form: name,direction\n"
                "please enter ! if you wish to end the game ")
            if len(choose) != 1 and len(choose) != 3:
                print("wrong input. Try again")
                continue
            if choose[0] == '!':
                break
            if choose[0] not in names:
                print("Invalid color. Try again")
                continue
            if self.single_change(choose):
                print("the change have been done")
            else:
                print("there is something wrong with the given\n"
                      "direction, try again")
        if self.__board.check_victory():
            print("Congrats!! You made it")
        else:
            print("thanks for trying")


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section
    if len(sys.argv) == 2:
        board = Board()
        game = Game(board)
        car_dict = helper.load_json(sys.argv[1])
        game.create_cars(car_dict)
        game.play()
    else:
        print("please enter a valid path for json File")