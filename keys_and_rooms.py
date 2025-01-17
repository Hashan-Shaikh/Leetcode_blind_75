class Solution(object):
    def canVisitAllRooms(self, rooms):
        stack = [rooms[0]]
        visited_rooms = [0]
        while stack:
            keys = stack.pop()
            for k in keys:
                if k not in visited_rooms:
                    stack.append(rooms[k])
                    visited_rooms.append(k)

        if len(visited_rooms) == len(rooms):
            return True
        else:
            return False

        