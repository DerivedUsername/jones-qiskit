"""Session 0 sanity check: build a Bell state and sample it on the Aer simulator."""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

counts = AerSimulator().run(qc, shots=1000).result().get_counts()
print(qc.draw())
print(counts)  # expect roughly half '00', half '11', nothing else
