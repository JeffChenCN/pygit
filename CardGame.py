from random import shuffle


class Card:
    suits = ["Spade", "Heart", "Diamond", "Club"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value > other.value:
            return False
        return self.suit < other.suit

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value < other.value:
            return False
        return self.suit > other.suit

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]


card1 = Card(10, 2)
card2 = Card(11, 3)
card3 = Card(10, 1)
print(card1 < card2)
print(card1 < card3)
print(card3)


class Deck:
    def __init__(self):
        self.cards = []
        for v in range(2, 15):
            for s in range(4):
                self.cards.append(Card(v, s))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def __repr__(self):
        return str(self.cards)


d = Deck()
print(d)
for card in d.cards:
    print(card)


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("player1 name: ")
        name2 = input("player2 name: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print('game time')
        response = None
        while len(cards) >= 2 and response != 'q':
            response = input('q to quit, else wise to play')
            self.player1.card = self.deck.remove_card()
            self.player2.card = self.deck.remove_card()
            print('{} drew {} then {} drew {}'.format(self.player1.name, self.player1.card, self.player2.name, self.player2.card))
            if self.player1.card > self.player2.card:
                self.player1.wins += 1
                print('{} win this round'.format(self.player1.name))
            else:
                self.player2.wins += 1
                print('{} win this round'.format(self.player2.name))
        print('game over, {} win!'.format(self.winner(self.player1, self.player2)))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return 'tie'


game = Game()
game.play_game()
