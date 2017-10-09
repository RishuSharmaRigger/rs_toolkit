import pymel.core as pm
objType = "orientConstraint"
suffixName = "_DORC"
sel = pm.ls(type=objType)
obj = pm.listRelatives(sel,p=True)
if objType == "joint" or objType == "ikHandle" or objType == "effector" or objType == "orientConstraint" or objType == "pointConstraint" or objType == "parentConstraint" or objType == "aimConstraint":
	for i in range(len(sel)):
		renam = pm.rename(sel[i],sel[i]+suffixName)
else:
	for x in range(len(obj)):
		rename = pm.rename(obj[x],obj[x]+suffixName)