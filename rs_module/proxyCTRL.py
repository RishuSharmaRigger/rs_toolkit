'''
Script For Proxy CTRL.
'''
def createProxyCTRL():
	import pymel.core as pm
	proxyGrp = pm.ls(sl=True)[0]
	grp = pm.duplicate(proxyGrp)
	ctrlShape = pm.listRelatives(grp,ad=True,type="nurbsCurve")
	ctrl = pm.listRelatives(ctrlShape,p=True)
	proxyCtrlShape = pm.listRelatives(proxyGrp,ad=True,type="nurbsCurve")
	proxyCtrl = pm.listRelatives(proxyCtrlShape,ap=True)
	proxyGrpHier = pm.listRelatives(proxyGrp,ad=True)
	for i in range(len(proxyGrpHier)):
		pm.rename(proxyGrpHier[i],proxyGrpHier[i]+"Proxy")
	pm.rename(proxyGrp,proxyGrp+"Proxy")
	pm.rename(grp,proxyGrp[:-5])
	for x in range(len(ctrl)):
		pm.connectAttr(ctrl[x].translate,proxyCtrl[x].translate)
		pm.connectAttr(ctrl[x].rotate,proxyCtrl[x].rotate)
	pm.hide(proxyGrp)
	pm.select(cl=True)

if __name__ == '__main__':
	createProxyCTRL()