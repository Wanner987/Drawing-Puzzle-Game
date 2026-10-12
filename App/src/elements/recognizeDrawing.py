import math
from .eventManager import EventManager

class recognizeDrawing:
    # For now this will only use the $1 unistroke recognizer
    # 1 Collect points/vector/coords 
    # 2 Resample collection to evenly spaced points
    # 3 Normalize 
        # - Rotation
        # - scale
        # - position
    # 4 compair against known shapes
    # 5 return the closest match
    
    def __init__(self):
        pass

    def distance(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        return math.hypot(dx, dy)

    def path_length(self, points : list):
        totalLength = 0

        for i in range(1, len(points)):
            totalLength += self.distance(points[i-1], points[i])
        
        return totalLength

    def resample_points(self, points : list, n = 64): # n is the number of points at the end of resample
        
        # turn all points into tuples
        points = [tuple(p) for p in points]
        
        interval = self.path_length(points) / (n - 1)

        # error hanling 
        if interval == 0:
            return [points[0]] * n

        new_points = [points[0]]
        distance_since_last = 0.0
        i = 1

        while i < len(points):
            p1 = points[i-1]
            p2 = points[i]
            
            distance = self.distance(points[i-1], points[i])
            if distance_since_last + distance >= interval:
                ratio = (interval - distance_since_last) / distance

                q = (
                    p1[0] + ratio * (p2[0] - p1[0]),
                    p1[1] + ratio * (p2[1] - p1[1])
                )

                new_points.append(q)
                points.insert(i, q)
                distance_since_last = 0
                i += 1
            else:
                new_points.append(new_points[-1])
                i += 1
            # end while loop
        
        while len(new_points) < n:
            new_points.append(points[-1])

        return new_points[:n]

    def recognize(self, points : list):
        if len(points) < 2:
            return "error list is too short"

        recognizedShape : str = "None recognized"
        
        start = points[0]
        end = points[-1]
        middle = points[len(points) // 2]

        path_length = self.path_length(points)

        if path_length == 0:
            return "unknown path is too short (0)"

        straightness = self.distance(start, end) / path_length

        if straightness >= 0.90:
            dx = end[0] - start[0]
            dy = end[1] - start[1]

            if abs(dx) >= abs(dy):
                recognizedShape = "line-right" if dx > 0 else "line-left"
            else:
                recognizedShape = "line-down" if dy > 0 else "line-up"

        # U shape recognization
        distance = self.distance(start, end)

        if distance / path_length < 0.75: # Distance from ends is within some %
            center_x = (start[0] + end[0]) / 2
            center_y = (start[1] + end[1]) / 2

            dx = middle[0] - center_x
            dy = middle[1] - center_y

            # 3. Determine which direction the U opens
            if abs(dx) >= abs(dy):
                if dx > 0:
                    recognizedShape = "U-left"
                else:
                    recognizedShape = "U-right"
            else:
                if dy > 0:
                    recognizedShape = "U-up"
                else:
                    recognizedShape = "U-down"
        
        EventManager.shapeRecognized(recognizedShape)
        return recognizedShape
