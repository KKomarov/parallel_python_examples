from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 1
send_data = (rank + 1) * numpy.arange(size, dtype=int)
recv_data = numpy.empty(size * a_size, dtype=int)
comm.Alltoall(send_data, recv_data)

print('Process %s send %s receive %s' % (rank, send_data, recv_data))
