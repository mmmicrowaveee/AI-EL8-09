# Expert System — Fuzzy Logic Auto-Braking Controller

## 1. Project Information

| Attribute | Description |
|---|---|
| Project Name | Fuzzy Logic System Jupyter |
| AI Category | Fuzzy Logic / Rule-Based Decision System |
| Application | Automatic Car Braking Controller |
| Programming Language | Python |
| Development Environment | Jupyter Notebook, Visual Studio Code |
| Operating System | Windows |
| Repository | https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter |

## 2. Project Description

This project demonstrates the application of fuzzy logic for an automatic car braking controller. The system models braking decisions using fuzzy membership functions and a rule-based inference mechanism.

Fuzzy logic allows the system to represent input conditions through degrees of membership ranging from 0 to 1. The applicable fuzzy rules are combined to produce an aggregated output, which can subsequently be converted into a crisp numerical value through defuzzification.

The project is intended to demonstrate how a rule-based decision system can determine an appropriate braking response based on vehicle conditions.

## 3. System Requirements

- Windows operating system
- Git
- Python 3.9
- Visual Studio Code
- Jupyter Notebook
- Python libraries:
  - NumPy
  - scikit-fuzzy
  - SciPy
  - Matplotlib
  - ipywidgets

## 4. Installation

### Step 1 — Clone the Repository

Open PowerShell and execute:

```powershell
cd D:\
git clone https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter.git
cd Fuzzy-Logic-System-Jupyter
```

### Step 2 — Create a Virtual Environment

```powershell
py -3.9 -m venv .venv
```

### Step 3 — Install the Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip

.\.venv\Scripts\python.exe -m pip install jupyter scikit-fuzzy numpy scipy matplotlib ipywidgets
```

### Step 4 — Start Jupyter Notebook

```powershell
.\.venv\Scripts\python.exe -m jupyter notebook
```

Open the project notebook located in the `Auto Braking Car Controller` directory.

## 5. System Workflow

The fuzzy logic controller follows these general stages:

1. Define the input and output variables.
2. Define fuzzy membership functions.
3. Evaluate the fuzzy rules.
4. Aggregate the rule outputs.
5. Apply defuzzification to calculate a crisp output.

The output represents the controller's calculated braking response according to the model implemented in the notebook.

## 6. Local Execution and Testing

The project was opened in Jupyter Notebook on a Windows laptop.

The following observations were recorded during testing:

| Test | Observation | Status |
|---|---|---|
| Repository setup | Project files opened locally | PASS |
| Jupyter Notebook | Notebook opened in a local browser | PASS |
| Fuzzy visualization | Aggregated membership graph displayed | PASS |
| Defuzzification | Execution stopped because `braking_force` was undefined | FAIL |
| Complete end-to-end execution | Final numerical output not verified | PENDING |

### Observed Error

```text
NameError: name 'braking_force' is not defined
```

An additional import error was also encountered while importing the `skfuzzy.control` module. The complete cause of that error has not yet been verified.

These issues may require correcting notebook execution order, checking the active Python kernel, or resolving dependency compatibility.

## 7. Results and Discussion

The notebook successfully displayed a graph titled **"Aggregated membership and result (line)"**. The visualization showed fuzzy membership curves and an orange aggregated output region.

However, the notebook encountered an error during the defuzzification stage because the variable `braking_force` was not defined in the active execution context.

Therefore, the visualization demonstrates that part of the fuzzy modeling workflow was executed, but the final crisp braking-force output has not been confirmed.

## 8. Conclusion

This project demonstrates the use of fuzzy logic and rule-based inference for an automatic braking controller.

Local setup and notebook visualization were partially successful. Further debugging is required to resolve the missing variable and import issues before the complete inference and defuzzification process can be considered successful.

The project is a simulation and must not be used as a real vehicle braking controller without independent engineering validation and safety testing.

## 9. References

- GitHub Repository: https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter
- Python Documentation: https://docs.python.org/3/
- Jupyter Documentation: https://docs.jupyter.org/
- scikit-fuzzy Documentation: https://scikit-fuzzy.readthedocs.io/
