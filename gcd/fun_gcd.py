from matplotlib import pyplot as plt

H_squares = []
new_a_b = []
H_squares = []
def gcd(a, b,H_squares):
    while True:
        H_squares.append([a, b])
        if a == b:
            return a
        b, a = abs(a - b), b





a = 45
b = 17
print(gcd(a, b,H_squares))
print(new_a_b)
c = 0
for i in H_squares:
    high = [0, 0, 1, 1, 0]
    length = [0, 1, 1, 0, 0]
    if i[0] > i[1]:
        high[2], high[3] = i[0], i[0]
        length[1], length[2] = i[1], i[1]
    else:
        high[2], high[3] = i[1], i[1]
        length[1], length[2] = i[0], i[0]
    new_a_b.append([high, length])
    print(new_a_b)
    x = [plt.plot(h[0], h[1]) for h in new_a_b]
    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Square {new_a_b[c][0][2]} x {new_a_b[c][1][2]}')
    plt.grid(False)
    plt.savefig(f'{chr(97 + c)}')
    c += 1
    # plt.show()




