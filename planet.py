import numpy as np


class Planet:
    def __init__(self, planet, mass, x, y, z, xv, yv, zv):
        self.planet = planet  # planet name
        self.mass = mass  # planet mass
        self.x, self.y, self.z = x, y, z  # planet positions
        self.xv, self.yv, self.zv = xv, yv, zv  # planet velocities

        self.sun_mass = 1.989e30  # sun mass
        self.xs, self.ys, self.zs = 0, 0, 0  # sun positions
        self.xvs, self.yvs, self.zvs = 0, 0, 0  # sun velocities

        self.G = 6.67e-11  # universal gravitation constant

        self.sec = 24.0 * 60 * 60  # second
        self.t = 0.0  # start time
        self.dt = 1 * self.sec  # time change (frame)

        self.coordinate_array = []

    def simulate(self):
        while self.t < 365 * self.sec:
            # distance from sun for each coordinate
            rx = self.x - self.xs
            ry = self.y - self.ys
            rz = self.z - self.zs

            distance = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5

            # force on earth
            Fx = -self.G * self.mass * self.sun_mass * rx / distance
            Fy = -self.G * self.mass * self.sun_mass * ry / distance
            Fz = -self.G * self.mass * self.sun_mass * rz / distance

            # velocity (a = F/m)
            self.xv += Fx * self.dt / self.mass
            self.yv += Fy * self.dt / self.mass
            self.zv += Fz * self.dt / self.mass

            # update position
            self.x += self.xv * self.dt
            self.y += self.yv * self.dt
            self.z += self.zv * self.dt

            # add positions to array
            self.coordinate_array.append([self.x, self.y, self.z])

            # update time
            self.t += self.dt

        return np.array(self.coordinate_array)


# create earth object
earth = Planet('Earth', 5.972e24, 1.5e11, 0, 0, 0, 29290, 0)

sim = earth.simulate()
