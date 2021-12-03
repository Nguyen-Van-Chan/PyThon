import turtle, time, pygame # pygame is used to play sounds

pygame.init()               # initializes pygame so that it can be used later in the following codes

class Player:
    '''
    Used to create instances of player object.
    Has methods to calculate the beers drunk by each players
    and draws them on the screen
    '''

    def __init__(self, text, x, y, score):
        '''
        Initializes objects arguments and values, and calls
        methods needed to create the objects
        :param text:
        :param x:
        :param y:
        :param score:
        '''
        self.turtle = turtle.Turtle()
        self.x = x
        self.y = y
        self.text = text
        self.score = score
        self.num_clicks = 0
        self.turn = False
        self.winner = False
        self.draw_player()
        self.draw_score()

    def draw_player(self):
        '''
        Draws the player on the screen
        :return:
        '''
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(self.x, self.y)
        self.turtle.color("white")
        self.turtle.write(self.text, align="right", font=("Arial", 25, "bold"))

    def draw_score(self):
        '''
        Draws the scores of players, which are beers drunk,
        on the screen. Initial value of scores is zero
        :return:
        '''
        self.turtle.clear()
        self.draw_player()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(self.x, self.y)
        self.turtle.write(("Drank: " + str(self.score)), align="left", font=("Arial", 20, "bold"))


class Beer:
    '''
    Draws the object beers on the screen, and assigns
    different methods to be used for beer objects'
    functionality
    '''
    def __init__(self, x, y):
        '''
        Initializes the values of Beer object
        Uses the global window, adds two images of beers to be used
        later in the methods. Creates a turtle to draw the beers
        x and y arguments are given to determine the positions of beers
        :param x:
        :param y:
        '''
        self.x = x
        self.y = y
        self.clicked = False
        global wn
        wn.addshape("pics/img.gif")
        wn.addshape("pics/img2.gif")
        self.t = turtle.Turtle()
        self.draw_beer(x,y)
        self.t.onclick(self.click_handler)
        self.count = 0


    def draw_beer(self, x, y):
        '''
        Given x and y, draws the beer object which is an image
        :param x:
        :param y:
        :return:
        '''
        self.t.penup()
        self.t.goto(x,y)
        self.t.color("white")
        self.t.shape("pics/img.gif")

    def click_handler(self, x, y):
        '''
        Handles the clicks on beers, adds one to the number of clicks
        each time it is clicked
        Calls the replace_img function to change the image of beers
        once it is clicked
        :param x:
        :param y:
        :return:
        '''
        self.clicked = True
        self.replace_img(x, y)
        self.count +=1

    def replace_img(self, x, y):
        '''
        Replaces the image of beers to a darker one,
        if clicked. If clicked again, calls the change_beer
        function to change the image to the original one.
        :param x:
        :param y:
        :return:
        '''
        self.t.shape("pics/img2.gif")
        self.t.onclick(self.change_beer)

    def change_beer(self, x, y):
        '''
        Changes the image of beer to the original one if
        clicked second time
        :param x:
        :param y:
        :return:
        '''
        self.t.shape("pics/img.gif")
        self.clicked = False
        self.t.onclick(self.click_handler)


