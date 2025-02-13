def bouncing_ball(h, bounce, window):
    if h < 0 or not (0 < bounce < 1) or window >= h:
        return -1
    times = 1
    ball_height = h * bounce
    while ball_height > window:
        times += 2
        ball_height *= bounce
    return times


print(bouncing_ball(2, 0.5, 1), 1)
print(bouncing_ball(3, 0.66, 1.5), 3)
print(bouncing_ball(30, 0.66, 1.5), 15)
print(bouncing_ball(30, 0.75, 1.5), 21)

