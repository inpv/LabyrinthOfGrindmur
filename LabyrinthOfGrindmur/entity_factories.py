from entity import Entity

player = Entity(1, 16, char="@", color=(255, 255, 255), name="Player", blocks_movement=True)
npc = Entity(21, 16, char="S", color=(255, 255, 0), name="Enemy", blocks_movement=True)
