"""
The task object class. Using this class (instead of plain dictionaries)
enforces document structure.
"""
from bson.objectid import ObjectId


class TaskItem(object):
    def __init__(self, _id=None, user_id=None, taskname=None,
                 description=None, datetime_due=None, priority=-1, done=False):
        if _id is None:
            self._id = ObjectId()
        else:
            self._id = _id
        self.user_id = user_id
        self.taskname = taskname
        self.description = description
        self.datetime_due = datetime_due
        self.priority = priority
        self.done = done

    def document(self):
        """
        Return dictionary representation of this TaskItem.
        """
        return self.__dict__

    def idstr(self):
        """
        Return a string representation of the TaskItem ID for use in templates.
        """
        return str(self._id)
