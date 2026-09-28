calculation_of_Chopper.py

print("DC CHOPPER CALCULATOR")
print("---------------------")

Vin = float(input("Enter input voltage (V): "))
duty_cycle = float(input("Enter duty cycle (%): "))

if 0 <= duty_cycle <= 100:
    D = duty_cycle / 100

    # Average output voltage for an ideal step-down chopper
    Vout = D * Vin

    print("\n--- Chopper Results ---")
    print("Duty Cycle =", duty_cycle, "%")
    print("Average Output Voltage =", round(Vout, 2), "V")
else:
    print("Duty cycle must be between 0 and 100%.")
