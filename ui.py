from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt

class AdditionApp(QWidget):
    """
    덧셈 계산기의 UI 및 관련 로직을 담당하는 클래스.
    윈도우, 입력 필드, 버튼, 결과 레이블을 생성하고 배치합니다.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 기본 설정
        self.setWindowTitle('PyQt 덧셈 계산기 (분리된 UI)')
        self.setGeometry(300, 300, 350, 200) # x, y, width, height

        # 메인 레이아웃 (세로 방향)
        main_layout = QVBoxLayout()

        # 1. 첫 번째 숫자 입력 필드
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("첫 번째 숫자를 입력하세요")
        self.num1_input.setAlignment(Qt.AlignRight) # 텍스트를 오른쪽 정렬
        self.num1_input.setStyleSheet("font-size: 16px; padding: 5px;")

        # 2. 두 번째 숫자 입력 필드
        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("두 번째 숫자를 입력하세요")
        self.num2_input.setAlignment(Qt.AlignRight) # 텍스트를 오른쪽 정렬
        self.num2_input.setStyleSheet("font-size: 16px; padding: 5px;")

        # 3. 더하기 버튼
        self.add_button = QPushButton('더하기', self)
        self.add_button.setStyleSheet("font-size: 18px; padding: 10px; background-color: #4CAF50; color: white; border-radius: 5px;")
        self.add_button.clicked.connect(self.add_numbers) # 버튼 클릭 시 add_numbers 메서드 호출

        # 4. 결과 출력 레이블
        self.result_label = QLabel('결과: ', self)
        self.result_label.setAlignment(Qt.AlignCenter) # 텍스트를 중앙 정렬
        self.result_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.result_label.setWordWrap(True) # 텍스트가 길어지면 줄 바꿈

        # 위젯들을 메인 레이아웃에 추가
        main_layout.addWidget(self.num1_input)
        main_layout.addWidget(self.num2_input)
        main_layout.addWidget(self.add_button)
        main_layout.addStretch(1) # 결과 레이블이 아래쪽에 위치하도록 공간 추가
        main_layout.addWidget(self.result_label)
        main_layout.addStretch(1) # 결과 레이블이 아래쪽에 위치하도록 공간 추가

        # 메인 레이아웃을 윈도우에 설정
        self.setLayout(main_layout)

    def add_numbers(self):
        """
        두 입력 필드의 숫자를 가져와 덧셈을 수행하고 결과를 레이블에 표시합니다.
        숫자가 아닌 값이 입력되면 오류 메시지를 표시합니다.
        """
        try:
            # QLineEdit에서 텍스트 가져오기
            num1_text = self.num1_input.text()
            num2_text = self.num2_input.text()

            # 텍스트를 숫자로 변환 (소수점도 처리하기 위해 float 사용)
            num1 = float(num1_text)
            num2 = float(num2_text)

            # 덧셈 수행
            result = num1 + num2

            # 결과를 레이블에 표시
            self.result_label.setText(f'결과: {result}')
            self.result_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;") # 성공 시 색상 유지
        except ValueError:
            # 숫자로 변환할 수 없는 경우 오류 메시지 표시
            self.result_label.setText('오류: 유효한 숫자를 입력해주세요.')
            self.result_label.setStyleSheet("font-size: 20px; font-weight: bold; color: red;") # 오류 시 빨간색으로 표시