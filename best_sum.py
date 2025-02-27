from typing import List
def best_sum(target_sum: int, numbers: List[int])-> List[int] | None:
    """_Find the shortest list of numbers that achieve a target value from a given list_

    Args:
        target_sum (int): _Sum to achieve_
        numbers (List[int]): _List of int_

    Returns:
        List[int]: _shortest list or None if no solution_
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_list = None
    for number in numbers:
        remainder = target_sum - number
        result =  best_sum(remainder, numbers)
        if result != None:
            current = [number] + result
            if shortest_list == None or len(shortest_list) > len(current):
                shortest_list = current
    return shortest_list

def main() -> None:
    numbers: List[int] = [2, 3, 5]
    target_sum: int = 8
    best: List[int] = best_sum(target_sum, numbers)
    print(f"Shortest list of int for target of {target_sum} from {numbers} is {best}")

if __name__ =="__main__":
    main()
