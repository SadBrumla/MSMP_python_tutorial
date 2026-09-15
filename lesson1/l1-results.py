# 1. CVIČENÍ

# 1.1 Definování proměnných
r = 287.15        
p1 = 95000      
kappa = 1.4    
T1 = 273.15 + 25  

epsilon = 16.0      # Kompresní poměr (v1 / v2)
alpha = 1.5         # Stupeň zvýšení tlaku (p3 / p2) - hoření při konst. objemu
beta = 1.8          # Stupeň plnění / předběžné expanze (v4 / v3) - hoření při konst. tlaku

# 1.2 Výpočet stavových veličin v bodě 1
v1 = (r * T1) / p1
print(f"Bod 1: p={p1} Pa, T={T1} K, v={v1} m3/kg")

# 1.3 Bod 2: Izoentropická komprese (1 -> 2)
v2 = v1 / epsilon
p2 = p1 * (epsilon ** kappa)
T2 = T1 * (epsilon ** (kappa - 1))
print(f"Bod 2: p={p2} Pa, T={T2} K, v={v2} m3/kg")

# 1.4 Bod 3: Izochorický přívod tepla (2 -> 3)
v3 = v2
p3 = p2 * alpha
T3 = T2 * alpha  
print(f"Bod 3: p={p3} Pa, T={T3} K, v={v3} m3/kg")

# 1.5 Bod 4: Izobarický přívod tepla (3 -> 4)
p4 = p3
v4 = v3 * beta
T4 = T3 * beta   
print(f"Bod 4: p={p4} Pa, T={T4} K, v={v4} m3/kg")

# 1.6 Bod 5: Izoentropická expanze (4 -> 5)
v5 = v1
T5 = T4 * ((v4 / v5) ** (kappa - 1))
p5 = p4 * ((v4 / v5) ** kappa)
print(f"Bod 5: p={p5} Pa, T={T5} K, v={v5} m3/kg")