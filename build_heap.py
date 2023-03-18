# python3
import sys

def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # Try to achieve O(n) and not O(n^2)
    def heap_sort(i):
        
        min_index = i
        left = 2*i + 1
        
        if left < length and data[left] < data[min_index]:
            min_index = left
        right = 2*i + 2
        
        if right < length and data[right] < data[min_index]:
            min_index = right
        
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            heap_sort(min_index)

    length = len(data)
    for i in range(length // 2, -1, -1):
        heap_sort(i)

    return swaps


def main():

    I_or_F= input().strip()
    
    if I_or_F == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    
    elif I_or_F == 'F':
        filename = input("file name: ")
        testfolder = "./tests/" + filename
        with open(testfolder) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    
    else:
        print("invalid input")
        sys.exit(1)

    # Check if length of data is the same as the specified length
    assert len(data) == n

    # Call function to assess the data and give back all swaps
    swaps = build_heap(data)

    # TODO: Output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # Output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
