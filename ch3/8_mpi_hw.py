from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()
print('Hello world from process', rank)
