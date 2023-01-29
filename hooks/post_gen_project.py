import os
import shutil
from glob import glob

LICENSE_ID = '{{ cookiecutter.license_id }}'
WITH_VUEX = '{{ cookiecutter.with_vuex }}'

os.rename('LICENSE.{{ cookiecutter.license_id }}', 'LICENSE')

if LICENSE_ID == 'Unlicense':
    os.rename('LICENSE', 'UNLICENSE')

if 'GPL' in LICENSE_ID:
    os.rename('LICENSE', 'COPYING')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if WITH_VUEX == 'no':
    shutil.rmtree('src/store', ignore_errors=True)
