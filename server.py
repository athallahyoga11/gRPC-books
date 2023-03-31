from concurrent import futures
import grpc
import pymongo

import book_pb2
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['bookstore']
        self.collection = self.db['books']

    def CreateBook(self, request, context):
        book = {
            'id': request.id,
            'title': request.title,
            'author': request.author,
            'description': request.description,
            'price': request.price
        }
        result = self.collection.insert_one(book)
        book['_id'] = str(result.inserted_id)
        return book_pb2.Book(**book)

    def ReadBook(self, request, context):
        book = self.collection.find_one({'id': request.id})
        if book:
            book['_id'] = str(book['_id'])
            return book_pb2.Book(**book)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found')
            return book_pb2.Book()

    def UpdateBook(self, request, context):
        book = {
            'id': request.id,
            'title': request.title,
            'author': request.author,
            'description': request.description,
            'price': request.price
        }
        result = self.collection.update_one({'id': request.id}, {'$set': book})
        if result.modified_count == 1:
            return book_pb2.Book(**book)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found')
            return book_pb2.Book()

    def DeleteBook(self, request, context):
        result = self.collection.delete_one({'id': request})
        if result.deleted_count == 1:
            return google.protobuf.empty_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found')
            return google.protobuf.empty_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Starting server...')
    serve()
