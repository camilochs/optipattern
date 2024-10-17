# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import time
from pathlib import Path

def generate_random_name(prefix, extension):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"

def write_file(content, prefix, extension="txt"):
    name_file = generate_random_name(prefix, extension)
    path = Path(f"outputs/{prefix}/")
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

    with open(f"{path.as_posix()}/{name_file}", "w") as f:
        f.write(content)
        print(f"{prefix} generated: outputs/{prefix}/{name_file}")
