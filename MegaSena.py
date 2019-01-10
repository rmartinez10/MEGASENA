#===============<<<    IMPORTS   >>>==================#
import csv 
import numpy as np

arquivo = csv.reader(open("arqmegacsv.csv"),delimiter=';')

print(' inicio do programa')
#===============<<<    VARIAVEIS DE TRABALHO   >>>==================#
count_num01 = 0
count_num02 = 0
count_num03 = 0
count_num04 = 0
count_num05 = 0
count_num06 = 0
count_num07 = 0
count_num08 = 0
count_num09 = 0
count_num10 = 0
count_num11 = 0
count_num12 = 0
count_num13 = 0
count_num14 = 0
count_num15 = 0
count_num16 = 0
count_num17 = 0
count_num18 = 0
count_num19 = 0
count_num20 = 0
count_num21 = 0
count_num22 = 0
count_num23 = 0
count_num24 = 0
count_num25 = 0
count_num26 = 0
count_num27 = 0
count_num28 = 0
count_num29 = 0
count_num30 = 0
count_num31 = 0
count_num32 = 0
count_num33 = 0
count_num34 = 0
count_num35 = 0
count_num36 = 0
count_num37 = 0
count_num38 = 0
count_num39 = 0
count_num40 = 0
count_num41 = 0
count_num42 = 0
count_num43 = 0
count_num44 = 0
count_num45 = 0
count_num46 = 0
count_num47 = 0
count_num48 = 0
count_num49 = 0
count_num50 = 0
count_num51 = 0
count_num52 = 0
count_num53 = 0
count_num54 = 0
count_num55 = 0
count_num56 = 0
count_num57 = 0
count_num58 = 0
count_num59 = 0
count_num60 = 0
line_count  = 0

