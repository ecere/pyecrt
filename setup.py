from setuptools import setup, Extension
import multiprocessing
from setuptools.command.build import build
from setuptools.command.egg_info import egg_info
import subprocess
import os
import sys
import shutil
import sysconfig

from os import path

dir = os.path.dirname(__file__)
if dir == '':
   rwd = os.path.abspath('.')
else:
   rwd = os.path.abspath(dir)
with open(os.path.join(rwd, 'README.md'), encoding='u8') as f:
   long_description = f.read()

pkg_version       = '0.0.1'

cpu_count = multiprocessing.cpu_count()
eC_dir = os.path.join(os.path.dirname(__file__), 'eC')
eC_c_dir = os.path.join(os.path.dirname(__file__), 'eC', 'bindings', 'c')
eC_py_dir = os.path.join(os.path.dirname(__file__), 'eC', 'bindings', 'py')
platform = 'win32' if sys.platform.startswith('win') else ('apple' if sys.platform.startswith('darwin') else 'linux')
dll_prefix = '' if platform == 'win32' else 'lib'
dll_dir = 'bin' if platform == 'win32' else 'lib'
dll_ext = '.dll' if platform == 'win32' else '.dylib' if platform == 'apple' else '.so'

pymodule = '_pyecrt' + sysconfig.get_config_var('EXT_SUFFIX')
artifacts_dir = os.path.join('artifacts', platform)
lib_dir = os.path.join(eC_dir, 'obj', platform, dll_dir)


def prepare_package_dir(src_files, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for src, rel_dest in src_files:
        dest_path = os.path.join(dest_dir, rel_dest)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        #print("Copying ", src, " to ", dest_path);
        shutil.copy(src, dest_path)

def build_package():
   try:
      if not os.path.exists(artifacts_dir):
         subprocess.check_call(['make', f'-j{cpu_count}', 'SKIP_SONAME=y'], cwd=eC_dir)
         subprocess.check_call(['make', f'-j{cpu_count}', 'SKIP_SONAME=y'], cwd=eC_c_dir)
         prepare_package_dir([
            (os.path.join(lib_dir, dll_prefix + 'ecrt' + dll_ext), os.path.join(dll_dir, dll_prefix + 'ecrt' + dll_ext)),
            #(os.path.join(lib_dir, dll_prefix + 'ecrt_c' + dll_ext), os.path.join(dll_dir, dll_prefix + 'ecrt_c' + dll_ext)),
            (os.path.join(eC_py_dir, 'ecrt.py'), 'ecrt.py'),
            (os.path.join(eC_py_dir, '__init__.py'), '__init__.py'),
         ], artifacts_dir)
   except subprocess.CalledProcessError as e:
      print(f"Error during make: {e}")
      sys.exit(1)

class build_with_make(build):
    def initialize_options(self):
        super().initialize_options()
    def run(self):
        build_package()
        super().run()

class egg_info_with_build(egg_info):
    def initialize_options(self):
        super().initialize_options()
    def run(self):
        build_package()
        super().run()

lib_files = [
   'libecrt' + dll_ext,
#   'libecrt_c' + dll_ext,
]


commands = set(sys.argv)

if 'sdist' in commands:
   packages=['ecrt']
   package_dir = { 'ecrt': 'eC' }
   package_data = {'ecrt': [] }
   cmdclass = {}
   cffi_modules = []
else:
   packages=['ecrt', 'ecrt.lib']
   package_dir={'ecrt': artifacts_dir, 'ecrt.lib': os.path.join(artifacts_dir, 'lib')}
   #package_data={'ecrt': [ pymodule_filename, 'ecrt.py' ], 'ecrt.lib': lib_files}
   package_data={'ecrt': [ 'ecrt.py' ], 'ecrt.lib': lib_files}
   cmdclass={'build': build_with_make, 'egg_info': egg_info_with_build }
   cffi_modules = [os.path.join('eC', 'bindings', 'py', 'build_ecrt.py') + ':ffi_ecrt']

setup(
    name='ecrt',
    version='0.0.1',
    cffi_modules=cffi_modules,
    setup_requires=['cffi >= 1.0.0'],
    install_requires=['cffi >= 1.0.0'],
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    include_package_data=True,
    ext_modules=[],
    cmdclass=cmdclass,
)
