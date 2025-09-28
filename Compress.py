import zipfile 
#from zipfile import *

f = zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED) 
#f = ZipFile('images.zip', 'w', ZIP_DEFLATED)

f.write('abu.png')
f.write('moon.png')
f.write('fossip.png')
f.write('trip.png')
f.write('payment.png')

f.close()
