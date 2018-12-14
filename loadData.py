


class LoadData:

    def __init__(self):
        self.headerName = "headersName"
        self.paramsName = "paramsName"
        pass

    def readLines(self, fileName):
        with open(fileName,'r',encoding='utf8') as file:
            lines = file.readlines()
        return lines

    def saveLines(self,lines,fileName):
        lines = "\n".join(lines)
        with open(fileName,'w',encoding='utf8') as file:
            file.write(lines)

    def saveFile(self,content,fileName):
        with open(fileName,'w',encoding='utf8') as file:
            file.write(content)

    def readFile(self,fileName):
        with open(fileName,'r',encoding='utf8') as file:
            contents = file.read()
        return contents

    def loadHeaders(self,fileName=None,split=":"):
        '''
        加载头文件数据
        :return:
        '''
        if fileName == None:
            fileName = self.headerName
        lines = self.readLines(fileName)
        headers = {}
        i = 1
        for line in lines:
            line = line.strip()
            if len(line)<1:
                i+=1
                continue
            index = line.find(split)
            if index==0:
                index = line.find(split,index+1)
            if index<0:
                print("error in"+self.headerName+":"+str(i))
                exit()
            key = line[:index].strip()
            value = line[index+1:].strip()
            headers[key]=value
            i+=1
        return headers



    def loadParams(self, paramsName,split="="):
        '''
        加载参数数据
        :return:
        '''
        if paramsName == None:
            paramsName = self.paramsName
        lines = self.readLines(paramsName)
        params = {}
        i = 1
        for line in lines:
            index = line.find(split)
            if index < 0:
                print("error in " + paramsName + ":" + str(i))
                exit()
            key = line[:index].strip()
            value = line[index + 1:].strip()
            params[key] = value
            i += 1
        return params