from datetime import date
Dataatu     = date.today()
Datatexto   = '{}.{}.{}'.format(Dataatu.day,Dataatu.month,Dataatu.year)
#===============<<<    FIM VARIAVEIS DE TRABALHO   >>>==================#
for [dez1,dez2,dez3,dez4,dez5,dez6] in arquivo:
    line_count += 1
    if (dez1 == '1') or (dez2 == '1') or (dez3 == '1') or (dez4 == '1') or (dez5 == '1') or (dez6 == '1'):
        count_num01 += 1
        num_sorteio = dez1
    if (dez1 == '2') or (dez2 == '2') or (dez3 == '2') or (dez4 == '2') or (dez5 == '2') or (dez6 == '2'):
        count_num02 += 1        
    if (dez1 == '3') or (dez2 == '3') or (dez3 == '3') or (dez4 == '3') or (dez5 == '3') or (dez6 == '3'):
        count_num03 += 1        
    if (dez1 == '4') or (dez2 == '4') or (dez3 == '4') or (dez4 == '4') or (dez5 == '4') or (dez6 == '4'):
        count_num04 += 1                                                                                  
    if (dez1 == '5') or (dez2 == '5') or (dez3 == '5') or (dez4 == '5') or (dez5 == '5') or (dez6 == '5'):
        count_num05 += 1                                                                                  
    if (dez1 == '6') or (dez2 == '6') or (dez3 == '6') or (dez4 == '6') or (dez5 == '6') or (dez6 == '6'):
        count_num06 += 1                                                                                  
    if (dez1 == '7') or (dez2 == '7') or (dez3 == '7') or (dez4 == '7') or (dez5 == '7') or (dez6 == '7'):
        count_num07 += 1                                                                                  
    if (dez1 == '8') or (dez2 == '8') or (dez3 == '8') or (dez4 == '8') or (dez5 == '8') or (dez6 == '8'):      
        count_num08 += 1                                                                                        
    if (dez1 == '9') or (dez2 == '9') or (dez3 == '9') or (dez4 == '9') or (dez5 == '9') or (dez6 == '9'):      
        count_num09 += 1                                                                                        
    if (dez1 == '10') or (dez2 == '10') or (dez3 == '10') or (dez4 == '10') or (dez5 == '10') or (dez6 == '10'):
        count_num10 += 1                                                                                        
    if (dez1 == '11') or (dez2 == '11') or (dez3 == '11') or (dez4 == '11') or (dez5 == '11') or (dez6 == '11'):
        count_num11 += 1                                                                                        
    if (dez1 == '12') or (dez2 == '12') or (dez3 == '12') or (dez4 == '12') or (dez5 == '12') or (dez6 == '12'):
        count_num12 += 1                                                                                        
    if (dez1 == '13') or (dez2 == '13') or (dez3 == '13') or (dez4 == '13') or (dez5 == '13') or (dez6 == '13'):
        count_num13 += 1                                                                                        
    if (dez1 == '14') or (dez2 == '14') or (dez3 == '14') or (dez4 == '14') or (dez5 == '14') or (dez6 == '14'):
        count_num14 += 1                                                                                        
    if (dez1 == '15') or (dez2 == '15') or (dez3 == '15') or (dez4 == '15') or (dez5 == '15') or (dez6 == '15'):
        count_num15 += 1                                                                                        
    if (dez1 == '16') or (dez2 == '16') or (dez3 == '16') or (dez4 == '16') or (dez5 == '16') or (dez6 == '16'):
        count_num16 += 1                                                                                        
    if (dez1 == '17') or (dez2 == '17') or (dez3 == '17') or (dez4 == '17') or (dez5 == '17') or (dez6 == '17'):
        count_num17 += 1                                                                                        
    if (dez1 == '18') or (dez2 == '18') or (dez3 == '18') or (dez4 == '18') or (dez5 == '18') or (dez6 == '18'):
        count_num18 += 1                                                                                        
    if (dez1 == '19') or (dez2 == '19') or (dez3 == '19') or (dez4 == '19') or (dez5 == '19') or (dez6 == '19'):
        count_num19 += 1                                                                                        
    if (dez1 == '20') or (dez2 == '20') or (dez3 == '20') or (dez4 == '20') or (dez5 == '20') or (dez6 == '20'):
        count_num20 += 1  
    if (dez1 == '21') or (dez2 == '21') or (dez3 == '21') or (dez4 == '21') or (dez5 == '21') or (dez6 == '21'):
        count_num21 += 1                                                                                        
    if (dez1 == '22') or (dez2 == '22') or (dez3 == '22') or (dez4 == '22') or (dez5 == '22') or (dez6 == '22'):
        count_num22 += 1                                                                                        
    if (dez1 == '23') or (dez2 == '23') or (dez3 == '23') or (dez4 == '23') or (dez5 == '23') or (dez6 == '23'):
        count_num23 += 1                                                                                        
    if (dez1 == '24') or (dez2 == '24') or (dez3 == '24') or (dez4 == '24') or (dez5 == '24') or (dez6 == '24'):
        count_num24 += 1                                                                                        
    if (dez1 == '25') or (dez2 == '25') or (dez3 == '25') or (dez4 == '25') or (dez5 == '25') or (dez6 == '25'):
        count_num25 += 1                                                                                        
    if (dez1 == '26') or (dez2 == '26') or (dez3 == '26') or (dez4 == '26') or (dez5 == '26') or (dez6 == '26'):
        count_num26 += 1                                                                                        
    if (dez1 == '27') or (dez2 == '27') or (dez3 == '27') or (dez4 == '27') or (dez5 == '27') or (dez6 == '27'):
        count_num27 += 1                                                                                        
    if (dez1 == '28') or (dez2 == '28') or (dez3 == '28') or (dez4 == '28') or (dez5 == '28') or (dez6 == '28'):
        count_num28 += 1                                                                                        
    if (dez1 == '29') or (dez2 == '29') or (dez3 == '29') or (dez4 == '29') or (dez5 == '29') or (dez6 == '29'):
        count_num29 += 1                                                                                        
    if (dez1 == '30') or (dez2 == '30') or (dez3 == '30') or (dez4 == '30') or (dez5 == '30') or (dez6 == '30'):
        count_num30 += 1                                                                                        
    if (dez1 == '31') or (dez2 == '31') or (dez3 == '31') or (dez4 == '31') or (dez5 == '31') or (dez6 == '31'):
        count_num31 += 1                                                                                        
    if (dez1 == '32') or (dez2 == '32') or (dez3 == '32') or (dez4 == '32') or (dez5 == '32') or (dez6 == '32'):
        count_num32 += 1                                                                                        
    if (dez1 == '33') or (dez2 == '33') or (dez3 == '33') or (dez4 == '33') or (dez5 == '33') or (dez6 == '33'):
        count_num33 += 1                                                                                        
    if (dez1 == '34') or (dez2 == '34') or (dez3 == '34') or (dez4 == '34') or (dez5 == '34') or (dez6 == '34'):
        count_num34 += 1                                                                                        
    if (dez1 == '35') or (dez2 == '35') or (dez3 == '35') or (dez4 == '35') or (dez5 == '35') or (dez6 == '35'):
        count_num35 += 1                                                                                        
    if (dez1 == '36') or (dez2 == '36') or (dez3 == '36') or (dez4 == '36') or (dez5 == '36') or (dez6 == '36'):
        count_num36 += 1                                                                                        
    if (dez1 == '37') or (dez2 == '37') or (dez3 == '37') or (dez4 == '37') or (dez5 == '37') or (dez6 == '37'):
        count_num37 += 1                                                                                        
    if (dez1 == '38') or (dez2 == '38') or (dez3 == '38') or (dez4 == '38') or (dez5 == '38') or (dez6 == '38'):
        count_num38 += 1                                                                                        
    if (dez1 == '39') or (dez2 == '39') or (dez3 == '39') or (dez4 == '39') or (dez5 == '39') or (dez6 == '39'):
        count_num39 += 1                                                                                        
    if (dez1 == '40') or (dez2 == '40') or (dez3 == '40') or (dez4 == '40') or (dez5 == '40') or (dez6 == '40'):
        count_num40 += 1                                                                                        
    if (dez1 == '41') or (dez2 == '41') or (dez3 == '41') or (dez4 == '41') or (dez5 == '41') or (dez6 == '41'):
        count_num41 += 1                                                                                        
    if (dez1 == '42') or (dez2 == '42') or (dez3 == '42') or (dez4 == '42') or (dez5 == '42') or (dez6 == '42'):
        count_num42 += 1                                                                                        
    if (dez1 == '43') or (dez2 == '43') or (dez3 == '43') or (dez4 == '43') or (dez5 == '43') or (dez6 == '43'):
        count_num43 += 1                                                                                        
    if (dez1 == '44') or (dez2 == '44') or (dez3 == '44') or (dez4 == '44') or (dez5 == '44') or (dez6 == '44'): 
        count_num44 += 1                                                                                        
    if (dez1 == '45') or (dez2 == '45') or (dez3 == '45') or (dez4 == '45') or (dez5 == '45') or (dez6 == '45'):
        count_num45 += 1                                                                                        
    if (dez1 == '46') or (dez2 == '46') or (dez3 == '46') or (dez4 == '46') or (dez5 == '46') or (dez6 == '46'):
        count_num46 += 1                                                                                        
    if (dez1 == '47') or (dez2 == '47') or (dez3 == '47') or (dez4 == '47') or (dez5 == '47') or (dez6 == '47'):
        count_num47 += 1                                                                                        
    if (dez1 == '48') or (dez2 == '48') or (dez3 == '48') or (dez4 == '48') or (dez5 == '48') or (dez6 == '48'):
        count_num48 += 1                                                                                        
    if (dez1 == '49') or (dez2 == '49') or (dez3 == '49') or (dez4 == '49') or (dez5 == '49') or (dez6 == '49'):
        count_num49 += 1                                                                                        
    if (dez1 == '50') or (dez2 == '50') or (dez3 == '50') or (dez4 == '50') or (dez5 == '50') or (dez6 == '50'):
        count_num50 += 1      
    if (dez1 == '51') or (dez2 == '51') or (dez3 == '51') or (dez4 == '51') or (dez5 == '51') or (dez6 == '51'):
        count_num51 += 1                                                                                        
    if (dez1 == '52') or (dez2 == '52') or (dez3 == '52') or (dez4 == '52') or (dez5 == '52') or (dez6 == '52'):
        count_num52 += 1                                                                                        
    if (dez1 == '53') or (dez2 == '53') or (dez3 == '53') or (dez4 == '53') or (dez5 == '53') or (dez6 == '53'):
        count_num53 += 1                                                                                        
    if (dez1 == '54') or (dez2 == '54') or (dez3 == '54') or (dez4 == '54') or (dez5 == '54') or (dez6 == '54'):
        count_num54 += 1                                                                                        
    if (dez1 == '55') or (dez2 == '55') or (dez3 == '55') or (dez4 == '55') or (dez5 == '55') or (dez6 == '55'):
        count_num55 += 1                                                                                        
    if (dez1 == '56') or (dez2 == '56') or (dez3 == '56') or (dez4 == '56') or (dez5 == '56') or (dez6 == '56'):
        count_num56 += 1                                                                                        
    if (dez1 == '57') or (dez2 == '57') or (dez3 == '57') or (dez4 == '57') or (dez5 == '57') or (dez6 == '57'):
        count_num57 += 1                                                                                        
    if (dez1 == '58') or (dez2 == '58') or (dez3 == '58') or (dez4 == '58') or (dez5 == '58') or (dez6 == '58'):
        count_num58 += 1                                                                                        
    if (dez1 == '59') or (dez2 == '59') or (dez3 == '59') or (dez4 == '59') or (dez5 == '59') or (dez6 == '59'):
        count_num59 += 1                                                                                        
    if (dez1 == '60') or (dez2 == '60') or (dez3 == '60') or (dez4 == '60') or (dez5 == '60') or (dez6 == '60'):
        count_num60 += 1  

