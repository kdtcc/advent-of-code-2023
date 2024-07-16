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
        

    print(game, "has", len(draws), "draws with at least ", max_red_cubes_drawn, " red cubes, ", max_green_cubes_drawn, " green cubes and ", max_blue_cubes_drawn, " blue cubes.")
    return ({"game_id": game_id, "red": max_red_cubes_drawn, "green": max_green_cubes_drawn, "blue": max_blue_cubes_drawn})

def main():
    # sum will contain the sum of the powers of the sets of cubes 
    power_sum = 0

    file = open("./src/day02/input.txt", "r")
    for line in file:
        game_data = read_game_data(line)
        power = game_data["red"] * game_data["green"] * game_data["blue"]
        power_sum += power

    print("The sum of the powers of the sets is: ", power_sum)

main()