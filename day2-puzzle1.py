# 12 red, 13 green, 14 blue

color_list = ["red", "green", "blue"]
global_limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_round_result(result: list):
    round_stats = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    result_len = len(result)
    for i in range(0, result_len, 2):
        round_stats[result[i+1]] = int(result[i])
    return round_stats

def is_beyond_limits(round_stats: dict):
    for color in color_list:
        if round_stats[color] > global_limits[color]:
            return True
    return False

def is_game_valid(results: list):
    for result in results:
        round_stats = parse_round_result(result)
        if is_beyond_limits(round_stats):
            return False
    return True

def count_valid_games_sum():
    valid_games = []
    with open("day2-input.txt") as f:
        for line in f:
            number_n_results = line.split(":")
            game_number = number_n_results[0].split()[1]
            results = number_n_results[1].split(";")
            results = [result.replace(",", "").split() for result in results]
            if is_game_valid(results):
                valid_games.append(int(game_number))
    return sum(valid_games)

if __name__ == "__main__":
    print(count_valid_games_sum())
