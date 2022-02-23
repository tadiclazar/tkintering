from setuptools import setup

setup(
    name="wget_gui",
    description="GUI Frontend to wget",
    version="0.0.1",
    py_modules=["wget_gui_main", "download_funcs"],
    entry_points={
     "gui_scripts": ["wget_gui = wget_gui_main:main"]
    }
)
