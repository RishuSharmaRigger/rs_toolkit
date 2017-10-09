def ui_py(ui_file):
    from pysideuic import compileUi
    py_file = ui_file.replace('.ui', '.py')
    pyfile = open(py_file, 'w')
    compileUi(ui_file, pyfile, False, 4,False)
    pyfile.close()
    return py_file

if __name__ == '__main__':
    import sys
    print ui_py("rs_riggingtool_ui.ui")
