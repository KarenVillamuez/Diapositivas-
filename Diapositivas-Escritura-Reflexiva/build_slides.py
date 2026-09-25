# -*- coding: utf-8 -*-
"""
Ejecutor de compilación de diapositivas modulares.
Delega a scripts/build.py
"""
import os
import subprocess
import sys

if __name__ == '__main__':
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'build.py')
    sys.exit(subprocess.call([sys.executable, script_path]))
