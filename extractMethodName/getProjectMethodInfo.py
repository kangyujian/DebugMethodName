import getJavaMethodInfo as javainfo
import os
import re

def hump2underline(hunp_str):
    p=re.compile(r'([a-z]|\d)([A-Z])')
    sub=re.sub(p,r'\1 \2',hunp_str).lower()
    return sub.replace(' ',',')


# 生成方法名称的数据集
# 格式为<Project_name>:<Package_name>:<Class_name>:<Method_name>:<Parameters>:<Return_type>@<Return_type>@<Parsed_method_name>
def generateMethodNameDataSet(projectSrc):
    with open('../data/our_data/spring-method-name/methodName.txt', 'a+') as methodNameFile:
        methodNameFile.write('<Project_name>:<Package_name>:<Class_name>:<Method_name>:<Parameters>:<Return_type>@<Return_type>@<Parsed_method_name>\n')
    for root, dirs, files in os.walk(projectSrc):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        projectName=root[root.rfind('/')+1:]

        # 遍历文件
        for f in files:

            with open('../data/our_data/spring-method-name/methodName.txt','a+') as methodNameFile:
                javaFileSrc=root+'/'+f
                try:
                    methodList,packageName,className=javainfo.getJavaFileInfoList(javaFileSrc)

                    for method in methodList:

                        methodName=method.name
                        print('正在处理{}类{}方法...'.format(className, methodName))
                        returnType=method.return_type
                        parameters=method.parameters
                        parameterStr=''
                        parsedMethodName=hump2underline(methodName)
                        for parameter in parameters:
                            parameterStr=parameterStr+parameter.type.name+'+'+parameter.name
                        if returnType==None:
                            returnType='None'
                        else:
                            returnType=returnType.name
                        linestr=projectName+':'+packageName+':'+className+':'+methodName+':'+parameterStr+':'+returnType+'@'+returnType+'@'+parsedMethodName+'\n'
                        methodNameFile.write(linestr)
                except:
                    print('发生异常,继续....')
    print('处理完成...')



# 提取方法体的数据集



if __name__ == '__main__':
    generateMethodNameDataSet('../data/our_data/spring-source-code')
