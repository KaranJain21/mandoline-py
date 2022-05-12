import sys, os
import pickle
import numpy
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 2:
        sys.exit('Must provide waypoints pickle filename')
    fname = sys.argv[1]

    if not os.path.isfile(fname):
        sys.exit('trajectory pickle file does not exist')

    # Load pickle file
    with open(fname, "rb") as pkl_handle:
        trajectory_dictionary = pickle.load(pkl_handle)

    trajectory_t = trajectory_dictionary['t']
    trajectory_pos = trajectory_dictionary['pos']
    trajectory_vel = trajectory_dictionary['vel']

    fig = plt.figure()
    ax = plt.axes(projection ='3d')

    ax.plot3D(trajectory_pos[:,0],trajectory_pos[:,1],trajectory_pos[:,2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_box_aspect([1,1.5,0.25])
    
    plt.show()

if __name__ == '__main__':
    main()