class Nim_game:
    '''
    A class to create all the objects in the game, and
    use all its methods
    '''
    def __init__(self):
        '''
        Initializes the values of Nim_game class.
        Adds two pictures of play button to be used in the
        introduction part; Uses global window
        '''
        global wn
        wn = turtle.Screen()
        wn.title("Oktoberfest Challenge")
        wn.bgpic("pics/bar3.gif")
        wn.update()
        wn.addshape("pics/play.gif")
        wn.addshape("pics/play_clicked.gif")
        self.beers = []
        self.num_beers = 0
        self.intr = turtle.Turtle()


    def intro(self):
        '''
        Draws the introduction part of the game, which explains the rules
        of the game, and asks if the player wants to play the game.
        :return:
        '''
        self.intr.speed(0)
        self.bg_of_text()
        self.intr.goto(0, 200)
        self.intr.color("white")
        self.intr.write("Oktoberfest Challenge",align="center", font=("Arial", 30, "bold"))
        self.intr.goto(0, 150)
        self.intr.write("Rules of the game:",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, 100)
        self.intr.write("There will be two players and a pack of beers",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, 60)
        self.intr.write("Players take turns to drink, and must drink 1-3 beers each time",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, 20)
        self.intr.write("The one who drinks the last beer",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, -20)
        self.intr.write("LOSEs the game, and has to buy a new pack.",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, -60)
        self.intr.write("Are you ready to play? (Make sure you have a partner)",align="center", font=("Arial", 20, "bold"))
        self.intr.goto(0, -150)
        self.intr.showturtle()
        self.intr.shape("pics/play.gif")
        self.intr.onclick(self.click_handler)

    def bg_of_text(self):
        '''
        Draws the dark background of the text
        :return:
        '''
        self.intr.hideturtle()
        self.intr.penup()
        self.intr.goto(450, 250)
        self.intr.right(180)
        self.intr.begin_fill()
        for i in range(2):
            self.intr.forward(900)
            self.intr.left(90)
            self.intr.forward(350)
            self.intr.left(90)
        self.intr.end_fill()

    def create_beers(self, n_beers=14):
        '''
        Creates a given number of instances of Beer object
        Default number is 14
        :param n_beers:
        :return:
        '''
        for i in range(int(n_beers)):
            self.beers.append(Beer(400 - (i * 60), 200))
        for i in self.beers:
            i.t.shape("pics/img.gif")

    def click_handler(self, x, y):
        '''
        Changes the picture of play button if clicked
        Calls the method to clear the introduction, and calls the method that creates all the objects on the screen
        to play the game
        :param x:
        :param y:
        :return:
        '''
        self.intr.goto(0,-160)
        self.intr.shape("pics/play_clicked.gif")
        time.sleep(.2)
        self.intr.shape("pics/play.gif")
        self.clear_intr()
        self.create_objects()

    def clear_intr(self):
        '''
        Clears the introduction, and hides the turtle
        :return:
        '''
        self.intr.clear()
        self.intr.hideturtle()

    def create_objects(self):
        '''
        Creates all the objects on the screen to play the game
        :return:
        '''
        pygame.mixer.music.load("sounds/beers.mp3")
        pygame.mixer.music.play()
        self.create_beers()
        btn = Button(self.beers)
        Player1 = Player("Player 1 : ", -280, -170, 0)
        Player2 = Player("Player 2 : ", 320, -170, 0)
        btn.player1 = Player1
        btn.player2 = Player2


