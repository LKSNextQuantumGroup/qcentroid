from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer

def run(input_data, solver_params, extra_arguments):
    #logger.info("Starting Solver...")

    # This is your solver's code

    #size = int(input_data['size'])
    size=100
    backend = Aer.get_backend('qasm_simulator')

    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()
    
    tqc = transpile(qc, backend)
    result = backend.run(tqc, shots=size).result()
    counts = result.get_counts()
    print(counts)
    output = {'shots': counts}
    # And this is the output it returns, which is a dictionary
    return output
