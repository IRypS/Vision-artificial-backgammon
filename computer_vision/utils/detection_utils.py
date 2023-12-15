import cv2
import numpy as np


def fixRectangleDraw( template, x, y ):
    return x + template.shape[1], y + template.shape[0]


def drawRectanglesInObjects( mainImage, indentifiedObjects, templateObjectImg, rgbColor ):
    for object in indentifiedObjects:
        x1, y1 = object[0], object[1]
        x2, y2 = fixRectangleDraw( templateObjectImg, x1, y1 )
        cv2.rectangle( mainImage, (x1, y1), (x2, y2), rgbColor, 2 )


def drawRectanglesInGroups(mainImage, groups, templateObjectImg, type="group"):
    i = 1
    for group in groups:
        min_x = min(obj[0] for obj in group)
        min_y = min(obj[1] for obj in group)
        max_x = max(obj[0] for obj in group)
        max_y = max(obj[1] for obj in group)
        x2, y2 = fixRectangleDraw( templateObjectImg, max_x, max_y )

        borderColor = (255, 0, 0) if type == "group" else (255, 255, 0)
        fontSize    = 0.6 if type == "group" else 0.5
        thickness   = 2 if type == "group" else 2
        shape       = 3 if type == "group" else 3

        cv2.rectangle(mainImage, (min_x, min_y), (x2, y2), borderColor, 2)

        numberPieces = str(len(group))
        titleGroup = f"G{i}: {numberPieces} fchs" if type == "group" else f"{numberPieces} fchs"
        drawScore( mainImage,titleGroup, (min_x, min_y - 5), fontSize, thickness, shape )

        i += 1



def drawScore(image, text, position, fontSize=1.2, fontThickness=3, fontThicknessShape=4):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = fontSize
    font_thickness = fontThickness
    font_color = (255, 255, 255)
    border_color = (0, 0, 0)

    cv2.putText(image, text, position, font, font_scale, border_color, font_thickness + fontThicknessShape) # shape
    cv2.putText(image, text, position, font, font_scale, font_color, font_thickness)