
class PointsForPlace:
    def __init__(self):
        self.points_pl = 0


    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            return f'Баллы начисляются только первым 100 участникам'
        if place < 1:
            return f'Спортсмен не может занять нулевое или отрицательное место'
        else:
            points_pl = 101 - place
            return points_pl

class PointsForMeters:
    def __init__(self):
        self.points_m = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            return f'Количество метров не может быть отрицательным'
        else:
            points_m = meters * 0.5
            return points_m

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    def get_total_points(self, place, meters):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 