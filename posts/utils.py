# utils.py
import numpy as np

def print_hamiltonian(op):
    """
    Parses a SparsePauliOp and prints it in a clean format:
    0.50 * ZZ + 0.20 * XX
    """
    terms = []
    # op.label_iter() returns pairs of (pauli_string, coefficient)
    # Note: Depending on Qiskit version, you might iterate zip(op.paulis, op.coeffs)
    for pauli, coeff in zip(op.paulis, op.coeffs):
        # coeff is complex, but usually real for Hamiltonians.
        c_val = coeff.real if np.isclose(coeff.imag, 0) else coeff
        terms.append(f"{c_val:.2f} * {pauli}")
    
    print(" + ".join(terms))