import sys
import pymel.core as pm
import maya.mel as mel

#sys.path.append(r"D:\rishu\rs_toolkit")

from PySide import QtGui, QtCore
from rs_ui import rs_riggingtool_ui
reload(rs_riggingtool_ui)


from rs_module import create_upper_grp
reload(create_upper_grp)

from rs_module import JointCreateOnSelection
reload(JointCreateOnSelection)

from rs_module import connectAttribute
reload(connectAttribute)

from rs_module import facialSetup
reload(facialSetup)

from rs_module import proxyCTRL
reload(proxyCTRL)

from rs_module import transferAttribute
reload(transferAttribute)

from rs_module import renameSuffixPrefixSearchReplace
reload(renameSuffixPrefixSearchReplace)

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.OpenMayaUI as omui
from shiboken import wrapInstance


def maya_main_window():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


class testWin(MayaQWidgetDockableMixin, QtGui.QMainWindow, rs_riggingtool_ui.rs_riggingtool_ui):
    def __init__(self, prnt=None):
        super(testWin, self).__init__(prnt)
        self.setupUi(self)
        self.proxy_le.hide()
        self.label_34.hide()
        self.sourcevis_le.hide()
        self.pushButton_64.hide()
        self.label_38.hide()
        self.destinationvisibility_le.hide()
        self.pushButton_68.hide()
        self.label_39.hide()
        self.sourceattribute_le.hide()
        self.setsource_pb.hide()
        self.label_40.hide()
        self.destinationattribute_le.hide()
        self.setdestination_pb.hide()
        self.transferattribute_pb.hide()
        self.line_12.hide()
        self.line_13.hide()

        self.makeConnections()

    def makeConnections(self):
        self.creategroupname_pb.clicked.connect(self.createuppergroup)
        self.getchild_pb.clicked.connect(self.getChild)
        self.getparent_pb.clicked.connect(self.getParent)
        self.createjoinandskin_pb.clicked.connect(self.jointonselection)
        self.getinput_pb.clicked.connect(self.getinput)
        self.setctrl_pb.clicked.connect(self.setctrl)
        self.connect_pb.clicked.connect(self.connectAttribute)
        self.setup_pb.clicked.connect(self.facial_setup)
        self.build_pb.clicked.connect(self.facial_build)
        self.selectproxygrp_pb.clicked.connect(self.proxyctrl)
        self.pushButton_61.clicked.connect(self.trans)
        self.pushButton_62.clicked.connect(self.rot)
        self.pushButton_63.clicked.connect(self.scale)
        self.pushButton_65.clicked.connect(self.setTrans)
        self.pushButton_66.clicked.connect(self.setRot)
        self.pushButton_67.clicked.connect(self.setScale)
        self.rename_pb.clicked.connect(self.renam)
        self.searchreplace_pb.clicked.connect(self.searchReplace)
        self.destination_pb.clicked.connect(self.setdestination)
        self.add_pb.clicked.connect(self.suffPrefix)

    def createuppergroup(self):
        create_upper_grp.create_upper_grp(self.groupname_le.text())

    def jointonselection(self):
        piv = self.centerofobj_cb.isChecked()
        ch = JointCreateOnSelection.jointonselection(self.childobj_le.text().split(','), pivot=piv)
        if self.parentobj_le.text() != '':
            pr = JointCreateOnSelection.jointonselection(self.parentobj_le.text().split(','), prnt=True, pivot=piv)
            pm.parent(ch[0], pr[0])
            pm.parent(ch[1], pr[1])

    def connectAttribute(self):
        connectAttribute.connectAttribute(self.listt,self.ctrlName)

    def proxyctrl(self):
        proxyCTRL.createProxyCTRL()

    def getChild(self):
        listt = [str(x) for x in pm.ls(sl=True)]
        self.childobj_le.setText(','.join(listt))

    def getParent(self):
        listt = [str(x) for x in pm.ls(sl=True)]
        self.parentobj_le.setText(listt[0])

    def getinput(self):
        self.listt = [str(x) for x in pm.ls(sl=True)]
        self.animateobj_le.setText(','.join(self.listt))

    def setctrl(self):
        listt = [str(x) for x in pm.ls(sl=True)]
        channelBox = mel.eval('global string $gChannelBoxName; $temp=$gChannelBoxName;')
        attrs = pm.channelBox(channelBox, q=True, sma=True)[0]
        self.ctrlName = listt[0]+'.'+attrs
        self.ctrl_le.setText(self.ctrlName)

    def facial_setup(self):
        if self.lip_cb.isChecked():
            facialSetup.lip_setup()

        if self.brow_cb.isChecked():
            facialSetup.eyeBrow_setup()

        if self.toonyjaw_cb.isChecked():
            facialSetup.toony_jaw()

        if self.sneer_cb.isChecked():
            facialSetup.nose_setup()

    def facial_build(self):
        if self.lip_cb.isChecked():
            facialSetup.LipsBuild()

        if self.brow_cb.isChecked():
            facialSetup.eyeBrowBuild()

        if self.toonyjaw_cb.isChecked():
            facialSetup.ToonyJaw_Build()

        if self.sneer_cb.isChecked():
            facialSetup.NoseBuild()

    def trans(self):
        transValue,rotValue,scaleValue = transferAttribute.getAttribute()
        self.sourcetranslate_le.setText(str(transValue))

    def rot(self):
        transValue,rotValue,scaleValue = transferAttribute.getAttribute()
        self.sourcerotate_le.setText(str(rotValue))

    def scale(self):
        transValue,rotValue,scaleValue = transferAttribute.getAttribute()
        self.sourcescale_le.setText(str(scaleValue))

    def setTrans(self):
        trans = self.sourcetranslate_le.text()
        transList = trans.split(',')
        transList = [float(x) for x in transList]
        setT = transferAttribute.setAttribute(None, transList, None, None)
        self.destinationtranslate_le.setText(str(setT))

    def setRot(self):
        rot = self.sourcerotate_le.text()
        rotateList = rot.split(',')
        rotateList = [float(x) for x in rotateList]
        setR = transferAttribute.setAttribute(None, None, rotateList, None)
        self.destinationrotate_le.setText(str(setR))

    def setScale(self):
        scale = self.sourcescale_le.text()
        scaleList = scale.split(',')
        scaleList = [float(x) for x in scaleList]
        setS = transferAttribute.setAttribute(None, None, None, scaleList)
        self.destinationscale_le.setText(str(setS))

    def renam(self):
        renameSuffixPrefixSearchReplace.renam(self.rename_le.text())

    def searchReplace(self):
        search = self.searchname_le.text()
        replace = self.replacename_le.text()
        renameSuffixPrefixSearchReplace.search_replace(search,replace)

    def suffixprefix(self):
        renameSuffixPrefixSearchReplace.suffixName(self.name_le.text())

    def setdestination(self):
        self.listt = [str(x) for x in pm.ls(sl=True)]
        self.ctrlname_le.setText(','.join(self.listt))

    def suffPrefix(self):
        if self.suffix_cb.isChecked():
            a = renameSuffixPrefixSearchReplace.suffixName(self.name_le.text())
            renameSuffixPrefixSearchReplace.suffixName(a)

        if self.prefix_cb.isChecked():
            b = renameSuffixPrefixSearchReplace.prefixName(self.name_le.text())
            renameSuffixPrefixSearchReplace.prefixName(b)


if __name__ == '__main__':
    win = testWin(prnt=maya_main_window())
    win.show(dockable=1)