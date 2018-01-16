from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = list(range(1, 11))
else:
    array_to_share = None

receive_buffer = comm.scatter(array_to_share, root=0)
print('Process', rank, 'received', receive_buffer)
