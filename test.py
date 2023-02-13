from flask import Flask, request

import subprocess; import shlex app Flask(_name__)

@app.route('/update_picture', methods=['POST'])

def update_picture():

url = request.form.get('url', 'http://localhost" image = request.form.get('image', 'profile.jpg') # Make sure users can only access localhost

try: url.index('http://localhost')

except: return 'Forbidden 1', 403

# Make sure the image is an image

is_image image.split('.')[-1] in ['jpg', 'png'] if not is_image:

return 'Forbidden 2', 403 args = ['curl', '--proto', '-file', url, '-x',

'GET', '-F', f'image= {image}', '>', 'backup_profile.jpg'] quoted_args [shlex.quote(arg) for arg in args] =

cmd=join(quoted_args) subprocess.run(cmd, shell=True,

stdout=subprocess.PIPE)

return 'Thanks for testing our semi-operational, image backup service!', 200
