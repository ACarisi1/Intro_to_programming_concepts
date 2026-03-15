class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

class NFLteam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def print_players(self):
        print("Team:", self.team_name)
        print("Players:")
        for player in self.players:
            print(player.player_name, "-" , player.player_position)


new_team = NFLteam("New Team")
rounds = int(input("Enter number of players to add to your team: "))
for i in range(rounds):
    name = input("Enter player name: ")
    position = input("Enter players position: ")

    player = Player(name, position)
    new_team.add_player(player)

new_team.print_players()