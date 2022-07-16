a = 1+2
print(a)
print(a + 10)

for a in range(1,10,2):
    print("python")

a = int(input("값을 입력하세요"))
print("a")

a= int(input("번호를 입력하세요"))
if(a < 2):
    print("작음")

def my_sum(x,y):
    return x+y
print(my_sum(10,2))

import pandas as pd
t = pd.Series(range(10,14),index=['서울', '부산', '대구', '광주'])
print(t)

#PANDAS 적용해야 가능
import pandas as pd
titanic_df=pd.read_csv('C:\data/train.csv')
print(titanic_df)
print(titanic_df.head(3)) #위에서 끊는다
print(titanic_df.tail(3)) #아래에서 끊는다
print(titanic_df.info()) #총 데이터 건수, 데이터 타입, Null 건수에 대한 정보를 보여줌
print(titanic_df.describe()) #칼럼별 숫자형 데이터 값의 n-percentile 분포도, 평균값, 최대값, 최소값을 나타낸다.
value_counts=titanic_df['Survived'].value_counts() #해당 Survived의 유형과 건수를 확인할 수 있다. 데이터의 빈도를 확인하는 데 유용한 함수
print(value_counts)
print(titanic_df.sort_values('Fare',ascending=False)) #요금 기준으로 내림차순 정렬
print(titanic_df.sort_values('Fare')) #오름차순
import pandas as pd
titanic_df=pd.read_csv('C:\data/train.csv')
titanic_df['Age_0']=0
print(titanic_df)
titanic_df['Age_by_10']=titanic_df['Age']*10
print(titanic_df.head(3))
#데이터 삭제 = DataFrame.drop(labels=None, axis=0, index=None, columns=None, inplace=False, errors='raise')
titanic_df.drop(['Age_0'],axis=1,inplace=True)
print(titanic_df.columns)
#axis: 값에 따라서 특정 칼럼 또는 특정 행을 드롭

#데이터 셀렉션 및 필터링
print(titanic_df[titanic_df['Pclass']==3].head(3))
titanic_df[['Age', 'Fare']].mean()
print(titanic_df.count())

titanic_grby=titanic_df.groupby(by='Pclass')
print(titanic_grby.count())
print(titanic_grby.sum())

import pandas as pd
import seaborn as sns
import numpy as nuumpy
import matplotlib.pyplot as plt
titanic_df=pd.read_csv('C:\data/train.csv')
#sns.countplot(x='Pclass', hue='Sex', data=titanic_df)
sns.heatmap(data=titanic_df.corr(),annot=True,cmap='Blues')
plt.show()