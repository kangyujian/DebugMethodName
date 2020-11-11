import javalang
import plyj.parser as plyj
from pprint import pprint
'''
# 功能:
    获取Java的方法的信息
# 返回
    1. 方法的对象 包含了方法名 方法参数 返回值
    2. 方法的类名
    3. 方法的包名
'''
def getJavaFileInfoList(sourceFile):
    with open(sourceFile,'r') as f:
        content=f.read()
    tree=javalang.parse.parse(content)
    methodList=[]
    flag=False
    className=None
    packageName=None
    for path, node in tree:
        if(str(type(node).__name__)=='MethodDeclaration'):
            methodList.append(node)
        if (str(type(node).__name__) == 'PackageDeclaration'):
            packageName=node.name
        if (str(type(node).__name__) == 'ClassDeclaration') and flag!=True:
            className=node.name
            flag=True
    return methodList,packageName,className






if __name__ == '__main__':
    getJavaFileBodyCode('./AbstractAdvisorAutoProxyCreator.java')

