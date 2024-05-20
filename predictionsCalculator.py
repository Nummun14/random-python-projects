# this code is used to calculate how good a prediction is. You type in the prediction and the results,
# and then given a score. the lower the score, the better the prediction.

def calculate_prediction_score(amount_of_teams):
    prediction = []
    actual_result = []
    score = 0

    for place in range(amount_of_teams, 0, -1):  # gets teams
        predicted_team = input("What team did you predict to finish in " + str(place) + " place? ")
        prediction.append(predicted_team.lower())
        actual_team = input("What team actually finished in " + str(place) + " place? ")
        actual_result.append(actual_team.lower())

    for team in prediction:  # calculates score
        score += abs(prediction.index(team) - actual_result.index(team))
    return score


print(calculate_prediction_score(20))
