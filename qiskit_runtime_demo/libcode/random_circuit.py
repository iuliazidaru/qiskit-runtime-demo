import random
from qiskit import transpile
from qiskit.circuit.random import random_circuit


class RandomCircuit:

    def __init__(self, iterations, backend):
        self.iterations = iterations
        self.backend = backend
        self.depth = 0

    def create_new_random_circuit(self):
        """Creates random circuits with increased circuit depth"""
        self.depth = self.depth + 1
        circuit = random_circuit(num_qubits=5, depth=self.depth, measure=True, seed=random.randint(0, 1000))
        return transpile(circuit, self.backend)