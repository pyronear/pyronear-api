# (generated with --quick)

import chardet.chardistribution
import chardet.codingstatemachine
import chardet.enums
import chardet.jpcntx
import chardet.mbcharsetprober
from typing import Any, Dict, Tuple, Type, Union

CodingStateMachine: Type[chardet.codingstatemachine.CodingStateMachine]
EUCJPContextAnalysis: Type[chardet.jpcntx.EUCJPContextAnalysis]
EUCJPDistributionAnalysis: Type[chardet.chardistribution.EUCJPDistributionAnalysis]
EUCJP_SM_MODEL: Dict[str, Union[int, str, Tuple[int, ...]]]
MachineState: Type[chardet.enums.MachineState]
MultiByteCharSetProber: Type[chardet.mbcharsetprober.MultiByteCharSetProber]
ProbingState: Type[chardet.enums.ProbingState]

class EUCJPProber(chardet.mbcharsetprober.MultiByteCharSetProber):
    _state: int
    charset_name: str
    coding_sm: chardet.codingstatemachine.CodingStateMachine
    context_analyzer: chardet.jpcntx.EUCJPContextAnalysis
    distribution_analyzer: chardet.chardistribution.EUCJPDistributionAnalysis
    language: str
    def __init__(self) -> None: ...
    def feed(self, byte_str) -> Any: ...
    def get_confidence(self) -> Any: ...
    def reset(self) -> None: ...
