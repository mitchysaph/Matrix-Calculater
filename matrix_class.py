memo={} #matrixの保管場所

class matrix:
    def __init__(self,name,contents,error):
        self.neme=name
        self.contents=contents
        self.IsSquare=bool(len(contents)==len(contents[0]))
        self.error=error

calculate_answer=matrix('calculate_answer',[[]],True)

def times (x,y): #積
    n,m=len(x),len(y[0])
    k,l=len(x[0]),len(y)
    if l!=k:
        print('error!')
        calculate_answer.error=False
        return
    ans=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for h in range(k):
                ans[i][j]+=y[h][j]*x[i][h]
    calculate_answer.contents=ans
    calculate_answer.error=True
    return

def Outpu(x): #出力
    if len(x)==0:
        print('no value to output')
        return
    n=len(x[0])
    for i in x:
        for j in range(n):
            if(j==n-1):
                print(i[j])
            else:
                print(i[j],end=' ')

def plus (x,y): #和
    n,m=len(x),len(y)
    if n!=m:
        print('error!')
        calculate_answer.error=False
        return
    ans=[]
    for i in range(n):
        k,l=len(x[i]),len(y[i])
        if k!=l:
            print('error!')
            calculate_answer.error=False
            return
        dda=[x[i][j]+y[i][j] for j in range(l)]
        ans.append(dda)
    calculate_answer.contents=ans
    calculate_answer.error=True
    return

def mynos (x,y): #差
    n,m=len(x),len(y)
    if n!=m:
        print('error!')
        calculate_answer.error=False
        return
    ans=[]
    for i in range(n):
        k,l=len(x[i]),len(y[i])
        if k!=l:
            print('error!')
            calculate_answer.error=False
            return
        dda=[x[i][j]-y[i][j] for j in range(l)]
        ans.append(dda)
    calculate_answer.contents=ans
    calculate_answer.error=True
    return

def inp(s): #入力
    n=int(input('line?> '))
    if n<1:
        print('Line should be larger than one')
        return
    m=int(input('row?> '))
    if m<1:
        print('Row should be larger than one')
    ans=[]
    for i in range(m):
        hoge=list(map(int,input().split()))
        if len(hoge)!=n:
            print('error!')
            return
        ans.append(hoge)
    memo[s]=matrix(s,ans,True)
    return

def det(n,co,da,ju): #行列式の再帰
    if(co==n-1):
        for i in range(n):
            if ju[i]:
                return da[n-1][i]
    else:
        ans=0
        di=1
        for i in range(n):
            if ju[i]:
                ju[i]=False
                ans+=da[co][i]*di*det(n,co+1,da,ju)
                ju[i]=True
                di=-di
        return ans
            
def det_calculate(x): #行列式の計算
    if x.IsSquare:
        n=len(x.contents)
        ju=[True for i in range(n)]
        print(det(n,0,x.contents,ju))
    else:
        print('{} is not square matrix.'.format(x.name))
    return

def trace (x): #trace
    if x.IsSquare:
        ans=0
        n=len(x.contents)
        for i in range(n):
            ans+=x.contents[i][i]
        print(ans)
    else:
        print('{} is not square matrix.'.format(x.name))

def transposed(x): #転置
    if x.IsSquare:
        calculate_answer.error=False
        return
    else:
        n=len(x.contents)
        ans=[[x.contents[j][i] for j in range(n)] for i in range(n)]
        calculate_answer.contents=ans
        calculate_answer.error=True
        return

#da=[list(map(int,input(i-1).split())) for i in range(3)]
while 1:
    s=input() #コマンドの受け取り
    if s=='end!': #end! 終了
        break
    elif s=='': # コマンドなしの処理
        pass
    elif s[-1]=='=': #X=で文字を置く
        if s[:-1] in memo:
            print('You can not use this name.')
        else:
            inp(s[:-1])
    elif s in memo: #変数の確認表示
        Outpu(memo[s].contents)
    elif s=='det': #行列式
        t=input()
        if t in memo:            
            det_calculate(memo[t])
        else:
            print("don't have {}.".format(t))
    elif s=='trace': #trace
        t=input()
        if t in memo:
            trace(memo[t])
        else:
            print("don't have {}.".format(t))
    else: 
        length=len(s)
        a,b=-1,-1 #a =の位置,b 演算子の位置
        for i in range(length):
            if s[i]=='=':
                a=i
            elif s[i]=='+' or s[i]=='-' or s[i]=='*':
                b=i
        if b<1: #演算子なしの場合
            print('need operater')
        elif a>=b: #=と演算子の位置が逆
            print('correct order')
        elif a<0: # =なしの場合
            if not(s[:b] in memo):
                print("don't have {}".format(s[:b]))
            elif not(s[b+1:] in memo):
                print("don't have {}".format(s[b+1:]))
            else:
                if s[b]=='+':
                    plus(memo[s[:b]].contents,memo[s[b+1:]].contents)
                elif s[b]=='-':
                    mynos(memo[s[:b]].contents,memo[s[b+1:]].contents)
                elif s[b]=='*':
                    times(memo[s[:b]].contents,memo[s[b+1:]].contents)
                if calculate_answer.error:
                    Outpu(calculate_answer.contents)
        else: #=ありの場合
            if not(s[a+1:b] in memo):
                print("don't have {}".format(s[a+1:b]))
            elif not(s[b+1:] in memo):
                print("don't have {}".format(s[b+1:]))
            elif a==0:
                print('need name before =')
            else:
                if s[b]=='+':
                    plus(memo[s[a+1:b]].contents,memo[s[b+1:]].contents)
                elif s[b]=='-':
                    mynos(memo[s[a+1:b]].contents,memo[s[b+1:]].contents)
                elif s[b]=='*':
                    times(memo[s[a+1:b]].contents,memo[s[b+1:]].contents)
                if calculate_answer.error:
                    memo[s[:a]]=matrix(s[:a],calculate_answer.contents,True)
                    calculate_answer.contents=[[]]
    print()
