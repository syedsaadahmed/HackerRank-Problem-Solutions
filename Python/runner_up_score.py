if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())  
    first, second = None, None
    for i in arr:
        if i > first:
            first, second = i, first
        elif first > i > second:
            second = i
    print second
