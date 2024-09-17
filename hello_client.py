import grpc
import proto.schema.greeter_pb2 as greeter_pb2
import proto.schema.greeter_pb2_grpc as greeter_pb2_grpc

port = 50051
host = 'localhost'

def run():
    print('\nStarting client...')

    with grpc.insecure_channel(f'{host}:{port}') as channel:
        greeter_stub = greeter_pb2_grpc.GreeterStub(channel)
        res1 = greeter_stub.SayHello(greeter_pb2.GreetingRequest(salutation='Mr.', name='Kababa'))
        print("SayHello received: " + res1.message)

        res2 = greeter_stub.SayHello(greeter_pb2.GreetingRequest(salutation='Miss.', name='Sandie'))
        print("SayHello received: " + res2.message)
        
        res3 = greeter_stub.GetGreetingHistory(greeter_pb2.GreetingHistoryRequest(name='Mzitoh'))
        print("GetGreetingHistory received:")
        print('timestamp: ' + ''.join(res3.timestamp))
        print('messages: ', res3.messages, '\n')

if __name__ == '__main__':
    run()
