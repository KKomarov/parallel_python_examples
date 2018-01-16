import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 3
recv_data = numpy.zeros(array_size, dtype=numpy.int)
send_data = (rank + 1) * numpy.arange(array_size, dtype=numpy.int)

print('Process %s sending %s' % (rank, send_data))

comm.Reduce(send_data, recv_data, root=0, op=MPI.SUM)

print('On task', rank, 'after reduce: data =', recv_data)
