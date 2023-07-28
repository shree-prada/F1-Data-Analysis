from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'MOntreal', 'R')

session.load()
fast_leclerc = session.laps.pick_driver('VER').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

fast_sirHam = session.laps.pick_driver(44).pick_fastest()
Ham_car_data = fast_sirHam.get_car_data()
th = Ham_car_data['Time']
HCar = Ham_car_data['Speed']

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.plot(th, HCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
plt.show()