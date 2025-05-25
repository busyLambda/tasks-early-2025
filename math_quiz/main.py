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

    # 5. feladat
    #
    # A = asztal
    # T = teknős
    # C = cica
    #
    # 2A + 1T + 1C = 170cm + 1C + 1T 130 + C + 170 + T = 2A + M + T 300 = 2A
    #
    # A = 150cm
    print("5.: 150")

    # 6. feladat
    #
    # K = kutya
    # C = cica
    # P = patkány
    #
    # 10 + 20 + 24 = 2C + 2K + 2P 54 = 2 ∗ (M + K + P)
    #
    # M + K + P = 27kg
    print("6.: 27")

    # 7. feladat
    # E = esély
    # N = egyik sem nyer
    #
    # N = (5/6) * (5/6) = 25/36
    #
    # P = (1/6) + (25/36) * P
    # P = (6/11)
    print(f"7.: {6/11}")

if __name__ == '__main__':
    main()
