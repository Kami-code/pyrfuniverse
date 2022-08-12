from pyrfuniverse.side_channel.side_channel import (
    IncomingMessage,
    OutgoingMessage,
)
from pyrfuniverse.rfuniverse_channel import RFUniverseChannel


class AssetChannel(RFUniverseChannel):

    def __init__(self, channel_id: str) -> None:
        super().__init__(channel_id)
        self.done = False
        self.data = {}

    def _parse_message(self, msg: IncomingMessage) -> None:
        title = msg.read_string()
        if title == 'PreLoad Done':
            print(title)
            self.done = True
        elif title == 'RFMoveColliders':
            collider = []
            object_count = msg.read_int32()
            for i in range(object_count):
                one = {}
                object_id = msg.read_int32()
                one['object_id'] = object_id
                collider_count = msg.read_int32()
                one['collider'] = []
                for j in range(collider_count):
                    collider_data = {}
                    collider_data['type'] = msg.read_string()
                    collider_data['position'] = []
                    collider_data['position'].append(msg.read_float32())
                    collider_data['position'].append(msg.read_float32())
                    collider_data['position'].append(msg.read_float32())
                    if collider_data['type'] == 'box':
                        collider_data['rotation'] = []
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['size'] = []
                        collider_data['size'].append(msg.read_float32())
                        collider_data['size'].append(msg.read_float32())
                        collider_data['size'].append(msg.read_float32())
                    elif collider_data['type'] == 'sphere':
                        collider_data['radius'] = msg.read_float32()
                    elif collider_data['type'] == 'capsule':
                        collider_data['rotation'] = []
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['rotation'].append(msg.read_float32())
                        collider_data['direction'] = msg.read_int32()
                        collider_data['radius'] = msg.read_float32()
                        collider_data['height'] = msg.read_float32()
                    one['collider'].append(collider_data)
                collider.append(one)
            self.data['colliders'] = collider
        elif title == 'CurrentCollisionPairs':
            collision_pairs = []
            pair_count = msg.read_int32()
            for i in range(pair_count):
                data = [msg.read_int32(), msg.read_int32()]
                collision_pairs.append(data)
            self.data['collision_pairs'] = collision_pairs

    def PreLoadAssetsAsync(self, names: list) -> None:
        msg = OutgoingMessage()
        msg.write_string('PreLoadAssetsAsync')
        count = len(names)
        msg.write_int32(count)
        for i in range(count):
            msg.write_string(names[i])
        self.send_message(msg)

    def LoadSceneAsync(self, file: str) -> None:
        msg = OutgoingMessage()
        msg.write_string('LoadSceneAsync')
        msg.write_string(file)
        self.send_message(msg)

    def SendMessage(self, message: str) -> None:
        msg = OutgoingMessage()
        msg.write_string('SendMessage')
        msg.write_string(message)
        self.send_message(msg)

    '''
    def InstanceObject(self, name: str, object_id: int) -> None:
        msg = OutgoingMessage()
        msg.write_string('InstanceObject')
        msg.write_string(name)
        msg.write_int32(object_id)
        self.send_message(msg)
    '''

    def InstanceObject(self, kwargs: dict) -> None:
        compulsory_params = ['name', 'id']
        self._check_kwargs(kwargs, compulsory_params)
        msg = OutgoingMessage()

        msg.write_string('InstanceObject')
        msg.write_string(kwargs['name'])
        msg.write_int32(kwargs['id'])
        self.send_message(msg)

    def IgnoreLayerCollision(self, layer1: int, layer2: int, ignore: bool) -> None:
        msg = OutgoingMessage()
        msg.write_string('IgnoreLayerCollision')
        msg.write_int32(layer1)
        msg.write_int32(layer2)
        msg.write_bool(ignore)
        self.send_message(msg)

    def GetCurrentCollisionPairs(self) -> None:
        msg = OutgoingMessage()
        msg.write_string('GetCurrentCollisionPairs')
        self.send_message(msg)

    def GetRFMoveColliders(self) -> None:
        msg = OutgoingMessage()
        msg.write_string('GetRFMoveColliders')
        self.send_message(msg)

    def SetGravity(self, gravity: list) -> None:
        msg = OutgoingMessage()
        msg.write_string('SetGravity')
        msg.write_float32(gravity[0])
        msg.write_float32(gravity[1])
        msg.write_float32(gravity[2])
        self.send_message(msg)

    def SetGroundPhysicMaterial(self, bounciness: float, dynamic_friction: float, static_friction: float, friction_combine: int, bounce_combine: int) -> None:
        msg = OutgoingMessage()
        msg.write_string('SetGroundPhysicMaterial')
        msg.write_float32(bounciness)
        msg.write_float32(dynamic_friction)
        msg.write_float32(static_friction)
        msg.write_int32(friction_combine)
        msg.write_int32(bounce_combine)
        self.send_message(msg)

    def SetTimeStep(self, delta_time: float) -> None:
        msg = OutgoingMessage()
        msg.write_string('SetTimeStep')
        msg.write_float32(delta_time)
        self.send_message(msg)

    def SetTimeScale(self, time_scale: float) -> None:
        msg = OutgoingMessage()
        msg.write_string('SetTimeScale')
        msg.write_float32(time_scale)
        self.send_message(msg)