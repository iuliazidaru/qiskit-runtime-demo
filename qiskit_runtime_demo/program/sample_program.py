# This code is part of qiskit-runtime.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""A sample runtime program that submits random circuits for user-specified iterations."""

import random
from typing import Any

from qiskit_runtime_demo.libcode.random_circuit import RandomCircuit


def main(backend, user_messenger, **kwargs) -> Any:
    """Main entry point of the program.

    Args:
        backend (qiskit.providers.Backend): Backend to submit the circuits to.
        user_messenger (qiskit.providers.ibmq.runtime.UserMessenger): Used to communicate with the
            program consumer.
        kwargs: User inputs.

    Returns:
        Final result of the program.
    """
    iterations = kwargs.pop("iterations", 5)
    random_circ = RandomCircuit(iterations, backend)
    for it in range(iterations):
        qc = random_circ.create_new_random_circuit()
        result = backend.run(qc).result()
        user_messenger.publish({"iteration": it, "counts": result.get_counts()})

    return "All done!"
