def verificare(d, sinitiala, sfinale, simbstart, cuvant):

        saux = sinitiala
        st = [simbstart]

        for i in range(len(cuvant)):

            if len(st) != 0 and (cuvant[i],st[-1]) in d[saux].keys():

                aux = d[saux][(cuvant[i],st[-1])]
                saux = aux[1]
                st = st[:-1]

                for j in aux[0]:

                    if j != '#':

                        st.append(j)

            else:
                return 0

        else:

            if len(st) == 0 or saux in sfinale or len(cuvant) and ('#',st[-1]) in d[saux].keys() and d[saux][('#',st[-1])][1] in sfinale:
                return 1

            else:
                return 0


with open('date.txt') as f:
    lstari = f.readline().split()
    d = {}

    for i in lstari:
        d[i] = {}

    sinitiala = f.readline()
    sinitiala = sinitiala.replace("\n", "")
    sfinale = f.readline().split()
    simbstart = f.readline()
    simbstart = simbstart.replace("\n", "")
    x = f.readline().split()

    while x:
        if x[1] not in d[x[0]].keys():
            d[x[0]][(x[1],x[2])] = {}
        d[x[0]][(x[1],x[2])] = [x[3:-1], x[-1]]
        x = f.readline().split()

with open('cuvant.txt') as g:
    cuvant = g.readline()
    print(cuvant)
    print(d)
    ok = verificare(d, sinitiala, sfinale, simbstart, cuvant)
    if(ok):
        print('\nCuvantul "',cuvant,'" este acceptat de automat', sep = '')
    else:
        print('\nCuvantul "',cuvant, '" este respins de automat', sep = '')
