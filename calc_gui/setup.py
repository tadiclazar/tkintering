from setuptools import setup

setup(
    name="calc_gui",
    description="Basic GUI Calculator",
    version="0.0.1",
    py_modules=["calc_gui", "buttons"],
    entry_points={
     "gui_scripts": ["calc_gui = calc_gui:main"]
    }
)
