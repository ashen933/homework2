import itertools

ls_point = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]


def lenth(a, b):
    return float(((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5)


def s_path(ls):
    len_path = {}
    start_point = ls[0]
    lsd = ls
    lsp = itertools.permutations(range(1, len(ls)))
    lsp2 = []
    for i in lsp:
        if i[::-1] not in lsp2:
            lsp2.append(i)
    for i in lsp2:
        a = 0
        len1 = 0

        for j in i:
            l = lenth(ls_point[a], ls_point[j])
            len1 += l

            a = j
        len1 += lenth(ls_point[a], ls_point[0])
        len_path[i] = len1
    len1 = 0
    fin = sorted(len_path.items(), key=lambda x: x[1])

    a = 0
    print('({0},{1})'.format(ls_point[a][0], ls_point[a][1]), end=' ')
    for i in fin[0][0]:
        l = lenth(ls_point[a], ls_point[i])
        len1 += l
        print(' = > ({0},{1})[{2}]'.format(ls_point[i][0], ls_point[i][1],
                                           len1),
              end=' ')
        a = i
    len1 += lenth(ls_point[a], ls_point[0])
    print(' = > ({0},{1})[{2}]'.format(ls_point[0][0], ls_point[0][1], len1),
          end=' ')
    return


s_path(ls_point)
