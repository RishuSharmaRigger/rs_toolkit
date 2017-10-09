#Script for Transfer Attribute.
import pymel.core as pm


def transferAttribute():
    obj = pm.ls(sl=True)
    if obj:
        allObj = ("A1", "A2", "A3", "A4", "A5", "A13", "A7", "A8", "A9", "A10", "A11")
        for i in range(len(obj)):
            getTrans = obj[i].translate.get()
            getRotate = obj[i].rotate.get()
            getScale = obj[i].scale.get()
            pm.setAttr(allObj[i]+".t", getTrans)
            pm.setAttr(allObj[i]+".r", getRotate)
            pm.setAttr(allObj[i]+".s", getScale)
    else:
        print "Please Select Target Object......",

# getTrans = None
# getRotate = None
# getScale = None


def getAttribute(obj=None):

    if not obj:
        obj = pm.ls(sl=True)[0]
        if obj:
            tx = "{0:.2f}".format(obj.translate.get()[0], 2)
            ty = "{0:.2f}".format(obj.translate.get()[1], 2)
            tz = "{0:.2f}".format(obj.translate.get()[2], 2)
            getTrans = tx, ty, tz
            trans = ','.join(getTrans)
            rx = "{0:.2f}".format(obj.rotate.get()[0], 2)
            ry = "{0:.2f}".format(obj.rotate.get()[1], 2)
            rz = "{0:.2f}".format(obj.rotate.get()[2], 2)
            getRotate = rx, ry, rz
            rot = ','.join(getRotate)
            sx = "{0:.2f}".format(obj.scale.get()[0], 2)
            sy = "{0:.2f}".format(obj.scale.get()[0], 2)
            sz = "{0:.2f}".format(obj.scale.get()[0], 2)
            getScale = sx, sy, sz
            scale = ','.join(getScale)
            return trans, rot, scale


def setAttribute(allObj=None, getTrans=None, getRotate=None, getScale=None):

    if not allObj:
        allObj = pm.ls(sl=True)
        if allObj:

            if getTrans:
                for i in range(len(allObj)):
                    pm.setAttr(allObj[i]+".t", getTrans)
                    st = ['{:.2f}'.format(x) for x in getTrans]
                    setTrans = ','.join(st)

                return setTrans

            if getRotate:
                for i in range(len(allObj)):
                    pm.setAttr(allObj[i]+".r", getRotate)
                    sr = ['{:.2f}'.format(x) for x in getRotate]
                    setRot = ','.join(sr)

                return  setRot

            if getScale:
                for i in range(len(allObj)):
                    pm.setAttr(allObj[i]+".s", getScale)
                    ss = ['{:.2f}'.format(x) for x in getScale]
                    setScale = ','.join(ss)

                return setScale


    else:
        print "Please Select Target Object......",

if __name__ == '__main__':
    transferAttribute()
    getAttribute()
    setAttribute()

