def vzdialenost(sirkaStart: float, dlzkaStart : float, sirkaCiel: float, dlzkaCiel : float) -> float:
    import math
    polomer = 6371000
    sirkaStart = math.radians(sirkaStart)
    dlzkaStart = math.radians(dlzkaStart)
    sirkaCiel = math.radians(sirkaCiel)
    dlzkaCiel = math.radians(dlzkaCiel)
    rozdielSirok = sirkaCiel - sirkaStart
    rozdielDlzok = dlzkaCiel - dlzkaStart
    a = math.sin(rozdielSirok/2) ** 2 + math.cos(sirkaStart) * math.cos(sirkaCiel) * math.sin(rozdielDlzok / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return polomer * c / 1000


class GPSTracker:
    def __init__(self):
        self.positions = []
        self.total_length = 0

    def add_position(self, gps_lat, gps_long):
        self.positions.append({'gps_lat': gps_lat, 'gps_long': gps_long})
        self._recount_total_length()

    def store(self):
        # TODO STORE DATA
        pass

    def load(self):
        #TODO LOAD DATA
        pass

    def _recount_total_length(self):
        if len(self.positions) != 1:
            # print(self.positions)
            # print(len(self.positions))
            last_position = self.positions[len(self.positions) - 2]
            # print("LAST")
            # print(last_position)
            new_position = self.positions[len(self.positions) - 1]
            # print("NEW")
            # print(new_position)
            self.total_length += vzdialenost(last_position['gps_lat'], last_position['gps_long'], new_position['gps_lat'], new_position['gps_long'])
            # print(self.total_length)

    def get_total_length(self):
        return self.total_length

tracker = GPSTracker()

# BA
# tracker.add_position(48.1357803, 17.108364)
# KE1
# tracker.add_position(48.725771, 21.300209)

# KE2
tracker.add_position(48.718983, 21.251835)
# PO
tracker.add_position(49.011862,21.245865)

print(tracker.get_total_length())