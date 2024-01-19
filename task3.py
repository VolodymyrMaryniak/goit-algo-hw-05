import timeit
from tabulate import tabulate

from substring_search_algorithms.rabin_karp import rabin_karp_search
from substring_search_algorithms.kmp import kmp_search
from substring_search_algorithms.boyer_moore import boyer_moore_search
from substring_search_algorithms.naive import naive_search


def read_text_from_file(filename):
    with open(filename, "r", encoding="cp1251") as file:
        return file.read()


def measure_time(search_function, text, pattern):
    return timeit.timeit(lambda: search_function(text, pattern), number=100)


def compare_search_algorithms(text_file, pattern):
    text = read_text_from_file(text_file)

    search_algorithms = [
        ("Rabin-Karp", rabin_karp_search),
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Naive", naive_search),
    ]

    results = []
    for algorithm_name, search_algorithm in search_algorithms:
        result = search_algorithm(text, pattern)
        real_pattern_time = measure_time(search_algorithm, text, pattern)
        results.append([algorithm_name, text_file, pattern, result, real_pattern_time])

    headers = ["Algorithm Name", "Text file", "Pattern", "Result", "Time"]

    print(tabulate(results, headers=headers, tablefmt="github"))
    print('\n' * 3)


def main():
    print("Experiment 1. Existing pattern")
    compare_search_algorithms("article1.txt", "елементів у відсортованому")

    print("Experiment 2. Non-existing pattern")
    compare_search_algorithms("article1.txt", "пошук елементів у відсортованому")

    print("Experiment 3. Existing pattern")
    compare_search_algorithms("article2.txt", "Час доступу до окремого елементу")

    print("Experiment 4. Non-existing pattern")
    compare_search_algorithms("article2.txt", "Час доступу до окремого елемента")

if __name__ == "__main__":
    main()
