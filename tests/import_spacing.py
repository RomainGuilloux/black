"""The asyncio package, tracking PEP 3156."""

# flake8: noqa

import sys

# This relies on each of the submodules having an __all__ variable.
from .base_events import *
from .coroutines import *
from .events import *  # comment here

from .futures import *
from .locks import *  # comment here
from .protocols import *

from ..runners import *  # comment here
from ..queues import *
from ..streams import *

from some_library import (
    Just, Enough, Libraries, To, Fit, In, This, Nice, Split, Which, We, No, Longer, Use
)

from .a.b.c.subprocess import *
from . import (tasks)
from . import (A, B, C)
from . import SomeVeryLongNameAndAllOfItsAdditionalLetters1, \
              SomeVeryLongNameAndAllOfItsAdditionalLetters2

__all__ = (
    base_events.__all__
    + coroutines.__all__
    + events.__all__
    + futures.__all__
    + locks.__all__
    + protocols.__all__
    + runners.__all__
    + queues.__all__
    + streams.__all__
    + tasks.__all__
)


# output


"""The asyncio package, tracking PEP 3156."""

# flake8: noqa

import sys

# This relies on each of the submodules having an __all__ variable.
from .base_events import *
from .coroutines import *
from .events import *  # comment here

from .futures import *
from .locks import *  # comment here
from .protocols import *

from ..runners import *  # comment here
from ..queues import *
from ..streams import *

from some_library import (
    Just,
    Enough,
    Libraries,
    To,
    Fit,
    In,
    This,
    Nice,
    Split,
    Which,
    We,
    No,
    Longer,
    Use,
)

from .a.b.c.subprocess import *
from . import tasks
from . import A, B, C
from . import (
    SomeVeryLongNameAndAllOfItsAdditionalLetters1,
    SomeVeryLongNameAndAllOfItsAdditionalLetters2,
)

__all__ = (
    base_events.__all__
    + coroutines.__all__
    + events.__all__
    + futures.__all__
    + locks.__all__
    + protocols.__all__
    + runners.__all__
    + queues.__all__
    + streams.__all__
    + tasks.__all__
)
