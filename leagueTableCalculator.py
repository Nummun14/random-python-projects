import random


def by_score_key(item):
    return item[1]


teams_points = {}
teams_games = {}
teams_wins = {}
teams_losses = {}
teams_draws = {}
teams_goals_for = {}
teams_goals_against = {}
week = 1

amount = int(input("how many teams?"))  # amount of teams
times = int(input("how many games do you want each team to play each other?"))  # times teams play each other
win = int(input("how many points for a win?"))  # points for win
draw = int(input("how many points for a draw?"))  # points for draw
loss = int(input("how many points for a loss?"))  # points for loss

for i in range(amount):
    team = input("input the name of a team")  # team names
    teams_games[team] = 0
    teams_points[team] = 0
    teams_wins[team] = 0
    teams_losses[team] = 0
    teams_draws[team] = 0
    teams_goals_for[team] = 0
    teams_goals_against[team] = 0

for u in range(times):
    matches = []

    for i in range(amount - 1):
        print("game-week", week)
        week += 1
        teams_play = list(teams_points.keys())

        # picking teams
        for game in range(len(teams_points) // 2):
            teams_found = False
            while not teams_found:
                team1 = random.choice(teams_play)
                team2 = random.choice(teams_play)

                if team1 == team2:
                    continue
                match = team1 + " vs " + team2
                match_rev = team2 + " vs " + team1
                if match in matches:
                    continue
                teams_play.remove(team1)
                teams_play.remove(team2)
                matches.append(match)
                matches.append(match_rev)
                break

            # game
            results = []
            loop = 0
            while len(results) != 2:
                loop += 1
                if loop > 1:
                    print("you need to print 2 numbers")
                result = input(match)
                results = result.split()

            # statistics
            teams_goals_for[team1] += int(results[0])
            teams_goals_for[team2] += int(results[1])
            teams_goals_against[team2] += int(results[0])
            teams_goals_against[team1] += int(results[1])
            teams_games[team1] += 1
            teams_games[team2] += 1

            # points calculation
            if int(results[0]) > int(results[1]):
                teams_points[team1] += win
                teams_wins[team1] += 1
                teams_points[team2] += loss
                teams_losses[team2] += 1
            elif int(results[0]) == int(results[1]):
                teams_points[team1] += draw
                teams_draws[team1] += 1
                teams_points[team2] += draw
                teams_draws[team2] += 1
            else:
                teams_points[team2] += win
                teams_wins[team2] += 1
                teams_points[team1] += loss
                teams_losses[team1] += 1

        # printing table
        tuples = list(teams_points.items())
        tuples.sort(key=by_score_key, reverse=True)
        print("#|team|Pts|Pl|W|D|L|GF|GA|GD")
        place = 1
        for j in tuples:
            print(place, ".", sep='', end=' ')
            place += 1
            print(j[0], j[1], teams_games[j[0]], teams_wins[j[0]], teams_draws[j[0]], teams_losses[j[0]], end=' ')
            print(teams_goals_for[j[0]], teams_goals_against[j[0]], int(teams_goals_for[j[0]]) - int(teams_goals_against[j[0]]))
