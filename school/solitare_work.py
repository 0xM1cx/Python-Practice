import random

# class Card:
#     def __init__(self, shape, rank, open = False):

class Card:
    def __init__(self, shape, rank, open = False):
        self.shape = shape
        self.rank = rank
        self.open = open

    def color(self):
        return 'Red' if self.shape in ['H', 'D'] else 'Black'

    def __str__(self):
        if self.open: # card is open = show
            return "{}{}".format(self.shape, self.rank)
        else:  # card closed = []
            return "[]"

class Solitaire:
    def __init__(self):
        self.piles = [[] for _ in range(7)]
        self.stock = []
        self.foundations = [[] for _ in range(4)]
        self.remaining_cards = []
        self.dealt_cards = set()
        self.initialize_game()

    def initialize_game(self):
        shapes = ['H', 'D', 'c', 's']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        deck = [Card(shape, rank, open = False) for shape in shapes for rank in ranks]
        random.shuffle(deck)

        for x in range(7): # cards to piles
            self.piles[x] = deck[x * (x + 1) // 2 :][:x + 1]

        for pile in self.piles: # last card = open
            if pile:
                pile[-1].open = True

        bottom_card = Card("XX", " ", open = False) # XX if empty

    def print_game_screen_layout(self):
        print("S O L I T A I R E")
        if self.stock:
            print("S: ", str(self.stock[0]))
        else:
            print("S: []   A: {}   B: {}   C: {}   D: {}".format(*('XX' if not card else str(card) for card in self.foundations)))  # print the foundation and stock

        print(":    ".join(str(i) for i in range(1, 8)))  # # number on top of cards
        max_pile_height = max(len(pile) for pile in self.piles) # max num of cards in each pile
        for row in range(1, max_pile_height + 1): # every row in the range starts from 1, then will add 1 to the height
            row_str = ""
            for pile in self.piles:
                if row <= len(pile):
                    row_str += f"{pile[row-1]}    " # adds the string of the card at position row-1 in the current pile
                else:
                    row_str += "      " # maintain allignment
            print(row_str.rstrip())

    def move_card(self, from_pile_index, target_pile_index):
        if not self.valid_pile(from_pile_index) or not self.valid_pile(target_pile_index):
            print("Invalid pile index.")
            return

        from_pile = self.piles[from_pile_index]
        target_pile = self.piles[target_pile_index]

        if not from_pile or not from_pile[-1].open:
            print("Invalid move. No open card in the source pile.")
            return

        held_card = from_pile.pop()

        if self.valid_move(held_card, target_pile):
            target_pile.append(held_card)
            print(f"Moved {held_card} from pile {from_pile_index + 1} to pile {target_pile_index + 1}.")
        else:
            print("Invalid move. Card cannot be moved to the target pile.")

    def valid_pile(self, pile_index):
        return 0 <= pile_index < int(len(self.piles))


    def deal_stock(self):
        if not self.stock:
            print("Stock is empty.")
            return

        held_card = self.stock.pop(0) # get top card
        foundation_index = int(input("Choose foundation (A-D) to move the card: ")) - 1
        row_index = int(input("Choose row (1-4 to move the card: )")) -1

        if self.valid_move(held_card, self.foundations[foundation_index]): #if valid, move
            self.foundations[foundation_index].append(held_card)
        else:
            print("Invalid move. Card cannot be moved to the foundation.")
        if self.valid_move(held_card, self.piles[row_index]):
            self.piles[row_index].append(held_card)
        else:
            print("Invalid move. Card cannot be moved to the row.")

    def valid_move(self, card, destination_pile):
      if not destination_pile: # empty (any card can be placed)
        return True
      else:
        print("Invalid move. Card cannot be moved.")

    def load_game(self, file_name):
        with open(file_name, 'r') as file: #'r' = read
            lines = file.readlines() # read all lines of file into lines

        self.stock = [Card(card[0], card[1:]) for card in lines[0].split()[1:]] #get stock from first line

        for i in range(1, 7):
            pile_cards = [Card(card[0], card[1:]) for card in lines[i].split()[2:]] #card info per pile
            self.piles[i - 1].cards = pile_cards # assign to i-1 (excluded)
            if pile_cards:
                pile_cards[-1].open = True # if pile has cards, open the last

        for i in range(8, 11): # foundation
            foundation_cards = [Card(card[0], card[1:]) for card in lines[i].split()[1:]]
            self.foundations[i - 8].cards = foundation_cards

def play():
    game = Solitaire()

    while True:
        game.print_game_screen_layout()

        # Displays the menu of the game.
        print("Menu:")
        print("[1] Move")
        print("[2] Deal")
        print("[3] Save")
        print("[4] Load")
        print("[CTRL-C] Exit")

        user = input("Enter choice: ").upper()  # Gets user's input.

        if user == '1':
            hold = input("Card to move: ") # Gets user's input.
            target_pile = input("Target pile: ") # Gets user's input.
            game.move_card(hold, target_pile)
        elif user == '2':
            game.deal_stock()
        elif user == '3':
            file_name= input("Enter filename to save: ").upper()
            print("Saved!")
        elif user == '4':
            print("Load")
        elif user == 'E':
            break
        else:
            print("Invalid choice. Please try again.") # If the user inputs other character/s.

play()