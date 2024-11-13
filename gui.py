from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox
import sys
#from lib import scp_download_file


# Sample data functions
def dynamic_list1():
    return ["Repo1", "Repo2", "Repo3"]

def dynamic_list2():
    return ["Log1", "Log2", "Log3"]

def get_repo_info():
    QMessageBox.information(None, "Repo Info", "Repo Info Fetched!")

def get_logs(selected_from_list1, selected_from_list2):
    selected_items = f"Selected from List 1: {selected_from_list1}\nSelected from List 2: {selected_from_list2}"
    QMessageBox.information(None, "Logs", f"Fetching logs for:\n{selected_items}")

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
        
        # Connect buttons to functions
        self.repo_info_button.clicked.connect(get_repo_info)
        self.logs_button.clicked.connect(self.get_selected_logs)
        
        # Add widgets to layout
        self.layout.addWidget(self.list_widget1)
        self.layout.addWidget(self.list_widget2)
        self.layout.addWidget(self.repo_info_button)
        self.layout.addWidget(self.logs_button)
        
        # Set layout and show the app
        self.setLayout(self.layout)
        self.setWindowTitle("Dynamic List App")
    
    def update_lists(self):
        # Populate List 1
        self.list_widget1.clear()
        for item in dynamic_list1():
            self.list_widget1.addItem(item)
        
        # Populate List 2
        self.list_widget2.clear()
        for item in dynamic_list2():
            self.list_widget2.addItem(item)
    
    def get_selected_logs(self):
        selected_from_list1 = [item.text() for item in self.list_widget1.selectedItems()]
        selected_from_list2 = [item.text() for item in self.list_widget2.selectedItems()]
        get_logs(selected_from_list1, selected_from_list2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
