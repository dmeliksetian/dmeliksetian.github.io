# Series Bible: Quantum Diagonalization Blog

## 1. Tone and Voice
* **The Persona:** A Computer Scientist and Engineer (not just a physicist) documenting a "Learning Sprint."
* **The Vibe:** "Lab Notebook meets Engineering Blog." It is rigorous but narrative-driven. We use first-person ("I ran this," "We must solve").
* **The Philosophy:** "Math into Metal." We don't just state equations; we map them to data structures and hardware constraints.
* **Key stylistic elements:**
    * Use analogies (e.g., "The Quantum Wall," "The Classical Driver," "Fitting a round peg into a square hole").
    * Acknowledge "The Reality Check" – always explain why the naive theoretical approach fails in practice (e.g., exponential scaling, lack of entanglement).

## 2. Formatting Rules (Quarto/Markdown)
* **Math:** Use LaTeX. Enclose in `$$` for block equations and `$` for inline.
* **Code Blocks:**
    * Must use explicit execution syntax: ` ```{python} ` (curly braces) to ensure Quarto executes them.
    * **Qiskit Version:** Strictly **Qiskit 1.0+ (V2 Primitives)**. Use `StatevectorEstimator`, `StatevectorSampler`, and `SparsePauliOp`.
    * **Output Handling:** Always index `result.data.evs[0]` or cast to `float()` to avoid printing array brackets.
    * **Hidden Setup:** Use `#| echo: false` for setup blocks (like path appending for `utils.py`).
* **Images:**
    * Use relative paths: `image: img/filename.png` in YAML and `![Alt](img/filename.png)` in body.
    * Diagrams are preferred over decorative images.
* **Callouts:** Use `::: {.callout-note collapse="true"}` for heavy mathematical proofs that might disrupt the flow.

## 3. Recurring Post Structure
Each post generally follows this "V-Shape" arc:
1.  **The Hook:** A direct link to the previous post and a statement of the current mathematical goal.
2.  **The Classical Problem:** Defining the matrix/vector mathematically first (Numpy/Linear Algebra) before touching quantum.
3.  **The Quantum Mapping:** How we translate that math into circuits and operators.
4.  **The Code (Implementation):** Working Qiskit code that reproduces the classical result.
5.  **The Complication (The "Turn"):** A section revealing why the simple solution just shown isn't enough (e.g., "Why we can't just scale up," "Why we need entanglement").
6.  **Next Steps:** A concrete teaser for the next technical milestone.

## 4. Current Context Summary
We are building a VQE (Variational Quantum Eigensolver) from scratch.
* **Post 01:** Set the roadmap (not just for molecules, but for graph spectral clustering).
* **Post 02:** Established the Linear Algebra foundation ($v^T A v \ge \lambda_0$) and the Variational Principle.
* **Post 03:** Implemented the "Engine." We mapped classical vectors to quantum states (Amplitude Encoding) and matrices to Pauli Strings (`SparsePauliOp`). We used the Estimator primitive to calculate expectation values.
* **Post 04:** Implemented the "Driver." We replaced fixed angles with parameters ($\vec{\theta}$), introduced the **Ansatz**, and closed the loop using a classical optimizer (COBYLA). We discovered that a product-state Ansatz fails to find the ground state of an entangled system (Matrix $A$), motivating the need for entangling gates (CNOTs).