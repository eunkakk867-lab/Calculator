import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Calculator(QWidget):
    """
    PyQt6를 사용한 기본 계산기 창 클래스
    """
    def __init__(self):
        """
        생성자 메서드. 부모 클래스의 생성자를 호출하고 UI를 초기화합니다.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        사용자 인터페이스(UI)를 초기화하는 메서드
        """
        # 창의 제목을 '계산기'로 설정합니다.
        self.setWindowTitle('계산기')
        
        # 창의 위치와 크기를 설정합니다. (x, y, 너비, 높이)
        # 화면의 x=300, y=300 위치에 300x400 크기의 창이 생성됩니다.
        self.setGeometry(300, 300, 300, 400)

        # '메시지 띄우기' 라는 텍스트를 가진 버튼을 생성합니다.
        btn = QPushButton('메시지 띄우기', self)
        # 버튼의 위치와 크기를 설정합니다.
        btn.setGeometry(100, 175, 100, 50)
        # 버튼을 클릭했을 때 self.showMessageBox 메서드가 호출되도록 연결합니다.
        btn.clicked.connect(self.showMessageBox)

        # 위젯을 화면에 보여줍니다.
        self.show()

    def showMessageBox(self):
        """
        메시지 박스를 화면에 표시하는 메서드
        """
        QMessageBox.information(self, '메시지', 'Button Clicker')

if __name__ == '__main__':
    # QApplication: 프로그램을 실행하고 이벤트 루프를 관리하는 클래스
    app = QApplication(sys.argv)
    
    # 우리가 만든 Calculator 클래스의 인스턴스를 생성합니다.
    ex = Calculator()
    
    # 프로그램을 실행하고, 창을 닫을 때 프로세스가 종료되도록 합니다.
    sys.exit(app.exec())
