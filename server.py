from bottle import get, post, route, run, request, response

# Called by web app to request device id be wiped.
@route('/wipedevice/:id#[0-9]+#')
def wipe_device(id):
    print "Wipe device: %d" % int(id)

# Called by web app to get location and wiped status of a device
@route('/devicestatus/:id#[0-9]+#')
def get_device_status(id):
    print "Get device status: %d" % int(id)

# Called by a remote device to see if it should initiate a wipe
@route('/checkwiperequested/:id#[0-9]+#')
def check_wipe_requested(id):
    print "Check wipe requested: %d" % int(id)

# Called by a remote device to inform server of wipe status (success/fail)
@route('/updatewipestatus/:id#[0-9]+#')
def update_wipe_status(id):
    print "poo"
    isWiped = request.GET.get('iswiped')
    print "poo2"
    print "Updating device %d's wiped status to %s" % (int(id), isWiped)

# Called by a remote device to updated it's location
@route('/updatelocation/:id#[0-9]+#/:lat#[0-9]+#/:lon#[0-9]+#')
def update_location(id, lat, lon):
    print "Updating device %d's location to %s, %t" % int(id), lat, lon

run(host='localhost', port=8080)
