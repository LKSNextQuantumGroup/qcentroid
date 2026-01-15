from qiskit import QuantumCircuit, Aer, execute, IBMQ

def run(input_data, solver_params, extra_arguments):
    #logger.info("Starting Solver...")

    # This is your solver's code

    #size = int(input_data['size'])
    size=1
    backend = Aer.get_backend('qasm_simulator')

    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()

    job = execute(qc, backend=backend, shots=size, memory=True)
    individual_shots = job.result().get_memory()

    #logger.info("Ending Solver...")
    shots = ''
    for i in individual_shots:
        shots += i

    output = {'shots': shots}
    # And this is the output it returns, which is a dictionary
    return output
