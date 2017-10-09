#Script for Suffix/Prefix, Search/Replace and Rename
import pymel.core as pm


def suffixName():
    suffixName = ""
    obj = pm.ls(sl=True)
    for i in range(len(obj)):
        pm.rename(obj[i],obj[i]+suffixName)

def prefixName():
    prefixName = ""
    for i in range(len(obj)):
        pm.rename(obj[i],prefixName+obj[i])

def search_replace():
    search = ""
    replace = ""
    obj = pm.ls("*" + search + "*")
    for i in range(len(obj)):
        pm.rename(obj[i],obj[i].replace(search, replace))

def renam(name = None):
    #name = "A"
    start = "0"
    obj = pm.ls(sl=True)
    for i in range(len(obj)):
        pm.rename(obj[i], name+str(i))

if __name__ == '__main__':
    suffixName()
    prefixName()
    search_replace()
    renam()