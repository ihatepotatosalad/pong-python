from turtle import Turtle


class Screen_Start(Turtle):
    def __init__(self):
        self.middle_line()
        self.points_player1 = 0
        self.points_bot = 0
        self.players = []
        self.score_board()

    def middle_line(self):
        middle_line = Turtle()
        middle_line.hideturtle()
        middle_line.color('white')
        middle_line.penup()
        middle_line.setposition(0, -400)
        middle_line.pendown()
        middle_line.setposition(0, 400)

    def score_board(self):
        player_score = Turtle()
        player_score.color('white')
        player_score.penup()
        player_score.goto(-300, 300)
        player_score.hideturtle()

        player_score.write(f'player1: {self.points_player1}')
        bot_score = Turtle()
        bot_score.goto(300, 300)
        bot_score.hideturtle()
        bot_score.color('white')
        bot_score.penup()
        bot_score.write(f'player2: {self.points_bot}')
        self.players.append(player_score)
        self.players.append(bot_score)

    def points_player(self):
        self.points_player1 += 1
        self.players[0].clear()
        self.players[0].write(f'player1: {self.points_player1}')

    def points_bots(self):
        self.points_bot += 1
        self.players[1].clear()
        self.players[1].write(f'player2: {self.points_bot}')
