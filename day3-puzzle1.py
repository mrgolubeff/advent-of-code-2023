digits = [x for x in range(10)]
dot = '.'

def count_sum():
    lines = []
    symbols_map = [[]]
    with open('day3-input.txt') as f:
        for line in f:
            clear_line = line.replace('\n', '')
            lines.append(list(clear_line))
    for line_count, line in enumerate(lines):
        for symbol_count, symbol in enumerate(line):
            pass

if __name__ == '__main__':
    count_sum()
