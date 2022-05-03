from single_point import parse
import pandas as pd
import numpy as np

column_count = 15


def parse_data(data_file_full_path):
    """This method parses the data into the final matrix [M x N] - called X matrix.
    and Nx1 vector of classifier results - Y vector.
    """

    final_x_matrix = list()
    final_y_vector = list()

    with open(data_file_full_path) as f:
        for line in f:
            if "?" in line:
                continue

            raw = [x.strip() for x in line.split(",")]
            if len(raw) != column_count:
                continue

            raw = list(map(lambda x: int(x) if x.isdigit() else x, raw))

            try:
                X, y = parse(raw)
                final_x_matrix.append(X)
                final_y_vector.append(y)
            except (ValueError, IndexError) as e:
                # mean we bumped into missing data
                continue

    return final_x_matrix, final_y_vector
