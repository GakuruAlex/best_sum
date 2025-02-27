from typing import List, Dict
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

def best_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, List[int]] = {0: []})-> List[int]:
    """_Find the shortest list of numbers from a given list that sum up to a given target_

    Args:
        target_sum (int): _target_
        numbers (List[int]): _List of int , from which a target could possibly be constructed_
        memo (_Dict[int, List[int]]_, optional): _Memo object that has already calculated values_. Defaults to {0: []}.

    Returns:
        List[int]: _shortest list of values that add up to target sum_
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_list = None

    for number in numbers:
        remainder = target_sum - number
        result = best_sum_memo(remainder, numbers, memo)
        if result != None:
            current = [number] + result
            if shortest_list == None or len(shortest_list) > len(current):
                shortest_list = current
    memo[target_sum] = shortest_list
    return shortest_list

def main() -> None:
    numbers: List[int] = [1, 2, 5, 25]
    target_sum: int = 100
    best: List[int] = best_sum_memo(target_sum, numbers)
    print(f"Shortest list of int for target of {target_sum} from {numbers} is {best}")

if __name__ =="__main__":
    main()
