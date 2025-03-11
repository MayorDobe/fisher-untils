class SortingError(Exception):
    """
    Sorting error class.
    """

    def __init__(self, exception_type, message):
        super().__init__(message)
        self.exception_type = exception_type
        self.message = message

    def __str__(self) -> str:
        return f"{self.exception_type}, {self.message}"

    def __repr__(self) -> str:
        return f"{self.exception_type}, {self.message}"


class SortingHat:
    """
    Sorting Hat class a collection of sorting algorithms.
    """

    def __init__(self) -> None:
        self.excs_log = []

    """
    Insertion sort algorithm. Allows sorting of int|float arrays.

    Complexity: O(n^2)

    Args:
        array (list[int|float]): array to sort
        length (int): length of the array
        debug (bool): set true allow sorting to continue if an exception occurs

    Returns:
        None

    Raises:
        SortingError: if array is not int|float

    """

    def insertion_sort(
        self, array: list[int | float], length: int, debug: bool = False
    ) -> None:
        # return if array is of length 0 or 1, we can consider it sorted
        if length <= 1:
            return

        # Begin insertion sort
        for i in range(1, length):
            try:
                # Assign array[i] to key
                key: int | float = array[i]
                # Assign j to i - 1
                j: int = i - 1
                # If j is pointing to a valid index, while key is less than array[j]
                while j >= 0 and key < array[j]:
                    # Shift array[j] to the right
                    array[j + 1] = array[j]
                    # Decrement j
                    j -= 1
                # Assign key to array[j + 1]
                array[j + 1] = key
            # Log exceptions
            except (ValueError, TypeError, IndexError) as e:
                if not debug:
                    raise SortingError(type(e), "Failed to sort array")

                e.add_note(f"Exception occured on itertion {i}/{length}")
                self.excs_log.append(SortingError(type(e), e.__notes__))

    def print_exceptions(self) -> None:
        """
        Print exceptions if any.
        """
        if self.excs_log:
            for exc in self.excs_log:
                print(exc)
        else:
            print("No exceptions occured.")


