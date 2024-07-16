def read_game_data(str):
    max_red_cubes_drawn = 0
    max_green_cubes_drawn = 0
    max_blue_cubes_drawn = 0

    (game, data) = str.split(": ")
    game_id = int(game.split(" ")[1])
    draws = data.split("; ")

    for draw in draws:
        draws_by_color = draw.split(", ")

        for draw_by_color in draws_by_color:
            (cube_number, cube_color) = draw_by_color.split(" ")
            cube_number = int(cube_number.strip())

            match cube_color.strip():
                case 'red':
                    if cube_number > max_red_cubes_drawn:
                        max_red_cubes_drawn = cube_number
                case 'green':
                    if cube_number > max_green_cubes_drawn:
                        max_green_cubes_drawn = cube_number
                case 'blue':
                    if cube_number > max_blue_cubes_drawn:
                        max_blue_cubes_drawn = cube_number
                case _:
                    print("COlor unknown", cube_color)
        

    print(game, "has", len(draws), "draws with ", max_red_cubes_drawn, " max red cubes, ", max_green_cubes_drawn, " max green cubes and ", max_blue_cubes_drawn, " max blue cubes.")
    return ({"game_id": game_id, "red": max_red_cubes_drawn, "green": max_green_cubes_drawn, "blue": max_blue_cubes_drawn})

def main():
    max_red_cubes = 12
    max_green_cubes = 13
    max_blue_cubes = 14

    # sum will contain the sum of the possible game ids 
    sum = 0

    file = open("./src/day02/input.txt", "r")
    for line in file:
        game_data = read_game_data(line)
        if game_data["red"] <= max_red_cubes and game_data["green"] <= max_green_cubes and game_data["blue"] <= max_blue_cubes:
            print("Game with id ", game_data["game_id"], " is possible")
            sum += game_data["game_id"]
            print("sum", sum)

    print(sum)

main()