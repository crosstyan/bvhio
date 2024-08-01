from .BvhJoint import BvhJoint
from typing import Optional


class BvhContainer:
    """Container for the information of the bvh file.

    Root is the recursive definition of the skeleton.

    Frame time the frame time.

    Frams are the count of keyframes of the motion."""
    Root: BvhJoint
    FrameCount: int
    FrameTime: float

    def __init__(self, root: Optional[BvhJoint] = None, frameCount: Optional[int] = None, frameTime: Optional[float] = None):
        self.Root = root if root is not None else BvhJoint("Root")
        self.FrameCount = frameCount if frameCount is not None else 0
        self.FrameTime = frameTime if frameTime is not None else 0
