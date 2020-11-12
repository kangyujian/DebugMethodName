import esprima
'''
# 功能：
1.将提取出来的函数体转化为token流
2.将tokens流写入文件
# 格式
项目名@包名@类名@方法名@方法体（type value type value...）
'''
def methodBody2Tokens(path,dist,errPath):
    with open(path,'r', encoding='utf-8') as f:
        lines=f.readlines()
    for line in lines:
        lineList=line.split('@')
        print(lineList)
        methodBody=lineList[-1].replace('\x00','')

        try:
            bodySequence=[]
            methodBodyTokenJson=esprima.tokenize(methodBody)
            for pair in methodBodyTokenJson:
                types=pair.type
                value=pair.value
                bodySequence.append(types)
                bodySequence.append(value)
            bodySequence=' '.join(bodySequence)
            with open(dist,'a') as f:
                f.write('@'.join(lineList[:-1]+[bodySequence])+'\n')
        except:
            with open(errPath,'a',encoding='utf8') as f:
                f.write('@'.join(lineList)+'\n')



if __name__ == '__main__':
    path='../data/our-data/spring-method-body/spring-method-body.txt'
    dist='../data/our-data/spring-method-body/spring-method-body-token.txt'
    err='../data/our-data/spring-method-body/spring-method-body-err-item.txt'
    methodBody2Tokens(path,dist,err)