tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    col_len = []
    val_len = 0
    for val in data:
        val_len = len(val)
        my_len = 0
        for val2 in val:
            if my_len < len(val2):
                my_len = len(val2)

        col_len.append(my_len)

    data_len = len(data)

    for v in range(val_len):
        for q in range(data_len):
            print(data[q][v].rjust(col_len[q]), end=", ")
        print()


print_table(tableData)
