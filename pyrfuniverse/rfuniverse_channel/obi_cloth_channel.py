from pyrfuniverse.side_channel.side_channel import (
    IncomingMessage,
    OutgoingMessage,
)
from pyrfuniverse.rfuniverse_channel import InstanceChannel


class ObiClothChannel:

    def __init__(self, channel: InstanceChannel) -> None:
        self.data = {}
        self.channel = channel

    def _parse_message(self, msg: IncomingMessage) -> None:
        id = msg.read_int32()
        this_object_data = {}
        '''
        name = msg.read_string()
        if name[-7:] == '(Clone)':
            name = name[:-7]
        this_object_data['name'] = name
        # Number of particles
        number_of_particles = msg.read_int32()
        this_object_data['number_of_particles'] = number_of_particles
        # Positions
        raw_positions = msg.read_float32_list()
        this_object_data['positions'] = self._parse_raw_list(raw_positions)
        '''
        self.data[id] = this_object_data
        self.channel.data[id] = this_object_data

    def _parse_raw_list(self, raw_list):
        length = len(raw_list)
        assert length % 3 == 0
        number_of_parts = length // 3
        norm_list = []
        for j in range(number_of_parts):
            transform = [raw_list[3 * j], raw_list[3 * j + 1], raw_list[3 * j + 2]]
            norm_list.append(transform)

        return norm_list

    def set_action(self, action: str, **kwargs) -> None:
        self.channel.set_action(action, **kwargs)