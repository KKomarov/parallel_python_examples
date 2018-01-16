from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank + 1) ** 2

if rank != 0:
    print('Sending', data, 'from process', rank)
    data = comm.gather(data, root=0)

if rank == 0:
    print('Rank', rank, 'start data receiving')
    data = comm.gather(data, root=0)
    for i in range(1, size):
        value = data[i]
        print('Process', rank, 'received', value, 'from process', i)