print ('----------------------------------------------------------------')
print ('-------------------<<    E X T R A T O    >>>-------------------')
print ('----------------------------------------------------------------')
print ('data.........................: ', Datatexto                      )
print ('Total de linhas no arquivo...: ', line_count                     )
print ('----------------------------------------------------------------')
print ('----------------------------------------------------------------') 

numeros = [ [0,1],[1,2],[2,3],[3,4],[4,5] ,[5,6] ,[6,7] ,[7,8] ,[8,9] ,[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],[17,18]
,[18,19],[19,20],[20,21],[21,22],[22,23],[23,24],[24,25],[25,26],[26,27],[27,28],[28,29],[29,30],[30,31],[31,32],[32,33],[33,34],[34,35]
,[35,36],[36,37],[37,38],[38,39],[39,40],[40,41],[41,42],[42,43],[43,44],[44,45],[45,46],[46,47],[47,48],[48,49],[49,50],[50,51],[51,52]
,[52,53],[53,54],[54,55],[55,56],[56,57],[57,58],[58,59],[59,60]  ]

numeros[0][0] = count_num01 
numeros[1][0] = count_num02 
numeros[2][0] = count_num03 
numeros[3][0] = count_num04 
numeros[4][0] = count_num05 
numeros[5][0] = count_num06 
numeros[6][0] = count_num07 
numeros[7][0] = count_num08 
numeros[8][0] = count_num09 
numeros[9][0] = count_num10 
numeros[10][0] = count_num11
numeros[11][0] = count_num12
numeros[12][0] = count_num13
numeros[13][0] = count_num14
numeros[14][0] = count_num15
numeros[15][0] = count_num16
numeros[16][0] = count_num17
numeros[17][0] = count_num18
numeros[18][0] = count_num19
numeros[19][0] = count_num20
numeros[20][0] = count_num21
numeros[21][0] = count_num22
numeros[22][0] = count_num23
numeros[23][0] = count_num24
numeros[24][0] = count_num25
numeros[25][0] = count_num26
numeros[26][0] = count_num27
numeros[27][0] = count_num28
numeros[28][0] = count_num29
numeros[29][0] = count_num30
numeros[30][0] = count_num31
numeros[31][0] = count_num32
numeros[32][0] = count_num33
numeros[33][0] = count_num34
numeros[34][0] = count_num35
numeros[35][0] = count_num36
numeros[36][0] = count_num37
numeros[37][0] = count_num38
numeros[38][0] = count_num39
numeros[39][0] = count_num40
numeros[40][0] = count_num41
numeros[41][0] = count_num42
numeros[42][0] = count_num43
numeros[43][0] = count_num44
numeros[44][0] = count_num45
numeros[45][0] = count_num46
numeros[46][0] = count_num47
numeros[47][0] = count_num48
numeros[48][0] = count_num49
numeros[49][0] = count_num50
numeros[50][0] = count_num51
numeros[51][0] = count_num52
numeros[52][0] = count_num53
numeros[53][0] = count_num54
numeros[54][0] = count_num55
numeros[55][0] = count_num56
numeros[56][0] = count_num57
numeros[57][0] = count_num58
numeros[58][0] = count_num59
numeros[59][0] = count_num60

