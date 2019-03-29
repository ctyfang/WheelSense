# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imumsg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imumsg.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0cimumsg.proto\"\x81\x01\n\x07IMUInfo\x12\x10\n\x08sensorID\x18\x03 \x01(\t\x12\r\n\x05\x61\x63\x63_x\x18\x01 \x01(\x02\x12\r\n\x05\x61\x63\x63_y\x18\x02 \x01(\x02\x12\r\n\x05\x61\x63\x63_z\x18\x04 \x01(\x02\x12\x11\n\tangular_x\x18\x05 \x01(\x02\x12\x11\n\tangular_y\x18\x06 \x01(\x02\x12\x11\n\tangular_z\x18\x07 \x01(\x02')
)




_IMUINFO = _descriptor.Descriptor(
  name='IMUInfo',
  full_name='IMUInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorID', full_name='IMUInfo.sensorID', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_x', full_name='IMUInfo.acc_x', index=1,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_y', full_name='IMUInfo.acc_y', index=2,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_z', full_name='IMUInfo.acc_z', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_x', full_name='IMUInfo.angular_x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_y', full_name='IMUInfo.angular_y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_z', full_name='IMUInfo.angular_z', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['IMUInfo'] = _IMUINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IMUInfo = _reflection.GeneratedProtocolMessageType('IMUInfo', (_message.Message,), dict(
  DESCRIPTOR = _IMUINFO,
  __module__ = 'imumsg_pb2'
  # @@protoc_insertion_point(class_scope:IMUInfo)
  ))
_sym_db.RegisterMessage(IMUInfo)


# @@protoc_insertion_point(module_scope)
