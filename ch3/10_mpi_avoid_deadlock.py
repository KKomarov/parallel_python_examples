from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print('My rank is', rank)

if rank == 1:
    data_send = 'a'
    destination = 5
    source = 5
    # send before recv
    comm.send(data_send, dest=destination)
    data_received = comm.recv(source=source)

    # Another approach
    # data_received = comm.sendrecv(data_send, dest=destination, source=source)

    print('Sending data', data_send, 'to process', destination)
    print('Received data', data_received, 'from process', source)

if rank == 5:
    data_send = 'b'
    destination = 1
    source = 1

    comm.send(data_send, dest=destination)
    data_received = comm.recv(source=source)

    print('Sending data', data_send, 'to process', destination)
    print('Received data', data_received, 'from process', source)
