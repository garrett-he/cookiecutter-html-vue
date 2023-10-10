import os
import shutil
from glob import glob

license_id = '{{ cookiecutter.license_id }}'
with_vuex = '{{ cookiecutter.with_vuex }}'

if license_id != 'Unlicense':
    os.rename('LICENSE.{{ cookiecutter.license_id }}', 'LICENSE')
    os.unlink('UNLICENSE')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if with_vuex == 'no':
    shutil.rmtree('src/store', ignore_errors=True)
