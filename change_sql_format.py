import sys

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
except ImportError as e:
    print("Hiba: A PyQt5 könyvtár nincs telepítve.")
    print("Kérlek, telepítsd a PyQt5 könyvtárat a 'pip install PyQt5' parancs segítségével.")
    sys.exit(1)

def modify_sql_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(output_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if 'ROW_FORMAT=COMPACT' in line:
                    line = line.replace('ROW_FORMAT=COMPACT', 'ROW_FORMAT=DYNAMIC')
                file.write(line)

        result_label.setText("A fájl sikeresen módosítva lett.")
    except Exception as e:
        result_label.setText(f"Hiba történt a fájl módosítása közben: {e}")

def update_modify_button_state():
    input_path = input_path_entry.text()
    output_path = output_path_entry.text()
    modify_button.setEnabled(bool(input_path and output_path))
    if input_path and output_path:
        modify_button.setStyleSheet("background-color: #007bff; color: white;")
    else:
        modify_button.setStyleSheet("")

def browse_input_file():
    input_file_path, _ = QFileDialog.getOpenFileName(window, "Válassz egy bemeneti fájlt", "", "SQL fájlok (*.sql);;Minden fájl (*.*)")
    if input_file_path:
        input_path_entry.setText(input_file_path)
        file_path_label.setText(input_file_path)
        update_modify_button_state()

def browse_output_file():
    output_file_path, _ = QFileDialog.getSaveFileName(window, "Válassz egy kimeneti fájlt", "", "SQL fájlok (*.sql);;Minden fájl (*.*)")
    if output_file_path:
        output_path_entry.setText(output_file_path)
        update_modify_button_state()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SQL Fájl Módosító")
window.setGeometry(100, 100, 600, 400)

layout = QVBoxLayout()

input_label = QLabel("Bemeneti fájl:")
layout.addWidget(input_label)

input_path_entry = QLineEdit()
input_path_entry.textChanged.connect(update_modify_button_state)
layout.addWidget(input_path_entry)

browse_input_button = QPushButton("Bemeneti Tallózás")
browse_input_button.clicked.connect(browse_input_file)
browse_input_button.setStyleSheet("background-color: #d3d3d3; color: black;")
layout.addWidget(browse_input_button)

file_path_label = QLabel()  # Fájl útvonal megjelenítése
layout.addWidget(file_path_label)

output_label = QLabel("Kimeneti fájl neve és helye:")
layout.addWidget(output_label)

output_path_entry = QLineEdit()  # Kimeneti fájl nevének és helyének beviteli mezője
output_path_entry.textChanged.connect(update_modify_button_state)
layout.addWidget(output_path_entry)

browse_output_button = QPushButton("Kimeneti Tallózás")
browse_output_button.clicked.connect(browse_output_file)
browse_output_button.setStyleSheet("background-color: #d3d3d3; color: black;")
layout.addWidget(browse_output_button)

modify_button = QPushButton("File módosítása!")
modify_button.clicked.connect(lambda: modify_sql_file(input_path_entry.text(), output_path_entry.text()))
modify_button.setStyleSheet("")
modify_button.setEnabled(False)
layout.addWidget(modify_button)

result_label = QLabel()
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
