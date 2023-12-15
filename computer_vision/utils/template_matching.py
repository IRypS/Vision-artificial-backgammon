import numpy as np
import cv2

def objectTemplateMatching( image, template, threshold = 0.7 ):
        objects = []

        result = cv2.matchTemplate( image, template, cv2.TM_CCOEFF_NORMED )
        candidates = np.where( result >= threshold )
        candidates = np.column_stack([ candidates[1], candidates[0] ])

        i = 0
        while len( candidates ) > 0:

            if i == 0: objects.append( candidates[0] )

            else:

                to_delete = []

                for j in range( 0, len(candidates) ):
                    diff = objects[i-1] - candidates[j]

                    if abs(diff[0]) < 10 and abs(diff[1]) < 10:
                        to_delete.append(j)

                candidates = np.delete(candidates, to_delete, axis=0)

                if len(candidates) == 0: break
                objects.append(candidates[0])
                
            i += 1
            
        return objects