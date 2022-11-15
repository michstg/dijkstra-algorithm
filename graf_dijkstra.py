graph = {
    'a':{'b':4},
    'b':{'d':16,'c':7,'f':15,'a':4},
    'c':{'d':13,'b':7},
    'd':{'e':16,'g':10,'b':16,'c':13},
    'e':{'d':16},
    'f':{'g':20,'i':14,'b':15},
    'g':{'h':20,'k':21,'f':20,'d':10},
    'h':{'g':20,'i':14},
    'i':{'j':18,'h':14,'f':14},
    'j':{'i':18,'l':6},
    'k':{'l':5,'g':21},
    'l':{'m':6,'k':5,'j':6},
    'm':{'l':6}
}

def dijkstra(graph,start,akhir):
    jarak_terpendek = { }
    jarak_edge = { }
    titik_verteks = graph
    infinity = 999999
    track_lintasan = [ ]

    for titik in titik_verteks:
        jarak_terpendek[titik]=infinity
    jarak_terpendek[start]=0

    while titik_verteks:
        min_jarak_titik=None
        for titik in titik_verteks:
            if min_jarak_titik is None:
                min_jarak_titik = titik
            elif jarak_terpendek[titik]<jarak_terpendek[min_jarak_titik]:
                min_jarak_titik = titik

        lintasan_options = graph[min_jarak_titik].items()
        for pendek_titik, pengaruh in lintasan_options:

            if pengaruh+jarak_terpendek[min_jarak_titik] < jarak_terpendek[pendek_titik]:
                jarak_terpendek[pendek_titik]=pengaruh+jarak_terpendek[min_jarak_titik]
                jarak_edge[pendek_titik]= min_jarak_titik

        titik_verteks.pop(min_jarak_titik)
    jumlahtitik = akhir

    while jumlahtitik != start:
        try:
            track_lintasan.insert(0,jumlahtitik)
            jumlahtitik=jarak_edge[jumlahtitik]

        except KeyError:
            print('lintasan tidak dijangkau')
            break

    track_lintasan.insert(0,start)


    if jarak_terpendek[start] != infinity:
        print('jarak terpendek adalah '+ str(jarak_terpendek[akhir]*5)+'km')
        print('lintasan adalah' + str(track_lintasan))

#Pengaturan Perhitungan Jarak
# A = titik Awal
# M = titik Tujuan
dijkstra(graph,'f','k')  # hasil pada TERMINAL



