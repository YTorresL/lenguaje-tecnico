def main():
    a = 10  # stored in stack
    p = None  # declaring p variable
    p = 10  # allocating memory in heap
    del p  # deleting memory allocation in heap
    p = [None] * 4  # array in heap allocation
    p = None  # free heap
    return 0


if __name__ == "__main__":
    main()