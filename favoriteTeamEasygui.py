import easygui

team = easygui.choicebox("What's your favorite football team?",
                         choices= ["Arsenal", "Manchester City", "Manchester United", "Liverpool", "Chelsea", "Totenham"])
easygui.msgbox("Your favorite football team is " + team)
