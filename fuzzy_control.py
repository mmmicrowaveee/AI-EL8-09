import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definisi Variabel Input (Sensor) dan Output (Aktuator Kendali)
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')
distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')
braking = ctrl.Consequent(np.arange(0, 101, 1), 'braking_force')

# 2. Fuzzification (Membership Functions)
speed['very_slow'] = fuzz.trapmf(speed.universe, [0, 0, 20, 35])
speed['slow']      = fuzz.trimf(speed.universe, [20, 40, 60])
speed['fast']      = fuzz.trimf(speed.universe, [45, 65, 85])
speed['very_fast'] = fuzz.trapmf(speed.universe, [70, 85, 100, 100])

distance['very_close'] = fuzz.trapmf(distance.universe, [0, 0, 15, 30])
distance['close']      = fuzz.trimf(distance.universe, [15, 35, 55])
distance['far']        = fuzz.trimf(distance.universe, [40, 65, 85])
distance['very_far']   = fuzz.trapmf(distance.universe, [70, 85, 100, 100])

braking['very_light'] = fuzz.trapmf(braking.universe, [0, 0, 15, 30])
braking['light']      = fuzz.trimf(braking.universe, [15, 35, 55])
braking['heavy']      = fuzz.trimf(braking.universe, [45, 65, 85])
braking['very_heavy'] = fuzz.trapmf(braking.universe, [70, 85, 100, 100])

# 3. Knowledge Base (Aturan Pakar IF-THEN Sistem Kendali)
rule1 = ctrl.Rule(speed['very_fast'] & distance['very_close'], braking['very_heavy'])
rule2 = ctrl.Rule(speed['fast'] & distance['very_close'], braking['very_heavy'])
rule3 = ctrl.Rule(speed['fast'] & distance['close'], braking['heavy'])
rule4 = ctrl.Rule(speed['slow'] & distance['close'], braking['light'])
rule5 = ctrl.Rule(speed['slow'] & distance['far'], braking['very_light'])
rule6 = ctrl.Rule(speed['very_slow'] | distance['very_far'], braking['very_light'])
rule7 = ctrl.Rule(speed['very_fast'] & distance['close'], braking['very_heavy'])
rule8 = ctrl.Rule(speed['very_fast'] & distance['far'], braking['heavy'])

# 4. Inference Engine & Control System Simulation
braking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
sim = ctrl.ControlSystemSimulation(braking_ctrl)

# 5. Pengujian Crisp Input Sensor
input_speed = 78     # km/jam
input_distance = 18  # meter
sim.input['speed'] = input_speed
sim.input['distance'] = input_distance

# 6. Defuzzification
sim.compute()
output_brake = sim.output['braking_force']

print("====================================================")
print("   EXPERT SYSTEM: FUZZY AUTONOMOUS BRAKING CONTROL  ")
print("====================================================")
print(f"Input Sensor Kecepatan (Speed)   : {input_speed} km/h")
print(f"Input Sensor Jarak (Distance)    : {input_distance} m")
print(f"Output Aktuator Pengereman       : {output_brake:.2f} %")
print("====================================================")

# 7. Tampilkan Grafik Hasil Defuzzification
braking.view(sim=sim)
plt.show()