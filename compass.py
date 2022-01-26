def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    if facing not in directions:
        return "Wrong facing"

    try:
        turn = int(turn)
        if turn < -1080 or turn > 1080:
            return "Wrong turn"
        if turn % 45 != 0:
            return "Turn is not multiple of 45"
    except ValueError:
        return "Turn is not a number"

    rotation = int((directions.index(facing) + turn / 45) % len(directions))

    return directions[rotation]
