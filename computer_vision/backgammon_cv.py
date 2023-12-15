import cv2
import numpy as np

from computer_vision.utils.template_matching import objectTemplateMatching
from computer_vision.utils.detection_utils import drawRectanglesInObjects, drawRectanglesInGroups, drawScore
from computer_vision.utils.grouping_objects import groupObjects

# Works
def countPiecesByColor( initialImage, templateImage1, templateImage2, thresholdTemplate1, thresholdTemplate2 ):

    cv2.destroyAllWindows()

    image = cv2.imread(initialImage)
    templatePiece1 = cv2.imread(templateImage1)
    templatePiece2 = cv2.imread(templateImage2)

    piecesDetected1 = objectTemplateMatching( image, templatePiece1, thresholdTemplate1 )
    piecesDetected2 = objectTemplateMatching( image, templatePiece2, thresholdTemplate2 )

    drawRectanglesInObjects( image, piecesDetected1, templatePiece1, (0, 255, 0) )
    drawRectanglesInObjects( image, piecesDetected2, templatePiece2, (0, 0, 255) )

    drawScore(image, f"Fichas blancas: {str(len(piecesDetected1))}", (35, 35))
    drawScore(image, f"Fichas verdes: {str(len(piecesDetected2))}", (470, 35))

    cv2.imshow("Backgammon", image)


def countPiecesByGroup( initialImage, templateImage1, templateImage2, thresholdTemplate1, thresholdTemplate2, type="group" ):

    cv2.destroyAllWindows()

    image = cv2.imread(initialImage)
    templatePiece1 = cv2.imread(templateImage1)
    templatePiece2 = cv2.imread(templateImage2)

    piecesDetected1 = objectTemplateMatching( image, templatePiece1, thresholdTemplate1 )
    piecesDetected2 = objectTemplateMatching( image, templatePiece2, thresholdTemplate2 )

    minDistance = 100 if type == "group" else 61
    grouped_objects = groupObjects( piecesDetected1, piecesDetected2, minDistance )

    drawRectanglesInGroups( image, grouped_objects, templatePiece1, type )
    groupingType = "grupos" if type == "group" else "columnas"
    drawScore(image, f"Cantidad de { groupingType }: {str(len(grouped_objects))}", (40, 360))

    cv2.imshow("Backgammon", image)