### Create Joints on Object with CTRLs ###
import pymel.core as pm

def jointonselection(obj=list(), prnt=False, pivot=False):
    if not obj:
        obj = pm.ls(sl=True)
    if obj:
        retJoints = list()
        retCtrl = list()
        for i in range(len(obj)):
            pm.select(cl=True)
            jnt = pm.joint(n=obj[i]+'_Jnt')
            retJoints.append(jnt)
            endJnt = pm.joint(n=obj[i]+'_EndJnt',p=(0,1,0))
            prntConst = obj[i]
            if pivot:
                prntConst = pm.cluster(obj[i])
            pm.select(cl=True)
            pm.delete(pm.parentConstraint(prntConst,jnt))
            pm.select(cl=True)
            if pivot:
                pm.delete(prntConst)
            pm.hide(jnt)
            offsetJnt = pm.joint(n='FKOffset'+obj[i])
            retCtrl.append(offsetJnt)
            pm.setAttr(offsetJnt+'.drawStyle',2)
            pm.delete(pm.parentConstraint(jnt,offsetJnt))
            ExtraGrp = pm.group(n='FKExtra'+obj[i],em=True)
            pm.delete(pm.parentConstraint(offsetJnt,ExtraGrp))
            pm.parent(ExtraGrp,offsetJnt)
            CTRL = pm.circle(n=obj[i]+'_CTRL',ch=False,nr=(0,1,0))
            pm.delete(pm.parentConstraint(jnt,CTRL))
            pm.parent(CTRL,ExtraGrp)
            jntNul = pm.joint(n='FK'+obj[i])
            pm.setAttr(jntNul+'.drawStyle',2)
            pm.parentConstraint(CTRL,jnt)
            bind = pm.skinCluster(obj[i],jnt)
                   
        print "Done...",
        if not prnt:
            return retJoints, retCtrl
        else:
            return retJoints, jntNul
    else:
        print "Please Select Object",
        return False, False
        
if __name__ == '__main__':
    ch = jointonselection()
    pr = jointonselection()

    pm.parent(ch[0], pr[0])
    pm.parent(ch[1], pr[1])