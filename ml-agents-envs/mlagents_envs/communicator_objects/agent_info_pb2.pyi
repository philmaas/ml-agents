# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents_envs.communicator_objects.observation_pb2 import (
    ObservationProto as mlagents_envs___communicator_objects___observation_pb2___ObservationProto,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class AgentInfoProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    reward = ... # type: builtin___float
    done = ... # type: builtin___bool
    max_step_reached = ... # type: builtin___bool
    id = ... # type: builtin___int
    action_mask = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool]
    team_manager_id = ... # type: builtin___int
    team_reward = ... # type: builtin___float

    @property
    def observations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[mlagents_envs___communicator_objects___observation_pb2___ObservationProto]: ...

    def __init__(self,
        *,
        reward : typing___Optional[builtin___float] = None,
        done : typing___Optional[builtin___bool] = None,
        max_step_reached : typing___Optional[builtin___bool] = None,
        id : typing___Optional[builtin___int] = None,
        action_mask : typing___Optional[typing___Iterable[builtin___bool]] = None,
        observations : typing___Optional[typing___Iterable[mlagents_envs___communicator_objects___observation_pb2___ObservationProto]] = None,
        team_manager_id : typing___Optional[builtin___int] = None,
        team_reward : typing___Optional[builtin___float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> AgentInfoProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"action_mask",u"done",u"id",u"max_step_reached",u"observations",u"reward",u"team_manager_id",u"team_reward"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"action_mask",b"action_mask",u"done",b"done",u"id",b"id",u"max_step_reached",b"max_step_reached",u"observations",b"observations",u"reward",b"reward",u"team_manager_id",b"team_manager_id",u"team_reward",b"team_reward"]) -> None: ...
