import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except (IOError, UnicodeDecodeError):
        return ''


setuptools.setup(
    name="psgtray-foss",
    version="1.0.2",
    author="WAS: PySimpleGUI",
    author_email="WAS: mike@PySimpleGUI.org",
    install_requires=['PySimpleGUI-4-foss', 'pystray<=0.18.0', 'pillow'],
    description="Mirror of psgtray that depends on  System Tray Icon that works with the PySimpleGUI tkinter port.  Uses pystray to supply the system tray.  Works well under Windows.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI PySimpleGUI tkinter systemtray pystray",
    url="WAS: https://github.com/PySimpleGUI",
    packages=['psgtray'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
)