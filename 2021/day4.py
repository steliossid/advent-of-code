with open("input/input4.txt", "r") as f:
    boards = []
    for line in f:
        if "," in line:
            random_order = [int(number) for number in line.strip().split(",")]
        else:
            if line.split():
                boards.append([int(number) for number in line.split()])

boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]


def has_won(board, called_numbers):
    won = False
    board_rows_cols = board + [[board[j][i] for j in range(len(board))] for i in range(len(board))]
    for line in board_rows_cols:
        if all(number in called_numbers for number in line):
            won = True
    return won


def score(board, called_numbers, current_number):
    numbers_not_called = []
    for row in board:
        for number in row:
            if number not in called_numbers:
                numbers_not_called.append(number)
    return current_number * sum(numbers_not_called)


def winning_board_score(random_order, boards):
    called_numbers = set()
    for current_number in random_order:
        called_numbers.add(current_number)
        for board in boards:
            if has_won(board, called_numbers):
                return score(board, called_numbers, current_number)


print(f"Part 1: What will your final score be "
      f"if you choose that board?: {winning_board_score(random_order, boards)}")


def last_winning_board_score(random_order, boards):
    called_numbers = set()
    for current_number in random_order:
        called_numbers.add(current_number)
        if len(boards) == 1 and has_won(boards[0], called_numbers):
            return score(boards[0], called_numbers, current_number)
        boards = [board for board in boards if not has_won(board, called_numbers)]


print(f"Part 2: Figure out which board will win last. "
      f"Once it wins, what would its final score be?: {last_winning_board_score(random_order, boards)}")
