
# coding: utf-8

# In[101]:


import os
import pandas as pd 
import numpy as np 
import scipy.io as sio
import math
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn import model_selection
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import lightgbm as lgb

def starts():

    # In[122]:

    F = open("feature.cfg","r")
    features=int(F.readline())
    FeatureSets= F.read().splitlines()
    F.close()

    # In[124]:


    decisions=[]
    X=[]
    for i in range(len(FeatureSets)):
        if FeatureSets[i][-3:]=="mat":
            mat_contents = sio.loadmat(FeatureSets[i])
            X.append(mat_contents['data'])
            decisions.append([False]*features)
            decisions[i][i]=True
        else:
            x=[]
            for i in FeatureSets[i].split(" "):
                x.append(eval(i))
            decisions.append(x)

        
    if os.path.exists("Results")==False:
        os.mkdir("Results")
        
    parameters=[]
    cv=[]
    s=open('parameter.cfg', 'r')
    for i in s.read().splitlines():
        if i=="SKIP":
            parameters.append(i)
            cv.append(5)
        else:
            i=i.split(' -- ')
            parameters.append(eval(i[0]))
            cv.append(int(i[1]))

    s.close()




    # In[142]:
    for decision in decisions:
        i=-1
        FolderName=''
        for dec in decision:
            i=i+1
            if dec:
                FolderName=FolderName+FeatureSets[i].split('/')[-1][:-4]+'_'
                labels=sio.loadmat(FeatureSets[i])['labels'].reshape(-1)


        if os.path.exists("Results\\"+FolderName)==False:
            os.mkdir("Results\\"+FolderName)

        path="Results\\"+FolderName+"\\"
        print("---------------------------------------")
        print("Creating Results for "+FolderName)


        Xd=np.ndarray(shape=(X[0].shape[0],0))

        i=-1
        for dec in decision:
            i=i+1
            if dec:
                if sum(decision)==1:
                    Xd=np.ndarray(shape=(X[i].shape[0],0))
                Xd=np.concatenate((Xd,X[i]),axis=1)


        df=pd.DataFrame(data = Xd.copy())
        results=pd.DataFrame(columns=["Model","BestScore","BestParameters"])
        print("Number of Features :"+str(df.shape[1]))

        def runmodel(model,parameters,name,cv=5):
            clf=model_selection.GridSearchCV(model,parameters,cv=cv)
            clf.fit(df,labels)

            plt.plot(clf.cv_results_['mean_test_score'])
            plt.title(FolderName[:-1]+"\n"+name+"_"+"MeanTestScore")
            plt.xlabel("Tuning Parameters")
            plt.ylabel("Accuracy")
            plt.savefig(path+name+"_MeanTestScore.png")
            plt.close()
            plt.plot(clf.cv_results_['mean_fit_time'])
            plt.title(FolderName[:-1]+"\n"+name+"_"+"MeanFitTime")  
            plt.xlabel("Tuning Parameters")
            plt.ylabel("Fit Time")
            plt.savefig(path+name+"_MeanFitTime.png")
            plt.close()
            results.loc[name]=[name,clf.best_score_,clf.best_params_]

        #KNN
        if parameters[0]!='SKIP':
            runmodel(neighbors.KNeighborsClassifier(),parameters[0],"KNN",cv[0])
            print("KNN Done for "+FolderName)

        #SVM
        if parameters[1]!='SKIP':
            runmodel(svm.SVC(),parameters[1],"SVM",cv[1])
            print("SVM Done for "+FolderName)
        
        #LogisticRegression
        if parameters[2]!='SKIP':
            runmodel(LogisticRegression(),parameters[2],"LogRegr",cv[2])
            print("LogisticRegression Done for "+FolderName)
        
        #XGBClassifier
        if parameters[3]!='SKIP':
            runmodel(XGBClassifier(),parameters[3],"XGB",cv[3])
            print("XGB Done for "+FolderName)
        
        #LGBClassifier
        if parameters[4]!='SKIP':      
            runmodel(lgb.LGBMClassifier(),parameters[4],"LGB",cv[4])
            print("LGB Done for "+FolderName)
        
        results.to_csv(path+FolderName+".csv",index=False)

    print("-------------------------")    
    print("| All Results Generated |")
    print("-------------------------")    


if __name__ == '__main__':
    starts()