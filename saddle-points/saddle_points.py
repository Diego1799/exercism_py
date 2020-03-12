def saddle_points(matrix):
    ln = len(matrix)
    if ln == 0:
        return [{}]
    col_ln = len(matrix[0])
    for row in matrix:
        if col_ln != len(row):
            raise ValueError("Tienen diferentes longitudes")

    max_key_values = [[(i, v) for i, v in enumerate(row) if v == max(row)] for row in matrix]
    sps = list()
    for row_index, kvs in enumerate(max_key_values):
        for kv in kvs:
            col_index = kv[0]
            value = kv[1]
            column = [row[col_index] for row in matrix]
            if value == min(column):
                sps.append({"row": row_index+1, "column": col_index+1})
    return sps if len(sps) > 0 else [{}]
