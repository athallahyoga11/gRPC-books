# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\x12\tbookstore\x1a\x1bgoogle/protobuf/empty.proto\"U\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x02\"\x1d\n\x0fReadBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1f\n\x11\x44\x65leteBookRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xea\x01\n\x0b\x42ookService\x12.\n\nCreateBook\x12\x0f.bookstore.Book\x1a\x0f.bookstore.Book\x12\x37\n\x08ReadBook\x12\x1a.bookstore.ReadBookRequest\x1a\x0f.bookstore.Book\x12.\n\nUpdateBook\x12\x0f.bookstore.Book\x1a\x0f.bookstore.Book\x12\x42\n\nDeleteBook\x12\x1c.bookstore.DeleteBookRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=54
  _BOOK._serialized_end=139
  _READBOOKREQUEST._serialized_start=141
  _READBOOKREQUEST._serialized_end=170
  _DELETEBOOKREQUEST._serialized_start=172
  _DELETEBOOKREQUEST._serialized_end=203
  _BOOKSERVICE._serialized_start=206
  _BOOKSERVICE._serialized_end=440
# @@protoc_insertion_point(module_scope)