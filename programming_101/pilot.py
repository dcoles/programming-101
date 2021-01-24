from IPython.core.magic import register_cell_magic


@register_cell_magic
def Example1(line, cell):
    print_result(eval(cell, {}), (12345 + 654321) / (6 * 7))


@register_cell_magic
def Exercise1_1(line, cell):
    print_result(eval(cell, {}), 783 + 295)


@register_cell_magic
def Exercise1_2(line, cell):
    print_result(eval(cell, {}), 1 + 2 * 3 + 4 * 5 + 6 * 7 + 8 * 9)


@register_cell_magic
def Exercise1_3(line, cell):
    print_result(eval(cell, {}), 11 / 9 - 28 / 45 + 22 / 5)


def print_result(result, answer):
    if result is Ellipsis:
        print('☝️ Replace `...` with your answer')
    else:
        print(f'{result} {"✔️" if result == answer else "❌"}')


__all__ = ['Example1', 'Exercise1_1', 'Exercise1_2', 'Exercise1_3']
