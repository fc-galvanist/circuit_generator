# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 Ferric Collective <galvanist@ferric-collective.org>


# Import the main Facade class
from .core import CircuitFacade

# Import specific constants or utilities if needed
from .simulation import list_supported_sims

# Define what is accessible when someone uses 'from circuit_gen import *'
__all__ = ['CircuitFacade', 'list_supported_sims']

# Optional: Version tracking
__version__ = "0.1.0"
