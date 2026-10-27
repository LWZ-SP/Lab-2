def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()                  # read from the console
    str_list = user_input.split(",")      # split into a list of strings
    num_list = []
    for s in str_list:                    # convert each string to a float
        num_list.append(float(s))
    return num_list


def calc_average_temperature(num_list):
    return sum(num_list) / len(num_list)


def calc_min_max_temperature(num_list):
    return [min(num_list), max(num_list)]


def sort_temperature(num_list):
    return sorted(num_list)


def calc_median_temperature(num_list):
    sorted_list = sort_temperature(num_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average_temperature(num_list)
    min_max = calc_min_max_temperature(num_list)
    median = calc_median_temperature(num_list)

    print("Numbers entered: " + str(num_list))
    print("Average = " + str(average))
    print("Minimum = " + str(min_max[0]))
    print("Maximum = " + str(min_max[1]))
    print("Sorted = " + str(sort_temperature(num_list)))
    print("Median = " + str(median))


if __name__ == "__main__":
    main()