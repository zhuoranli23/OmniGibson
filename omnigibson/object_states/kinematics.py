from omnigibson.object_states.aabb import AABB
from omnigibson.object_states.contact_bodies import ContactBodies
from omnigibson.object_states.object_state_base import BaseObjectState
from omnigibson.object_states.pose import Pose


class KinematicsMixin(BaseObjectState):
    """
    This class is a subclass of BaseObjectState that adds dependencies
    on the default kinematics states.
    """

    @staticmethod
    def get_dependencies():
        return BaseObjectState.get_dependencies() + [Pose, AABB, ContactBodies]

    def cache_info(self, get_value_args):
        # Import here to avoid circular imports
        from omnigibson.objects.stateful_object import StatefulObject

        # Run super first
        info = super().cache_info(get_value_args=get_value_args)

        # Store this object as well as any other objects from @get_value_args
        info[self.obj] = self.obj.states[Pose].get_value()
        for arg in get_value_args:
            if isinstance(arg, StatefulObject):
                info[arg] = arg.states[Pose].get_value()

        return info

    def _cache_is_valid(self, get_value_args):
        # Import here to avoid circular imports
        from omnigibson.objects.stateful_object import StatefulObject

        # Cache is valid if and only if all of our cached objects have not changed
        t = self._cache[get_value_args]["t"]
        for obj, pose in self._cache[get_value_args]["info"].items():
            if isinstance(obj, StatefulObject):
                if obj.states[Pose].has_changed(get_value_args=(), value=pose, info={}, t=t):
                    return False
        return True
