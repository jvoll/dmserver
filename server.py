from bottle import get, post, route, run, request, response
from device import *
from io import TextIOWrapper
import json

# Register a device for remote wipe and tracking
# return an id for the device
@route('/registerdevice/')
def register_device():
    id = len(devices)
    allow_tracking = request.GET.get('allowtracking')
    if not allow_tracking:
	allow_tracking=False
    devices.append( Device( id, allow_tracking ) )
    print "Length of devices: %s" % len(devices)
    return {'id':id}

# Called by web app to request device id be wiped.
@route('/wipedevice/:id#[0-9]+#', method='POST')
@post('/wipedevice/:id#[0-9]+#')
def wipe_device(id):
    id = int(id)
    if (is_device(id)):
	devices[id].wipe_requested = True
	print "Wipe device: %d" % id
    else:
	#send back a failure message?
	print "device id not found"

# Called by web app to get location and wiped status of a device
@route('/devicestatus/:id#[0-9]+#')
def get_device_status(id):
    id = int(id)
    if (is_device(id)):
	print "Get device status: %d" % id
	return {'id':devices[id].id, 'wipe_requested':devices[id].wipe_requested, 'lat':devices[id].lat,
	    'lon':devices[id].lon, 'is_wiped':devices[id].is_wiped, 'allow_tracking':devices[id].allow_tracking}
    else:
	#send a failure of some sort
	print "device id not found"

# Called by a remote device to see if it should initiate a wipe
@route('/checkwiperequested/:id#[0-9]+#')
def check_wipe_requested(id):
    id = int(id)
    if (is_device(id)):
	print "Check wipe requested: %d" % id
	return {'id':devices[id].id, 'wipe_requested':devices[id].wipe_requested}
    else:
	#send a failure of some sort
	print "device id not found"

# Called by a remote device to inform server of wipe status (success/fail)
@route('/updatewipestatus/:id#[0-9]+#', method='POST')
@post('/updatewipestatus/:id#[0-9]+#')
def update_wipe_status(id):
    id = int(id)
    entity = json.loads(request.body.readline())
    isWiped = entity.get('iswiped')
    if (is_device(id)):
	devices[id].is_wiped = isWiped
        print "Updating device %d's wiped status to %s" % (int(id), isWiped)
    else:
	#send a failure of some sort
	print "device id not found"

# Called by a remote device to updated it's location
@route('/updatelocation/:id#[0-9]+#', method='POST')
@post('/updatelocation/:id#[0-9]+#')
def update_location(id):
    id = int(id)
    entity = json.loads(request.body.readline())
    lat = entity.get('lat')
    lon = entity.get('lon')
    if (is_device(id)):
	devices[id].lat = lat
	devices[id].lon = lon
	print "Updating device %d's location to %s, %s" % (int(id), lat, lon)
    else:
	#send a failure of some sort
	print "device id not found"

# Helper function to determine if device id is registered
def is_device(id):
    return int(id) < len(devices) and devices[int(id)]


devices=[]
run(host='localhost', port=8080)
