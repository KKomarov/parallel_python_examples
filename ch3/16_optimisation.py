from mpi4py import MPI
import numpy as np

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
neighbour_processes = [0, 0, 0, 0]

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_rows = int(np.floor(np.sqrt(comm.size)))
    grid_cols = comm.size // grid_rows

    if grid_rows * grid_cols > size:
        grid_cols -= 1
    if grid_rows * grid_cols > size:
        grid_rows -= 1

    if rank == 0:
        print('Building a %d x %d grid topology' % (grid_rows, grid_cols))

    cartesian_communicator = comm.Create_cart(
        (grid_rows, grid_cols), periods=(True, True), reorder=True
    )
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(
        cartesian_communicator.rank
    )
    neighbour_processes[UP], neighbour_processes[DOWN] = \
        cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = \
        cartesian_communicator.Shift(1, 1)

    print('Process = %s\
row = %s\
column = %s\
neighboor_processes[UP] = %s\
neighboor_processes[DOWN] = %s\
neighboor_processes[LEFT] = %s\
neighboor_processes[RIGHT] = %s' % (rank, my_mpi_row, my_mpi_col,
                                    neighbour_processes[UP],
                                    neighbour_processes[DOWN],
                                    neighbour_processes[LEFT],
                                    neighbour_processes[RIGHT]))