class Button:
    '''
    Creates a button that is clickable;
    This is used especially for Drink button
    '''
    def __init__(self, beers):
        '''
        Initializes all the values of the button
        :param beers:
        '''
        global wn
        wn.addshape("pics/drink.gif")
        wn.addshape("pics/drink_pressed.gif")
        wn.addshape("pics/play_again.gif")
        wn.addshape("pics/play_again_pressed.gif")
        self.turt = turtle.Turtle()
        self.create_button()
        self.turt.onclick(self.click_handler)
        self.beers = beers
        self.player1 = None
        self.player2 = None
        self.turn = 0
        self.drank = 0
        self.counter = int(len(self.beers))

    def create_button(self):
        '''
        Creates the button
        :return:
        '''
        self.turt.penup()
        self.turt.goto(0,0)
        self.turt.shape("pics/drink.gif")

    def replace_img(self):
        '''
        Replaces the image of the button to a clicked picture of a button
        Replaces it to the original one if clicked a second time
        :return:
        '''
        self.turt.shape("pics/drink_pressed.gif")
        time.sleep(.2)
        self.turt.shape("pics/drink.gif")

    def win_or_lose(self, counter, who):
        '''
        Checks if there are still beers left on the screen,
        if there is none left, brings up a message telling the player
        who drank the last beer is a loser.
        :param counter:
        :param who:
        :return:
        '''
        if counter < 1:
            global wn
            wn.bgpic("pics/cheering.gif")
            pygame.mixer.music.load("sounds/cheering.mp3")
            pygame.mixer.music.play()
            self.player1.turtle.clear()
            self.player2.turtle.clear()
            self.bg_of_text()
            self.turt.goto(0, 200)
            self.turt.color("white")
            self.turt.write((who + " has lost the game!"),align="center", font=("Arial", 30, "bold"))
            self.turt.goto(0, 100)
            self.turt.write("You go and buy a new pack, Drunkard!",align="center", font=("Arial", 25, "bold"))
            if who == "Player 1":
                self.turt.goto(0, 0)
                self.turt.write("Player 2 gets FREE drink today!",align="center", font=("Arial", 25, "bold"))
            else:
                self.turt.goto(0, 0)
                self.turt.write("Player 1 gets FREE drink today!",align="center", font=("Arial", 25, "bold"))
            self.turt.goto(0,-200)
            self.turt.showturtle()
            self.turt.shape("pics/play_again.gif")
            self.turt.onclick(self.play_again)

    def bg_of_text(self):
        '''
        Draws the dark background of the text
        :return:
        '''
        self.turt.speed(0)
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.goto(450, 300)
        self.turt.right(180)
        self.turt.begin_fill()
        for i in range(2):
            self.turt.forward(900)
            self.turt.left(90)
            self.turt.forward(400)
            self.turt.left(90)
        self.turt.end_fill()

    def play_again(self, x, y):
        '''
        Draws "Play Again" button, and once pressed, calls the Nim game one more time
        :param x:
        :param y:
        :return:
        '''
        self.turt.shape("pics/play_again_pressed.gif")
        time.sleep(0.4)
        self.turt.clear()
        self.turt.hideturtle()
        play_again = Nim_game()
        play_again.create_objects()

    def click_handler(self, x, y):
        '''
        Handles the clicks of the Drink button, gets rid of the clicked beers, and adds them to the
        score of the corresponding player, and calls methods to clear the clicked beers, and change
        the players' turns.
        :param x:
        :param y:
        :return:
        '''
        self.replace_img()
        num = 0
        num_clicked = 0
        for i in self.beers:
            if i.clicked is True:
                num_clicked += 1
                if num_clicked < 4:
                    i.t.hideturtle()
                    num += 1
                elif num_clicked > 3:
                    for i in self.beers:
                        i.change_beer(x, y)
                        i.clicked = False
        if num_clicked != 0:
            pygame.mixer.music.load("sounds/beer_opening.mp3")
            pygame.mixer.music.play()
            time.sleep(.2)
            pygame.mixer.music.load("sounds/slurp.mp3")
            pygame.mixer.music.play()
            self.clear_clicks()
            self.switch_player(num)

    def switch_player(self, num):
        '''
        Switches the players' turns
        :param num:
        :return:
        '''
        if self.turn == 0:
            self.counter -= num
            self.player1.score = num + self.player1.score
            self.player1.draw_score()
            self.drank += num
            self.turn = 1
            who = "Player 1"
            self.win_or_lose(self.counter, who)
        else:
            self.counter -= num
            self.player2.score = num + self.player2.score
            self.player2.draw_score()
            self.drank += num
            self.turn = 0
            who = "Player 2"
            self.win_or_lose(self.counter, who)

    def clear_clicks(self):
        '''
        Gets rid of the clicked beers
        :return:
        '''
        for i in self.beers:
            if i.clicked == True:
                i.clicked = False


def main():
    '''
    Call to create objects and use their methods
    :return:
    '''
    global wn
    test = Nim_game()           # Creates an instance of a Nim_game class
    test.intro()                # Call to the intro() method of the Nim game
    wn.mainloop()


if __name__ == '__main__':
    main()                      # Call to main() function
