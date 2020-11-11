package MethodExtraction;

import java.io.*;
import java.util.*;

import util.Util;



public class Main {
	public static void main(String args[]) throws IOException {

		try (BufferedReader br = new BufferedReader(new FileReader("tests/file_list.txt"))) {
			String line;
			while ((line = br.readLine()) != null) {
				//依次读取项目所在文件夹
				String projectPath = line;
				System.out.println(line);
				//获得项目的名称
				String projectName = line.substring(line.lastIndexOf('/')+1);
				//遍历项目的文件夹获取.java文件
				File projectDirFile=new File(projectPath);
				filesDirs(projectDirFile,projectName);
			}
		}
	}

	//遍历项目文件夹获取Java文件

	//使用递归遍历文件夹及子文件夹中文件
	public static void filesDirs(File file,String projectName) throws FileNotFoundException {
		//File对象是文件或文件夹的路径，第一层判断路径是否为空
		if(file!=null){
			//第二层路径不为空，判断是文件夹还是文件
			if(file.isDirectory()){
				//进入这里说明为文件夹，此时需要获得当前文件夹下所有文件，包括目录
				File[] files=file.listFiles();//注意:这里只能用listFiles()，不能使用list()
				//files下的所有内容，可能是文件夹，也可能是文件，那么需要一个个去判断是文件还是文件夹，这个判断过程就是这里封装的方法
				//因此可以调用自己来判断，实现递归
				for (File flies2:files) {
					filesDirs(flies2,projectName);
				}
			}else{
				System.out.println("正在处理"+projectName+"文件"+file+".......");
				//获取java绝对路径
				String javaFileAbsPath=file.getAbsolutePath();
				//获取Java的类名
				String javaFileName=file.getName();
				String publicClassName=javaFileName.substring(0,javaFileName.lastIndexOf('.'));
				parseJavaFileExtractMethodBody(javaFileAbsPath,projectName,publicClassName);

			}
		}else{
			System.out.println("文件不存在");
		}
	}


	//解析Java文件
	public static void parseJavaFileExtractMethodBody(String javaFileAbsoulutePath,String projectName,String publicClassName) throws FileNotFoundException {
		JavaMethodExtractor methodExtractor = new JavaMethodExtractor(javaFileAbsoulutePath);
		methodExtractor.extract();
		try {
			HashMap<String, String> methodBodies = methodExtractor.getMethodBodies(); // methodSignature => methodBody
			HashMap<String, ArrayList<String>> apiCalls = methodExtractor.getAPICalls(); //methodSignature => ArrayList of API Calls
			String packageName=methodExtractor.getPackageName().replace('\n','\0');
			String javaClassName=publicClassName;
			Set<String> methodSigs = methodBodies.keySet();
			for (String methodSig: methodSigs){
				String methodName=methodSig;
				String methodBody=methodBodies.get(methodSig).replace('\n','\0');
				StringBuilder sb=new StringBuilder();
				sb.append(projectName).append("@").append(packageName).append("@").append(publicClassName).append("@").append(methodName).append("@").append(methodBody).append("\n");
				String writeToFileContent=sb.toString();
				writeToFile(writeToFileContent);
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}


	//写入文件
	public static  void writeToFile(String contents){
		FileWriter fw;
		BufferedWriter bf;
		boolean append =false;
		File file = new File("test.txt");
		try{
			if(file.exists()) append =true;
			fw = new FileWriter("test.txt",append);//同时创建新文件
			//创建字符输出流对象
			bf = new BufferedWriter(fw);
			//创建缓冲字符输出流对象
			bf.append(contents);
			bf.flush();
			bf.close();
		}catch (IOException e){
			e.printStackTrace();
		}

	}




}
