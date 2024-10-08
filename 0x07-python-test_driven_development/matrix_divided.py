def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number and rounds the result.

    Args:
        matrix (list of list): A list of lists containing integers or floats.
        div (int or float): The number by which to divide the matrix elements.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats,
                    or if the rows of `matrix` are not all the same size,
                    or if `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Returns:
        list: A new matrix containing the divided values rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row is of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
