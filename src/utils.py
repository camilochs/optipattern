# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import time

def generate_random_name(prefix, extension):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"

def write_file(content, prefix, extension="txt"):
    name_file = generate_random_name(prefix, extension)
    with open(f"outputs/{prefix}/{name_file}", "w") as f:
        f.write(content)
        print(f"{prefix} generated: outputs/{prefix}/{name_file}")
