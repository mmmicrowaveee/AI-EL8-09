# TugasAI_ControlSystem
# Multi-Agent System — Westworld

## 1. Project Information

- **Project:** Westworld
- **Category:** Multi-Agent System
- **Repository:** https://github.com/TheoLvs/westworld
- **Operating System:** Windows
- **IDE:** Visual Studio Code
- **Python Version:** 3.9.13
- **Pygame Version:** 2.6.1

## 2. Project Description

Westworld is a Python library for developing agent-based simulations. It supports agents interacting within a shared environment and provides tools for simulating agent movement and behavior.

For this local test, a grid-based simulation was configured with three rabbit agents and twenty food objects.

## 3. Installation

The project was cloned and executed locally on Windows.

A Python virtual environment was created to isolate project dependencies.

```powershell
py -3.9 -m venv .venv
```

Dependencies were installed using:

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

Additional dependencies required during troubleshooting included:

```powershell
.\.venv\Scripts\python.exe -m pip install pywin32 ipywidgets
```

## 4. Running the Simulation

The simulation was executed using:

```powershell
.\.venv\Scripts\python.exe quickstart.py
```

The simulation configuration specified:
- Environment: 20 × 10 grid
- Rabbit agents: 3
- Food objects: 20
- Simulation steps: 50
- Target frame rate: 10 FPS
- Output format: GIF

## 5. Testing Results

| Test | Observed Result | Status |
|---|---|---|
| Python environment | Python 3.9.13 | PASS |
| Pygame import | Pygame 2.6.1 initialized | PASS |
| Dependency installation | Installation completed | PASS |
| Simulation execution | Program reached episode execution | PASS |
| GIF output | Saving GIF message and image output displayed | PASS |
| Visual behavior verification | Requires inspection of the GIF | PENDING |

## 6. Output

The terminal reported the generated GIF path:

`captures/Quickstart_1792126977.gif`

The output also included an interactive widget with a play control and a maximum step value of 50.

## 7. Conclusion

The Westworld package was installed and executed locally using Python 3.9.13 on Windows. The program reached the simulation and output-generation stages and reported a GIF output path.

Further visual inspection is required to confirm the actual movement and interaction of agents throughout the simulation.
