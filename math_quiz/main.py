print('1.:')

def main() -> None:
    # 1. feladat
    # (R-1)^2+(R-2)^2   = R^2
    # R^2-2R+1+R^2-4R+4 = R^2
    # R^2-6R+5          = 0
    #
    # R1,2 = 6+-sqrt(36-20)/2 = 5(✓), 1(✕ Nem lehetséges: R >= 2)
    print("1.: 5")

    # 2. feladat
    # (1/(sqrt(1)+sqrt(2)))+(1/(sqrt(2)+sqrt(3)))+(1/(sqrt(3)+sqrt(4)))+...+(1/(sqrt(99)+sqrt(100)))
    #
    # (1/(sqrt(2)+sqrt(1)))+(1/(sqrt(3)+sqrt(2)))+(1/(sqrt(4)+sqrt(3)))+...+(1/(sqrt(100)+sqrt(99)))
    #
    # (( ( sqrt(2)-sqrt(1) ) / ((sqrt(2)+sqrt(1)) * (sqrt(2)-sqrt(1)) ) )+
    # ( ( sqrt(3)-sqrt(2) ) / ((sqrt(3)+sqrt(2)) * (sqrt(3)-sqrt(2)) ) )+
    # ( ( sqrt(4)-sqrt(3) ) / ((sqrt(4)+sqrt(3)) * (sqrt(4)-sqrt(3)) ) )+
    # ...+
    # ( ( sqrt(100)-sqrt(99) ) / ((sqrt(100)+sqrt(99)) * (sqrt(100)-sqrt(99)) ) )
    #
    # sqrt(100) - sqrt(1) = 10 - 1 = 9
    print("3.: 9")

if __name__ == '__main__':
    main()
