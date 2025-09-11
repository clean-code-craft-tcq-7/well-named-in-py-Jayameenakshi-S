from color_code import MAJOR_COLORS, MINOR_COLORS, get_color_from_pair_number

def format_color_map_entry(pair_number, major, minor):
    return f"{pair_number:2} | {major:<6} | {minor:<6}"


def print_reference_manual():
    manual_lines = []
    pair_count = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for i in range(1, pair_count + 1):
        major, minor = get_color_from_pair_number(i)
        manual_lines.append(format_color_map_entry(i, major, minor))
    return "\n".join(manual_lines)


def test_print_reference_manual():
    manual = print_reference_manual()
    assert " 1 | White  | Blue  " in manual
    assert "25 | Violet | Slate " in manual