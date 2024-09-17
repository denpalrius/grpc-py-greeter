from concurrent import futures
import grpc
from datetime import datetime
import proto.schema.greeter_pb2 as greeter_pb2
import proto.schema.greeter_pb2_grpc as greeter_pb2_grpc

port = 50051
host = 'localhost'

class GreeterService(greeter_pb2_grpc.GreeterServicer):
    greetings_history = []
    def SayHello(self, request, context):
        print(f'\nSayHello received: {request.salutation} {request.name}')
        res_msg = f'Hello, {request.salutation} {request.name}!'
        self.greetings_history.append(res_msg)
        return greeter_pb2.GreetingResponse(message=res_msg)
    
    def GetGreetingHistory(self, request: greeter_pb2.GreetingHistoryRequest, context):
        print(f'\nGetGreetingHistory received: {request.name}')
        return greeter_pb2.GreetingHistoryResponse(
            messages = self.greetings_history, 
            timestamp = datetime.now().isoformat())
            

def serve():
    print('Starting server...')
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)

    server.add_insecure_port(f'{host}:{port}')
    server.start()

    print('Server started. Listening on port 50051.')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()