print('lista  desordenada: ',numeros)          
numeros.sort()
print (' ') 
print('lista ordenada....: ',numeros)
print ('-----------------------------------------------------') 
print('NUMERO QUE MAIS SAI : ',numeros[59][1], ' e Saiu ',numeros[59][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[58][1], ' e Saiu ',numeros[58][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[57][1], ' e Saiu ',numeros[57][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[56][1], ' e Saiu ',numeros[56][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[55][1], ' e Saiu ',numeros[55][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[54][1], ' e Saiu ',numeros[54][0],'vezes!')
print (' ') 
print('NUMERO QUE MAIS SAI : ',numeros[53][1], ' e Saiu ',numeros[53][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[52][1], ' e Saiu ',numeros[52][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[51][1], ' e Saiu ',numeros[51][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[50][1], ' e Saiu ',numeros[50][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[49][1], ' e Saiu ',numeros[49][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[48][1], ' e Saiu ',numeros[48][0],'vezes!')
print (' ') 
print('NUMERO QUE MAIS SAI : ',numeros[47][1], ' e Saiu ',numeros[47][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[46][1], ' e Saiu ',numeros[46][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[45][1], ' e Saiu ',numeros[45][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[44][1], ' e Saiu ',numeros[44][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[43][1], ' e Saiu ',numeros[43][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[42][1], ' e Saiu ',numeros[42][0],'vezes!')
print (' ') 
print('NUMERO QUE MAIS SAI : ',numeros[41][1], ' e Saiu ',numeros[41][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[40][1], ' e Saiu ',numeros[40][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[39][1], ' e Saiu ',numeros[39][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[38][1], ' e Saiu ',numeros[38][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[37][1], ' e Saiu ',numeros[37][0],'vezes!')
print('NUMERO QUE MAIS SAI : ',numeros[36][1], ' e Saiu ',numeros[36][0],'vezes!')
print ('======================================================================= ') 
print('NUMERO QUE MENOS SAI : ',numeros[0][1], ' e Saiu ',numeros[0][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[1][1], ' e Saiu ',numeros[1][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[2][1], ' e Saiu ',numeros[2][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[3][1], ' e Saiu ',numeros[3][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[4][1], ' e Saiu ',numeros[4][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[5][1], ' e Saiu ',numeros[5][0],'vezes!')
print (' ') 
print('NUMERO QUE MENOS SAI : ',numeros[6][1], ' e Saiu ',numeros[6][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[7][1], ' e Saiu ',numeros[7][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[8][1], ' e Saiu ',numeros[8][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[9][1], ' e Saiu ',numeros[9][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[10][1], ' e Saiu ',numeros[10][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[11][1], ' e Saiu ',numeros[11][0],'vezes!')
print (' ') 
print('NUMERO QUE MENOS SAI : ',numeros[12][1], ' e Saiu ',numeros[12][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[13][1], ' e Saiu ',numeros[13][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[14][1], ' e Saiu ',numeros[14][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[15][1], ' e Saiu ',numeros[15][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[16][1], ' e Saiu ',numeros[16][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[17][1], ' e Saiu ',numeros[17][0],'vezes!')
print (' ') 
print('NUMERO QUE MENOS SAI : ',numeros[18][1], ' e Saiu ',numeros[18][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[19][1], ' e Saiu ',numeros[19][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[20][1], ' e Saiu ',numeros[20][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[21][1], ' e Saiu ',numeros[21][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[22][1], ' e Saiu ',numeros[22][0],'vezes!')
print('NUMERO QUE MENOS SAI : ',numeros[23][1], ' e Saiu ',numeros[23][0],'vezes!')
print (' ') 
print ('------------<<<   F I M CLASSE  >>>------------------') 


