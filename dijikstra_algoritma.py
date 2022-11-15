graph = {
    'a':{'b':18,'c':17,'f':20},
    'b':{'d':2,'f':8,'a':18},
    'c':{'e':8,'f':9,'a':17},
    'd':{'b':2,'f':4,'k':10,'l':5},
    'e':{'c':8,'f':6,'g':4,'h':12},
    'f':{'a':20,'b':8,'c':9,'d':4,'e':6,'g':2,'j':2,'k':3},
    'g':{'e':4,'f':2,'h':3,'i':3,'j':4},
    'h':{'e':12,'g':3,'i':4,'m':6},
    'i':{'g':3,'h':4,'j':4,'m':2,'r':9},
    'j':{'f':2,'g':4,'i':4,'k':5,'n':4,'r':6},
    'k':{'d':10,'f':3,'j':5,'n':6,'o':2,'p':10},
    'l':{'d':5,'k':6,'p':8},
    'm':{'h':6,'i':2,'r':7,'v':10},
    'n':{'k':6,'j':4,'o':4,'q':5,'r':5,'s':7},
    'o':{'k':2,'n':4,'p':5,'q':2},
    'p':{'k':10,'l':8,'o':5,'q':6,'t':4,'u':7},
    'q':{'n':5,'o':2,'p':6,'s':6,'t':2},
    'r':{'i':9,'j':6,'m':7,'n':5,'s':6,'v':5,'w':4},
    's':{'n':7,'q':6,'r':6,'w':5,'x':3},
    't':{'p':6,'q':2,'u':5,'x':6},
    'u':{'p':7,'t':5,'x':6,'y':5},
    'v':{'m':10,'r':5,'w':3},
    'w':{'r':4,'s':5,'v':3,'x':7,'y':10},
    'x':{'s':3,'t':6,'u':6,'w':7,'y':4},
    'y':{'u':5,'w':10,'x':4}
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
        print('jarak terpendek adalah '+ str(jarak_terpendek[akhir]*1)+'km')
        print('lintasan adalah' + str(track_lintasan))

#Pengaturan Perhitungan Jarak
# A = titik Awal
# Y = titik Tujuan
dijkstra(graph,'a','y')  # hasil pada TERMINAL



