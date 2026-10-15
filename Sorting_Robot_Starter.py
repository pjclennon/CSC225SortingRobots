"""CSC 225 — Sorting Robot Lottery, simplified edition.

Complete TimeSheet, choose_algorithms, and only your two randomly assigned sorts.
Each sorting function returns (sorted_original_list, number_of_value_comparisons).
Run: python3 Sorting_Robot_Starter.py
"""
import random


class TimeSheet:
    def __init__(self, algorithm):
        # TODO: store the name; initialize a list of comparison counts.
        self.algorithm = algorithm
        self.comparison_counts = []

    def add_run(self, count):
        # TODO: append a nonnegative integer comparison count.
        if count >= 0:
            self.comparison_counts.append(count)
        else:
            raise ValueError

    def average(self):
        # TODO: mean; return None if the list is empty.
        if len(self.comparison_counts) == 0:
            return None

        total = sum(self.comparison_counts)
        count = len(self.comparison_counts)
        return total / count

    def median(self):
        # TODO: middle of a sorted copy, average two middles if even.
        # Return None if the list is empty.
        if len(self.comparison_counts) == 0:
            return None

        sort = sorted(self.comparison_counts)

        n = len(sort)
        mid = n // 2

        if n % 2 == 1:
            return sort[mid]

        return (sort[mid- 1] + sort[mid]) / 2
    
    def standard_deviation(self):
        # TODO: population standard deviation of the comparison counts.
        # Return None if empty; use self.average() to calculate the mean.
        # Do not use the statistics module.
        if len(self.comparison_counts) == 0:
            return None

        mean = self.average()

        total = 0 
        for value in self.comparison_counts:
            total += (value - mean) ** 2

        variance = total / len(self.comparison_counts)

        return variance ** 0.5


    def minimum(self):

        # TODO: return smallest count or None if empty.
        if len(self.comparison_counts) == 0:
            return None

        return min(self.comparison_counts)

    def maximum(self):
        # TODO: return largest count or None if empty.
        if len(self.comparison_counts) == 0:
            return None

        return max(self.comparison_counts)



def bubble_sort(values):
    # TODO if assigned: return (values, comparisons)
    comparisons = 0
    n = len(values)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if values[j] > values[j + 1]:
                values[j],  values[j + 1] = values[j + 1], values[j]
                swapped = True
            if not swapped:
                break
    return values, comparisons


def selection_sort(values):
    # TODO if assigned
    comparisons = 0
    n = len(values)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            comparisons += 1
            if values[j] < values[smallest]:
                smallest = j
        values[i], values[smallest] = values[smallest], values[i]
    return values, comparisons
                

def merge_sort(values):
    # TODO if assigned (you may use temporary lists)
    raise NotImplementedError


def quick_sort(values):
    # TODO if assigned; use last-element pivot
    if len(values) <= 1:
        return values

    pivot = values[-1]
    left = []
    mid = []
    right = []

    for i in values:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                right.append(i)
    return quick_sort(left) + mid + quick_sort(right) 


def heap_sort(values):
    # TODO if assigned; max heap
    raise NotImplementedError


ALGORITHMS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
}


def choose_algorithms(seed):
    """Use random.Random(seed).sample(...) for two DISTINCT names."""
    ran = random.Random(seed)

    name = list(ALGORITHMS.keys())

    selected = ran.sample(name, 2)

    return selected


NUMBER_OF_RUNS = 50
LIST_SIZE = 100


def make_test_lists(seed):
    """Create reproducible random lists; both methods receive identical inputs."""
    rng = random.Random(seed + 1000)
    return [[rng.randint(0, 999) for _ in range(LIST_SIZE)]
            for _ in range(NUMBER_OF_RUNS)]


def run_lab(seed):
    selected = choose_algorithms(seed)
    sheets = {name: TimeSheet(name) for name in selected}
    print(f"Seed: {seed} | Algorithms: {', '.join(selected)}")
    print(f"{'Run':>4} {'Method':12} {'Comparisons':>12}")
    for run_number, original in enumerate(make_test_lists(seed), start=1):
        for name in selected:
            values = original.copy()
            _, count = ALGORITHMS[name](values)
            sheets[name].add_run(count)
            print(f"{run_number:4d} {name:12} {count:12d}")
    print("\nCOMPARISON SUMMARIES")
    for name in selected:
        sheet = sheets[name]
        print(f"{name}: counts={sheet.comparison_counts}, average={sheet.average()}, "
              f"median={sheet.median()}, std_dev={sheet.standard_deviation()}, "
              f"min={sheet.minimum()}, max={sheet.maximum()}")


if __name__ == "__main__":
    seed = int(input("Enter your integer seed: "))
    run_lab(seed)
