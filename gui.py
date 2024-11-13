from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox, QDialog, QLineEdit, QLabel, QFormLayout, QDialogButtonBox
import sys
import functions

# nodes
def node_list():
    return ["node1", "node2", "node3"]

# logs
def log_list():
    return ["Log1", "Log2", "Log3"]

# Move function definitions above the GUI classes
def get_repo_info():
    dialog = InputDialog()
    if dialog.exec_() == QDialog.Accepted:
        username, password, hostname = dialog.get_inputs()
        functions.get_repo_info(username, password)
        QMessageBox.information(None, "Repo Info", f"Repo Info Fetched!\nUsername: {username}\nHostname: {hostname}")

def get_logs(node, log):
    dialog = InputDialog()
    if dialog.exec_() == QDialog.Accepted:
        username, password = dialog.get_inputs()
        selected_items = f"Selected from List 1: {node}\nSelected from List 2: {log}"
        functions.get_logs(node, username, password, log)
        QMessageBox.information(None, "Logs", f"Fetching logs for:\n{selected_items}\nUsername: {username}\nHostname: {node}")

def send_file(username, password, hostname):
    # send file to remote host
    functions.send_file(hostname, username, password)
    QMessageBox.information(None, "Send File", f"File sent to {hostname} using Username: {username}")

class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Credentials")
        
        # Create form layout
        self.layout = QFormLayout()
        
        # Create input fields
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.hostname_input = QLineEdit()
        
        # Set password input to hide text
        self.password_input.setEchoMode(QLineEdit.Password)
        
        # Add fields to layout
        self.layout.addRow(QLabel("Username:"), self.username_input)
        self.layout.addRow(QLabel("Password:"), self.password_input)
        self.layout.addRow(QLabel("Hostname:"), self.hostname_input)
        
        # Create buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        # Add button box to layout
        self.layout.addWidget(self.button_box)
        
        self.setLayout(self.layout)

    def get_inputs(self):
        return self.username_input.text(), self.password_input.text(), self.hostname_input.text()

class SimpleInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Username and Password")
        
        # Create form layout
        self.layout = QFormLayout()
        
        # Create input fields
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        
        # Set password input to hide text
        self.password_input.setEchoMode(QLineEdit.Password)
        
        # Add fields to layout
        self.layout.addRow(QLabel("Username:"), self.username_input)
        self.layout.addRow(QLabel("Password:"), self.password_input)
        
        # Create buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        # Add button box to layout
        self.layout.addWidget(self.button_box)
        
        self.setLayout(self.layout)

    def get_inputs(self):
        return self.username_input.text(), self.password_input.text()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Setup the layout
        self.layout = QVBoxLayout()
        
        # Create two list widgets for dynamic lists
        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()
        
        # Enable multi-selection for both lists
        self.list_widget1.setSelectionMode(QListWidget.MultiSelection)
        self.list_widget2.setSelectionMode(QListWidget.MultiSelection)
        
        # Fill lists with dynamic data
        self.update_lists()
        
        # Create buttons
        self.repo_info_button = QPushButton("Get Repo Info")
        self.logs_button = QPushButton("Get Logs")
        self.send_button = QPushButton("Send")
        
        # Connect buttons to functions
        self.repo_info_button.clicked.connect(get_repo_info)
        self.logs_button.clicked.connect(self.get_selected_logs)
        self.send_button.clicked.connect(self.send_file_dialog)
        
        # Add widgets to layout
        self.layout.addWidget(self.list_widget1)
        self.layout.addWidget(self.list_widget2)
        self.layout.addWidget(self.repo_info_button)
        self.layout.addWidget(self.logs_button)
        self.layout.addWidget(self.send_button)
        
        # Set layout and show the app
        self.setLayout(self.layout)
        self.setWindowTitle("Dynamic List App")
    
    def update_lists(self):
        # Populate nodes list
        self.list_widget1.clear()
        for item in node_list():
            self.list_widget1.addItem(item)
        
        # Populate logs list
        self.list_widget2.clear()
        for item in log_list():
            self.list_widget2.addItem(item)
    
    def get_selected_logs(self):
        nodes = [item.text() for item in self.list_widget1.selectedItems()]
        logs = [item.text() for item in self.list_widget2.selectedItems()]
        for node in nodes:  
            for log in logs:
                get_logs(node, log)
    
    def send_file_dialog(self):
        dialog = InputDialog()
        if dialog.exec_() == QDialog.Accepted:
            username, password, hostname = dialog.get_inputs()
            send_file(username, password, hostname)

   #def get 
    def get_username_password(self):
        dialog = SimpleInputDialog()
        if dialog.exec_() == QDialog.Accepted:
            username, password = dialog.get_inputs()
            return username, password

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
