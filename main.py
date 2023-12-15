# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivymd.app import MDApp

from computer_vision.backgammon_cv import countPiecesByColor, countPiecesByGroup

kivy_path = "kivy/layout2v.kv"

images_path = "images"
templates_path = f"{images_path}/templates"

class VisionArtificalBackgammon(MDApp):

    def build(self):
        return Builder.load_file(kivy_path)
    
    def on_start(self):
        self.main_image = images_path + "/backgammon-tablero.png"
        self.piece_1_template = templates_path + "/backgammon-white.png"
        self.piece_2_template = templates_path + "/backgammon-green.png"

        self.thresholdTemplate1 = 0.7
        self.thresholdTemplate2 = 0.55
    
    def workCountPiecesByColor(self):
        countPiecesByColor(
            self.main_image,
            self.piece_1_template,
            self.piece_2_template,
            self.thresholdTemplate1,
            self.thresholdTemplate2,
        )

    def workCountPiecesByGroup(self):
        countPiecesByGroup(
            self.main_image,
            self.piece_1_template,
            self.piece_2_template,
            self.thresholdTemplate1,
            self.thresholdTemplate2,
            "group"
        )

    def workCountPiecesByColumn(self):
        countPiecesByGroup(
            self.main_image,
            self.piece_1_template,
            self.piece_2_template,
            self.thresholdTemplate1,
            self.thresholdTemplate2,
            "column"
        )


if __name__ == '__main__':
    VisionArtificalBackgammon().run()