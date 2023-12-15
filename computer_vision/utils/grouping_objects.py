import numpy as np

def groupObjects(objectsPieces1, objectsPieces2, min_distance=10):
        
    objectsLen1 = len( objectsPieces1 )
    objectsLen2 = len( objectsPieces2 )

    if objectsLen1 > 0 and objectsLen2 > 0:
        objects = np.concatenate( (objectsPieces1, objectsPieces2) )

    elif objectsLen1 == 0 and objectsLen2 > 0:
        objects = objectsPieces2

    elif objectsLen1 > 0 and objectsLen2 == 0:
        objects = objectsPieces1

    else:
        objects = []
    
    
    grouped_objects = []

    for obj in objects:

        if len(grouped_objects) == 0:
            grouped_objects.append([obj])
            continue

        added_to_group = False

        for group in grouped_objects:

            for group_obj in group:

                diff = np.array(obj) - np.array(group_obj)

                if np.all(np.abs(diff) < min_distance):
                    group.append(obj)
                    added_to_group = True
                    break

        if not added_to_group:
            grouped_objects.append([obj])

    return grouped_objects