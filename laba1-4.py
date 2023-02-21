map_ = {frozenset(("красный", "синий")): "фиолетовый", frozenset(("красный", "желтый")): "оранжевый", frozenset(("синий", "желтый")): "зеленый", **{frozenset((color,)): color for color in ("красный", "синий", "желтый")}}
from_, to = (input() for _ in range(2))
result = map_.get(frozenset((from_, to)), "ошибка цвета")
print(result)