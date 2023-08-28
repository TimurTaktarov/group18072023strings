def list_of_letters(roster: str) -> list:
    simple_list = []
    if not roster:
        return simple_list
    len_of_roster = len(roster)
    position = 0
    while position < len_of_roster:
        symbol_thing = roster[position]
        if symbol_thing not in 'mn':
            simple_list.append(symbol_thing)
        if len(simple_list) == 100:
            return simple_list
        position += 1
    return simple_list

