def check_id_valid(id_number):
    """Checks for id validity.
    :param id_number: id number from main
    :type id_number: int
    :return: True if the number is valid, else False
    :rtype: bool
    """
    numbers = [int(digit) for digit in str(id_number)]  # List of id number splited
    actual_numbers = []  # List of doubled numbers in even place and regular numbers in uneven place
    gener = [actual_numbers.append(numbers[i] * 2) if i % 2 != 0 else actual_numbers.append(numbers[i]) for i in
             range(len(numbers))]
    addup = []  # List that adds up the sum of dual-numbered number (for exemp. 12 is 1+2=3)
    for num in actual_numbers:
        if num > 9:
            temp = (int(i) for i in str(num))
            addup.append(sum(temp))
        else:
            addup.append(num)
    return True if sum(addup) % 10 == 0 else False  # Returns True of False base on if the sum can divide by 10


class IDIterator:
    """
    A class used to do a custom iterator for the id which entered in main func.
    :raise: StopIteration: raises an Exception when id>=999999999
    """

    def __init__(self, _id):
        self._id = _id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id == 999999999:
            raise StopIteration()
        else:
            id = int(self._id)
            for x in range(id, 999999999):  # Runs on each id in search of the next one
                id += 1
                if check_id_valid(id):
                    return id


def id_generator(id):
    """Generator function which produce next valid number in range
    :param id: The id number
    :type base: int
    :return: The next valid id
    :ytype: int
    :raise: StopIteration: raises an Exception when id>=999999999
    """
    if id < 999999999:  # As long as the id is under 999999999
        for x in range(id, 999999999):  # Runs on each id in search of the next one
            id += 1
            if check_id_valid(id):
                yield id
    else:
        raise StopIteration()


def main():
    id = int(input("Enter ID:"))
    choice = input("Generator or Iterator? (gen/it)? ")
    if choice == "it":
        for i in range(10):
            user_id = IDIterator(id)  # Saves the iterator
            id = next(user_id)  # Jump to the next func in IDIterator
            print(id)  # Prints the next id
    if choice == "gen":
        for i in range(10):
            id_gener = id_generator(id)  # Saves the generator
            id = next(id_gener)  # Moves to the next iteration
            print(id)  # Prints the next id


main()
