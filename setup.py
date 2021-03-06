from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize("cytest.pyx"),
    zip_safe=False,
)

setup(
    name="mixcypy",
    ext_modules=cythonize("mixcypy.py"),
    zip_safe=False,
)