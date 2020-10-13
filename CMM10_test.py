import numpy as np
import CoeffecientData as data
import AircraftDynamics as ps

if __name__ == "__main__":
	plane = ps.Plane()
	print(plane.state_vector)
	