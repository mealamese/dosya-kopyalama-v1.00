import sys, os, shutil
from PyQt5 import QtWidgets

class GUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.butKaynak = QtWidgets.QPushButton("Kaynak Dizin")
        self.LabelKaynak = QtWidgets.QLabel("")
        self.butHedef = QtWidgets.QPushButton("Hedef Dizin")
        self.LabelHedef = QtWidgets.QLabel("")
        self.butCalistir = QtWidgets.QPushButton("Çalıştır")
        self.LineUzanti = QtWidgets.QLineEdit("")
        self.LineUzanti.setPlaceholderText("Dosya Uzantısını Giriniz")
        self.checkYeniKlasor = QtWidgets.QCheckBox("Kopyalanacak dizinde yeni klasör oluştur")
        self.yeniklasorismi = QtWidgets.QLineEdit("")
        self.yeniklasorismi.setPlaceholderText("Oluşturmak İstediğiniz Klasör İsmi")
        self.ilerlemedurumu = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.butKaynak)
        v_box.addWidget(self.LabelKaynak)
        v_box.addWidget(self.butHedef)
        v_box.addWidget(self.LabelHedef)
        v_box.addStretch()
        v_box.addWidget(self.LineUzanti)
        v_box.addWidget(self.checkYeniKlasor)
        v_box.addWidget(self.yeniklasorismi)
        v_box.addStretch()
        v_box.addWidget(self.ilerlemedurumu)
        v_box.addWidget(self.butCalistir)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addLayout(v_box)

        self.setLayout(h_box)
        self.setWindowTitle("Kopyalama Programı")

        self.butKaynak.clicked.connect(self.kaynak_dizin)
        self.butHedef.clicked.connect(self.hedef_dizin)
        self.butCalistir.clicked.connect(self.calistir)

        self.show()

    def kaynak_dizin(self):
        self.kaynak_yolu = QtWidgets.QFileDialog.getExistingDirectory(self, "Kaynak Dizin", os.getenv("HOME"))
        self.LabelKaynak.setText("Kaynak Dizin: " + self.kaynak_yolu)

    def hedef_dizin(self):
        self.hedef_yolu = QtWidgets.QFileDialog.getExistingDirectory(self, "Hedef Dizin", os.getenv("HOME"))
        self.LabelHedef.setText("Hedef Dizin: " + self.hedef_yolu)

    def calistir(self):
        hedef_dizini = self.hedef_yolu

        if(self.checkYeniKlasor.isChecked()):
            yeni_hedef = self.hedef_yolu + os.sep + self.yeniklasorismi.text()
            if not os.path.isdir(yeni_hedef):
                os.makedirs(yeni_hedef)
            self.LabelHedef.setText("Hedef Dizin: " + yeni_hedef)
            hedef_dizini = yeni_hedef

        kopyalanan_dosya = 0
        toplam_dosya = 0

        for yol, klasor, dosya in os.walk(self.kaynak_yolu):
            for i in dosya:
                if(i.endswith(self.LineUzanti.text())):
                    toplam_dosya += 1

        for yol, klasor, dosya in os.walk(self.kaynak_yolu):
            for i in dosya:
                if(i.endswith(self.LineUzanti.text())):
                    shutil.copy(os.sep.join([yol, i]) , hedef_dizini)
                    kopyalanan_dosya += 1
                    self.ilerlemedurumu.setText("{}/{} Tamamlandı. {} Dosya Kaldı.".format(kopyalanan_dosya, toplam_dosya, toplam_dosya - kopyalanan_dosya))
                    self.setWindowTitle("%{} Tamamlandı".format(round((kopyalanan_dosya/toplam_dosya)*100,2)))

        self.setWindowTitle("Kopyalama Programı")

app = QtWidgets.QApplication(sys.argv)

gui = GUI()

sys.exit(app.exec_())
