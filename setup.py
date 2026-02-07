# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 Ferric Collective <galvanist@ferric-collective.org>

from setuptools import setup, find_packages

setup(
    name="circuit_gen",
    version="0.1.0",
    author="galvanist@ferric-collective.org",
    description="A facade for circuit simulation and KiCad schematic generation",
    # This automatically finds the 'circuit_gen' folder you just made
    packages=find_packages(), 
    install_requires=[
        "PySpice",
        "kicad-sch-api",
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.7",
)
