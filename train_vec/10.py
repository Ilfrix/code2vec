def main(table):
    valid_table = get_unique_valid_columns(table)
    split_table = custom_split(valid_table)
    move_table_res = move_table(split_table)
    sorted_table = sort_table(move_table_res)
    return sorted_table


def get_unique_valid_columns(input_table):
    unique_columns = []
    for column in zip(*input_table):
        if [*column] not in unique_columns and column[0] is not None:
            unique_columns.append(list(column))

    return unique_columns


def custom_split(table):
    new_table = []
    for column in table:
        new_column = [[], []]
        for elem in column:
            if elem is not None and ':' in elem:
                tmp = elem.split(':')
                new_column[0].append(tmp[0].replace('/', '-'))
                new_column[1].append(str(round(0.01 * float(tmp[1][:-1]), 2)))
            else:
                new_column[0].append(elem)
        new_table += new_column
    new_table.remove([])
    return check_percent(new_table)


def check_percent(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if (i == 2 and len(table[i][j]) != 4):
                table[i][j] += '0'
    return table


def move_table(table):
    new_table = []
    for column in table:
        new_column = []
        for row in column:
            elem = row
            if '.' in row and (row[0] < '0' or row[0] > '9'):
                index = row.find('.')
                elem = row[index - 1] + '. ' + row[:index - 2]
            new_column.append(elem)
        new_table.append(new_column)
    return new_table


def sort_table(table):
    for i in range(len(table)):
        for j in range(len(table[i]) - 1):
            if (table[0][j] > table[0][j + 1]):
                table[0][j], table[0][j + 1] = table[0][j + 1], table[0][j]
                table[1][j], table[1][j + 1] = table[1][j + 1], table[1][j]
                table[2][j], table[2][j + 1] = table[2][j + 1], table[2][j]
    return table
