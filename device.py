
class Device:

    def __init__(self, id=-1, allow_tracking=False, lat=0.0, lon=0.0, is_wiped=False, wipe_requested=False):
	self.id = id
	self.allow_tracking = allow_tracking
	self.lat = lat
	self.lon = lon
	self.is_wiped = is_wiped
	self.wipe_requested = wipe_requested
