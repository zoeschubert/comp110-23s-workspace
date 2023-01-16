
"""EX08 - Data Wrangling."""
__author__ = "730466642"


from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    data_rows: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        data_rows.append(row)
    file_handle.close()
    return data_rows


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    subject_age: list[str] = []
    #step through table
    for row in table: 
        #save every value under the key "header"
        subject_age.append(row[header])
    return subject_age


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Reformats data so that it is a dictionary with column headers."""
    data_cols: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
    #for each key, make a dictionary entry with all column values
        data_cols[key] = column_values(table, key)
    return data_cols


def head(data_cols: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only first N rows of data."""
    data_cols_head: dict[str, list[str]] = {}
    for column in data_cols:
        first_N: list = []
        if rows >= len(data_cols[column]):
            for elem in data_cols[column]:
                first_N.append(elem)
        else: 
            i: int = 0
            while i < rows:
                first_N.append(data_cols[column][i])
                i += 1
        data_cols_head[column] = first_N
    return data_cols_head


def select(data_cols: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a subset of the original column vals."""
    selected_data: dict[str, list[str]] = {}
    for column in names:
        selected_data[column] = data_cols[column]
    return selected_data


def concat(table: dict[str, list[str]], additional_table: dict[str, list[str]]) -> dict[str, list[str]]:
    combined: dict[str, list[str]] = {}
    for column in table:
        combined[column] = table[column]
    for column in additional_table:
        if column in combined:
            combined[column] += additional_table[column]
        else:
            combined[column] = additional_table[column]
    return combined


def count(input: list[str]) -> dict[str, int]:
    race_counts: dict[str, int] = {}
    for item in input:
        if item in race_counts:
            race_counts[item] += 1
        else:
            race_counts[item] = 1
    return race_counts