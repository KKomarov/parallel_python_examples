from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print('My rank is : ', rank)

if rank == 0:
    data = 10 ** 7
    destination_process = 4

    comm.send(data, dest=destination_process)
    print('Sending data %s' % data, 'to process %d' % destination_process)

if rank == 1:
    destination_process = 8
    data = 'hello'

    comm.send(data, dest=destination_process)
    print('Sending data %s' % data, 'to process %d' % destination_process)

if rank == 4:
    data = comm.recv(source=0)
    print('Data received is =', data)

if rank == 8:
    data = comm.recv(source=1)
    print('Data received is =', data)
