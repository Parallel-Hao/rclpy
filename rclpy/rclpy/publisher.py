# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rclpy.impl.implementation_singleton import rclpy_implementation as _rclpy

import time

class Publisher:

    def __init__(self, publisher_handle, msg_type, topic, qos_profile, node_handle, raw):
        self.publisher_handle = publisher_handle
        self.msg_type = msg_type
        self.topic = topic
        self.qos_profile = qos_profile
        self.node_handle = node_handle
        self._use_proto_ = False
        self.raw = raw
        if hasattr(self.msg_type, '_use_proto_'):
            self._use_proto_ = True

    def publish(self, msg):
        if self.raw:
            assert isinstance(msg, bytes)
            _rclpy.rclpy_publish_serialized(self.publisher_handle, msg)
            return
        if self._use_proto_:
            t0 = time.time()
            raw = msg.SerializeToString()
            t1 = time.time()
            lat = (t1 - t0) * 1e3
            print("Serialize: " + str(lat) + ' ms')
            _rclpy.rclpy_publish_serialized(self.publisher_handle, raw)
        else:
            _rclpy.rclpy_publish(self.publisher_handle, msg)
