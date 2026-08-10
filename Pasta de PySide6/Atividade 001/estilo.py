ESTILO = """
QWidget {
    background-color: #b5b8b1;
    color: #3D3D3D;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 14px;
}

h2, h3 {
    color: #FFFFFF;
}

QLineEdit {
    background-color: #3282F6;
    border: 2px solid #333333;
    border-radius: 8px;
    padding: 10px;
    color: #FFFFFF;
}

QLineEdit:focus {
    border: 2px solid #2259A8;
}

QPushButton {
    background-color: #005EF2;
    color: #121212;
    border: none;
    border-radius: 8px;
    padding: 12px;
    font-weight: bold;
    font-size: 14px;
}

QPushButton:hover {
    background-color: #0137F5;
}

QPushButton:pressed {
    background-color: #0E27F5;
}

QListWidget {
    background-color: #3282F6;
    border: 2px solid #333333;
    border-radius: 8px;
    padding: 5px;
    outline: none;
}

QListWidget::item {
    padding: 12px;
    border-bottom: 1px solid #2A2A2A;
    border-radius: 4px;
}

QListWidget::item:selected {
    background-color: #2251F6;
    color: #121212;
    font-weight: bold;
}
"""