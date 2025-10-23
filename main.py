import sys
from PyQt5.QtWidgets import QApplication
from ui import AdditionApp # ui.py 파일에서 AdditionApp 클래스를 가져옵니다.

def main():
    """
    애플리케이션을 생성하고 메인 윈도우를 실행합니다.
    """
    app = QApplication(sys.argv) # QApplication 인스턴스 생성
    main_window = AdditionApp()  # ui.py에 정의된 메인 윈도우 클래스의 인스턴스 생성
    main_window.show()           # 윈도우를 화면에 표시
    sys.exit(app.exec_())        # 애플리케이션 이벤트 루프 시작

if __name__ == '__main__':
    # 이 스크립트가 직접 실행될 때만 main() 함수를 호출합니다.
    main()