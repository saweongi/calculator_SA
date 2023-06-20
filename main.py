import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.resize(256,256)
        self.show()

if __name__ =='__main__': # 이 파일을 직접 실행할 시에만 명령을 수행하겠다!.
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())