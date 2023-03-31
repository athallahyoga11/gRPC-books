import grpc

import book_pb2
import book_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)

        # Create a new book
        book = {
            'id': '1',
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': 'J.K. Rowling',
            'description': 'The first book in the Harry Potter series',
            'price': 9.99
        }
        response = stub.CreateBook(book_pb2.Book(**book))
        print('Book created:', response)

        # Read a book
        response = stub.ReadBook(book_pb2.Book(id='1'))
        print('Book found:', response)

        # Update a book
        book['description'] = 'The first book in the Harry Potter series, now in a new edition'
        response = stub.UpdateBook(book_pb2.Book(**book))
        print('Book updated:', response)

        # Delete a book
        response = stub.DeleteBook(book_pb2.Book(id='1'))
        print('Book deleted')

if __name__ == '__main__':
    run()
