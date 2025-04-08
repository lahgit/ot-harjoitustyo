```mermaid
 classDiagram
    index.py -- SelectorForLevels
    SelectorForLevels ".selected_level" -- Level
    Level ".draw_grid" --  index.py
```
