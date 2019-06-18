# -- coding: utf-8 --
import handle as handleObj
print "welcome to use it"


class Code:
    pass

handle=[]
handles=[]

def compare(str1,str2):
    return str1.replace(' ','').lower()==str2.replace(' ','').lower()

def split_line(line):
    #print line
    code=Code()
    code.addr=line[0:8].rstrip()
    code.asm=line[18:60].rstrip()
    code.info=line[62:].rstrip()
    return code


theLog=open("d:\\11.txt", "r").readlines()

for index in range(len(theLog)):
    line=theLog[index].rstrip()
    code=split_line(line)
    #break
    if code.addr == 'Address':
        continue
    handle.append(code)
    if compare(code.asm,'jmp edi'):
        #print code.addr
        handles.append(handle)
        handle=[]
    elif compare(code.asm,'push edi'):
        nextSplit=split_line(theLog[index+1].rstrip())
        if compare(nextSplit.asm,'retn'):
            #print code.addr
            handle.append(nextSplit)
            handles.append(handle)
            handle=[]
            ##### 上面已经分析过了，下条语句是retn，所以直接跳过吧
            index+=1


theHandleIndex=0


def analysis_handle(handle):
    global theHandleIndex
    theHandleIndex += 1
    ret =handleObj.run(handle)
    param= " ".join(ret['param'])
    vcode='%s %s' % (ret['name'],param)
    print "%4d----%s" % (theHandleIndex, vcode)

    #return
    if ret['name'] == "UNKNOWN":
        for code in handle:
            print '%s%s%s;%s' % (ret['name'].ljust(12), code.addr.ljust(10), code.asm.ljust(40), code.info)


for theHandle in handles:
    analysis_handle(theHandle)
