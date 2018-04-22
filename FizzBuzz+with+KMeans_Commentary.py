import numpy as np                 #数値計算モジュール
from sklearn.cluster import KMeans #機械学習モジュール
#========================================================================================================================#
palameter = 6 #array_A・array_Bの要素数は１５。(３と５の公倍数[FizzBuzz])×"palameter"
#--------------------------------------------------------------------------------#
array_A=np.tile([0,0,1],palameter*5)     #３の倍数[Fizz]にフラグを立てていく。
array_B=np.tile([0,0,0,0,1],palameter*3) #５の倍数[Buzz]にフラグを立てていく。
#--------------------------------------------------------------------------------#
array_X=np.array([array_A,array_B])      #array_Aとarray_Bを結合。
array_Y=array_X.T                        #array_Xを転置、これにて準備完了。
#--------------------------------------------------------------------------------#
array_V=KMeans(n_clusters=4,n_jobs=-1).fit_predict(array_Y) #KMeansを使用して４つのクラスターに分けた結果をarray_Vに代入。
#========================================================================================================================#
for temp in array_V:           #array_Vのすべての要素に対して実行する。
    if temp == array_V[2]:     #取り出された要素が、２番目と同じならば、
        print('Fizz')          #Fizzを出力。
    elif  temp == array_V[4]:  #５番目と同じならば、
        print('Buzz')          #Buzzを出力。
    elif  temp == array_V[14]: #１５番目と同じならば、
        print('FizzBuzz')      #FizzBuzzを出力。
    else:                      #３・５・１５番目と同じでなければ、
        print(0)               #０を出力。