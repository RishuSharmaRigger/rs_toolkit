import maya.cmds as cmds
def create_upper_grp(name):
    ctrls = cmds.ls(sl=True)
    if ctrls:
        for i in range(len(ctrls)):
            ctrlsname = ctrls[i].split('_')
            grp = cmds.group(em=True,n=ctrlsname[0]+name+ctrlsname[1])
            ctrlsUpperGrp = cmds.listRelatives(ctrls[i],p=True)
            cmds.delete(cmds.parentConstraint(ctrls[i],grp))
            cmds.parent(grp,ctrlsUpperGrp[0])
            cmds.parent(ctrls[i],grp)
        print "Done.....",
    else:
        print "Please Select atleast one Object.....",

if __name__ == '__main__':
    create_upper_grp()