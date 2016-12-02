def move(start_pt,end_pt):
    """Function takes starting position and final position as parameters and
    returns the minimum number of steps needed to reach there according to the given condition."""

    steps = 0
    while (start_pt != end_pt):
        # print steps,":", start_pt,"-", end_pt
        if start_pt > end_pt:
            steps += (start_pt - end_pt)
            start_pt = end_pt
        else:
            steps += 1
            start_pt *= 2
    return steps

def main():
    try:
        test_cnt = int(raw_input("Enter number of test cases : "))
        for i in range(test_cnt):
            def inner():
                try:
                    st_pt = int(raw_input("Enter start point : "))
                    en_pt = int(raw_input("Enter end point : "))
                    print str(move(st_pt,en_pt))
                except:
                    print "Enter a valid integer"
                    inner()
            inner()
    except:
        print "Enter a valid integer"
        main()

if __name__ == '__main__':
    main()

# Output
# Enter number of test cases : a
# Enter a valid integer
# Enter number of test cases : 3
# Enter start point : 3
# Enter end point : 8
# 6
# Enter start point : a
# Enter a valid integer
# Enter start point : 5
# Enter end point : 7
# 4
# Enter start point : 2
# Enter end point : a
# Enter a valid integer
# Enter start point : 2
# Enter end point : 5
# 5

