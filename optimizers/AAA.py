
from solution import solution
import numpy
import random
import math
import time



#def AAA(objf,lb,ub,dim,SearchAgents_no,Max_iter):
def AAA(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    iter=Max_iter
    Max_iter = Max_iter * SearchAgents_no
    # Max_iter=1000
    # SearchAgents_no=40
    # dim=30
    # lb=-100
    # ub=100
    #print(dim,lb,ub)
    k = 2               # kesme kuvveti
    le = 0.3            # energy loss paramtresi
    ap = 0.5            # adaptasyon sabiti original 0.5
    #print(dim,lb,ub)
    say = 0

    # popülasyon açlık matrisi başlangıçta hepsi 0
    starveAlg=numpy.zeros(SearchAgents_no,'int')

    # popülasyonun büyüklük dizisi
    algBuyuklukMatrisi=numpy.ones(SearchAgents_no)


    ALG = numpy.random.uniform(0, 1, (SearchAgents_no, dim)) * (ub - lb) + lb


    # popülasyonun fitness değerlerinin tutulduğu dizi
    fitnesslar = numpy.zeros(SearchAgents_no)

    for i in range(0,SearchAgents_no):
        fitnesslar[i] = objf(ALG[i,:])


    minfit = min(fitnesslar)
    minfitindis= numpy.argmin(fitnesslar)

    eniyiALG = ALG[minfitindis,:].copy()
    #print(eniyiALG)
    eniyiFit = minfit
    #print(minfitindis,minfit)

    BuyuklukHesapla(algBuyuklukMatrisi,fitnesslar.copy())


    # Initialize convergence
    convergence_curve = numpy.zeros(iter)
    ############################

    s = solution()

    print("AAA is optimizing  \"" + objf.__name__ + "\"")

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    ############################


    c=SearchAgents_no
    #print(['At iteration ' + str(c/SearchAgents_no) + ' the best fitness is ' + str(eniyiFit)])

    convergence_curve[0] = eniyiFit
    t=1

    #Max_iter = Max_iter * SearchAgents_no
    #Max_iter =150000
    while c < Max_iter:


         Enerji = EnerjiHesapla(algBuyuklukMatrisi.copy())
         AlgSurtunme = SurtunmeHesapla(algBuyuklukMatrisi.copy())
         #print('enerji',Enerji)
         #print('sürtünme',AlgSurtunme)
         for i in range(SearchAgents_no):

             istarve = 0

             while(Enerji[i] >= 0 and c < Max_iter):

                 Komsu=TurnuvaSecimi(fitnesslar.copy())         #   Neigbour 1 ile 40 arasında bir tam sayı komşu alg

                 while Komsu==i :
                     Komsu=TurnuvaSecimi(fitnesslar)

                 boyut1=random.randint(0,dim-1)
                 boyut2=random.randint(0,dim-1)
                 boyut3=random.randint(0,dim-1)
                 while(boyut1 == boyut2 or boyut1 == boyut3 or boyut2==boyut3):
                     boyut2=random.randint(0,dim-1)
                     boyut3=random.randint(0,dim-1)

                 yeniAlg=ALG[i,:].copy()


                 yeniAlg[boyut1] = yeniAlg[boyut1] + (ALG[Komsu, boyut1] - yeniAlg[boyut1]) * (k - AlgSurtunme[i]) * ((random.random() - 0.5) * 2)
                 yeniAlg[boyut2] = yeniAlg[boyut2] + (ALG[Komsu, boyut2] - yeniAlg[boyut2]) * (k - AlgSurtunme[i]) *  math.cos(random.random() * 360)
                 yeniAlg[boyut3] = yeniAlg[boyut3] + (ALG[Komsu, boyut3] - yeniAlg[boyut3]) * (k - AlgSurtunme[i]) *  math.sin(random.random() * 360)

                 yeniAlg = numpy.clip(yeniAlg, lb, ub)


                 yeniAlgfitness = objf(yeniAlg)


                 Enerji[i] = Enerji[i] - le/2



                 if( yeniAlgfitness <= fitnesslar[i] ):
                     ALG[i,:] = yeniAlg.copy()
                     fitnesslar[i] = yeniAlgfitness
                     istarve = 1

                 else:
                     Enerji[i] = Enerji[i] - le/2



                 deger = min(fitnesslar)
                 index = numpy.argmin(fitnesslar)
                 if deger < eniyiFit:
                     eniyiFit = deger
                     eniyiALG = ALG[index, :].copy()

                 c=c+1

                 if (c % SearchAgents_no == 0):
                     #print(['At iteration ' + str(c/SearchAgents_no) + ' the best fitness is ' + str(eniyiFit)])
                     convergence_curve[t] = eniyiFit
                     t = t + 1



             if istarve==0:
                starveAlg[i]= starveAlg[i] + 1


             # deger = min(fitnesslar)
             # index = numpy.argmin(fitnesslar)
             # if deger < eniyiFit:
             #     eniyiFit = deger
             #     eniyiALG = ALG[index, :].copy()
             #     #print("en iyi fitness  ajan no ",i,":",deger,'iterasyon',c/40)

         ############################################################






         #Evrimsel Süreç-----#Evrimsel Süreç-----#Evrimsel Süreç-----#Evrimsel Süreç-----

         BuyuklukHesapla(algBuyuklukMatrisi, fitnesslar.copy())
         randboyut=random.randint(0,dim-1)

         minindis = numpy.argmin(algBuyuklukMatrisi)
         maxindis = numpy.argmax(algBuyuklukMatrisi)

         ALG[minindis,randboyut] = ALG[maxindis,randboyut]

         #Evrimsel süreç biter#   #Evrimsel süreç biter##   #Evrimsel süreç biter##





         #Adaptasyon işlemi --  #Adaptasyon işlemi --#Adaptasyon işlemi --#Adaptasyon işlemi --

         indis3 = numpy.argmax(starveAlg)
         if random.random() < ap :
             for i in range(dim):
                 ALG[indis3, i] = ALG[indis3, i] +  ( eniyiALG[i] - ALG[indis3,i] ) * random.random()
                 say= say + 1



         # Adaptasyon işlemi biter-- # Adaptasyon işlemi biter-- # Adaptasyon işlemi biter--

         if (c % Max_iter == 0):
              print(['At iteration ' + str(c) + ' the best fitness is ' + str(eniyiFit)])

    #convergence_curve[t] = eniyiFit
    #print("sad",eniyiFit)
    #print(say)

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.optimizer = "AAA"
    s.objfname = objf.__name__
    s.bestIndividual = eniyiALG


    return s










#BigX=CalculateGreatness(BigX,ObjX)
def BuyuklukHesapla(buyukluk, fitnesslar1):

    maxdeg = max(fitnesslar1)
    mindeg = min(fitnesslar1)

    for i in range(len(fitnesslar1)):
        fitnesslar1[i] = (fitnesslar1[i]-mindeg)  /  (maxdeg-mindeg)  #normalizasyon
        fitnesslar1[i] = 1 - fitnesslar1[i]  # fitness min yapamaya calıstıgımız icin 1 den cıkarıyoruz


    for i in range(len(buyukluk)):
        fKs = abs(buyukluk[i] / 2 )     #yarı doygunluk sabiti
        M = fitnesslar1[i] / (fKs + fitnesslar1[i])
        dX = M * buyukluk[i]            #büyüme oranı
        buyukluk[i] = buyukluk[i] + dX  #yeni büyüklük hesabı





#function fGreatYuzey=GreatnessOrder(fBig)
def EnerjiHesapla(buyukluk):

    siralama = numpy.ones(len(buyukluk),'int')
    fGreatYuzey = numpy.zeros(len(buyukluk))

    for i in range(0,len(buyukluk)):
        siralama[i] = i


    for i in range(len(buyukluk)-1):
        for j in range(i+1,len(buyukluk)):
            if(buyukluk[siralama[i]] > buyukluk[siralama[j]]):
                siralama[i] ,siralama[j] = siralama[j], siralama[i]
        fGreatYuzey[siralama[i]] = i**2

    fGreatYuzey[siralama[len(buyukluk)-1]] = (i+1)**2
    maxdeg = max(fGreatYuzey)
    mindeg = min(fGreatYuzey)

    for i in range(len(fGreatYuzey)):
        fGreatYuzey[i] = (fGreatYuzey[i] - mindeg) / (maxdeg - mindeg)

    return fGreatYuzey





#FrictionSurface
def SurtunmeHesapla(algBuyuklukMatrisi):

    fGreatYuzey=numpy.zeros(len(algBuyuklukMatrisi))
    for i in range(len(algBuyuklukMatrisi)):
        r = ((algBuyuklukMatrisi[i] * 3) / (4* math.pi)) ** (1/3)
        fGreatYuzey[i] = 2 * math.pi * (r**2)

    maxdeg = max(fGreatYuzey)
    mindeg =  min(fGreatYuzey)
    #print('max,min, fgreatyuzey:', maxdeg, mindeg, fGreatYuzey)

    for i in range(len(fGreatYuzey)):
        fGreatYuzey[i] = (fGreatYuzey[i]-mindeg)  /  (maxdeg-mindeg)

    return fGreatYuzey






def TurnuvaSecimi(fitnesslar):

    birey1=random.randint(0,len(fitnesslar)-1)
    birey2=random.randint(0,len(fitnesslar)-1)

    while birey1==birey2:
        birey2=random.randint(0,len(fitnesslar)-1)

    if (fitnesslar[birey1] < fitnesslar[birey2]):
        return birey1
    else:
        return birey2



